"""
This file is based on: https://github.com/microsoft/ProphetNet/tree/master/CRITIC
"""
import random
import os
import argparse
import time
import openai
# from vllm import LLM, SamplingParams
from datetime import datetime
from tqdm import tqdm

from eval.evaluate import evaluate
from utils.utils import set_seed, load_jsonl, save_jsonl, construct_prompt
from utils.parser import *
from utils.data_loader import load_data
from utils.python_executor import PythonExecutor

MAX_CODE_FIX_RETRIES = 4
MAX_PROMPT_LENGTH_GPT4 = 7000
MAX_PROMPT_LENGTH_GPT35 = 15000

import subprocess

def get_git_commit_id(length=7):
    try:
        # Run the git command to get the latest commit ID
        commit_id = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()
        # Decode bytes to string
        return commit_id.decode('utf-8')[:length]
    except subprocess.CalledProcessError:
        # Handle errors if the command fails
        return "Unknown"

from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff

# define a retry decorator
def retry_with_exponential_backoff(
    func,
    initial_delay: float = 1,
    exponential_base: float = 2,
    max_delay: float = 8,
    jitter: bool = True,
    max_retries: int = 20,
    errors: tuple = (openai.error.RateLimitError, openai.error.APIConnectionError, openai.error.APIError, openai.error.ServiceUnavailableError),
):
    """Retry a function with exponential backoff."""

    def wrapper(*args, **kwargs):
        # Initialize variables
        num_retries = 0
        delay = initial_delay

        # Loop until a successful response or max_retries is hit or an exception is raised
        while True:
            try:
                return func(*args, **kwargs)
            
            # Retry on specified errors
            except errors as e:
                # Increment retries
                num_retries += 1
                print("<error>", e, "</error>")

                # Check if max retries has been reached
                if num_retries > max_retries:
                    raise Exception(
                        f"Maximum number of retries ({max_retries}) exceeded."
                    )

                # Increment the delay
                delay *= min(exponential_base * (1 + jitter * random.random()), max_delay)

                # Sleep for the delay
                time.sleep(delay)

            # Raise exceptions for any errors not specified
            except Exception as e:
                raise e

    return wrapper


# @retry(wait=wait_random_exponential(min=1, max=4), stop=stop_after_attempt(20))
@retry_with_exponential_backoff
def completion_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_name", default="gsm8k", type=str)
    parser.add_argument("--model_name_or_path", default="gpt-4", type=str)
    parser.add_argument("--prompt_type", default="pal", type=str)
    parser.add_argument("--split", default="test", type=str)
    parser.add_argument("--num_test_sample", default=-1, type=int) # -1 for full data
    parser.add_argument("--seed", default=0, type=int)
    parser.add_argument("--start", default=0, type=int)
    parser.add_argument("--end", default=-1, type=int)
    parser.add_argument("--temperature", default=0, type=float)
    parser.add_argument("--n_sampling", default=1, type=int)
    parser.add_argument("--top_p", default=0.95, type=float)
    parser.add_argument("--shuffle", action="store_true")
    parser.add_argument("--use_train_prompt_format", action="store_true")
    parser.add_argument("--code_concat", action="store_true") # Code concatenation options are checked here to determine if code snippets are concatenated or not
    parser.add_argument("--code_exec_warning", action="store_true")
    parser.add_argument("--max_func_call", default=4, type=int)
    parser.add_argument("--max_code_fix_retries", default=4, type=int)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    args.top_p = 1 if args.temperature == 0 else args.top_p # top_p must be 1 when using greedy sampling (vllm)
    args.max_code_fix_retries = min(args.max_code_fix_retries, int(args.max_func_call / 2))
    if args.prompt_type in ["cr"]:
        args.max_func_call = max(args.max_func_call, 10)
    return args

def main(args):
    initial_system_prompt = "As one of the most distinguished mathematicians, logicians, programmers, and AI scientists, you possess an unparalleled mastery over Arithmetic, Combinatorics, Number Theory, Probability Theory, Algebra, Analysis, and Geometry. You are not only intelligent and rational but also prudent and cautious. You are willing to write and execute Python code. Let's approach each problem step by step, take a deep breath, do not save your words, articulating our thoughts in detail, as detailed as possible."
    if args.prompt_type in ["cot"]:
        initial_system_prompt = "As one of the most distinguished mathematicians, logicians, programmers, and AI scientists, you possess an unparalleled mastery over Arithmetic, Combinatorics, Number Theory, Probability Theory, Algebra, Analysis, and Geometry. You are not only intelligent and rational but also prudent and cautious. Let's approach each problem step by step, take a deep breath, do not save your words, articulating our thoughts in detail, as detailed as possible."
    elif args.prompt_type in ["direct"]:
        initial_system_prompt = "As one of the most distinguished mathematicians, logicians, programmers, and AI scientists, you possess an unparalleled mastery over Arithmetic, Combinatorics, Number Theory, Probability Theory, Algebra, Analysis, and Geometry. You are not only intelligent and rational but also prudent and cautious."
    elif args.prompt_type in ["pal"]:
        initial_system_prompt = "As one of the most distinguished mathematicians, logicians, programmers, and AI scientists, you possess an unparalleled mastery over Arithmetic, Combinatorics, Number Theory, Probability Theory, Algebra, Analysis, and Geometry. You are not only intelligent and rational but also prudent and cautious. You just need to write python code."
    examples = load_data(args.data_name, args.split)

    # sample `num_test_sample` from dataset
    if args.num_test_sample > 0:
        examples = random.sample(examples, args.num_test_sample)
    
    # shuffle
    if args.shuffle:
        random.seed(datetime.now().timestamp())
        random.shuffle(examples)

    # select start and end
    if args.end == -1:
        args.end = len(examples)
    examples = examples[args.start:args.end]

    MAX_CODE_FIX_RETRIES = args.max_code_fix_retries

    # get out_file
    dt_string = datetime.now().strftime("%m-%d_%H-%M")
    model_name = "/".join(args.model_name_or_path.split("/")[-2:])
    file_prompt_type = args.prompt_type.replace("program_only", "tora")
    out_file_prefix = f'{args.split}_{file_prompt_type}_{args.num_test_sample}_seed{args.seed}_t{args.temperature}'
    commit_id = get_git_commit_id()
    out_file = f'outputs/{model_name}/{args.data_name}/{out_file_prefix}_s{args.start}_e{args.end}_{dt_string}_{commit_id}.jsonl'
    os.makedirs(f'outputs/{model_name}/{args.data_name}', exist_ok=True)

    # all files in the output folder
    processed_files = [f for f in os.listdir(f"outputs/{model_name}/{args.data_name}/") if f.endswith(".jsonl") and f.startswith(out_file_prefix)]    
    processed_samples = []
    for f in processed_files:
        if args.prompt_type not in ["cr"] and (args.model_name_or_path in ["gpt-4", "gpt-4-0314", "gpt-4-0613", "gpt-4-1106-preview"] or "gpt-4" in args.model_name_or_path):
            processed_samples.extend(list(load_jsonl(f"outputs/{model_name}/{args.data_name}/{f}")))
            print("f:", f)
        else:
            continue

    # dedepulicate
    processed_samples = {sample['idx']: sample for sample in processed_samples}
    processed_idxs = list(processed_samples.keys())
    processed_samples = list(processed_samples.values())
    total_examples = len(examples)
    examples = [example for example in examples if example['idx'] not in processed_idxs]
    print(f"Idx {args.start} - {args.end}: Remain {len(examples)}/{total_examples} samples.")
    if len(examples) == 0:
        print("No examples to process.")
        pass
        # return
    else:
        print(examples[0])

    # Initialize the Python executor based on prompt type
    if "pal" in args.prompt_type:
        executor = PythonExecutor(get_answer_expr='solution()')
    else:
        executor = PythonExecutor(get_answer_from_stdout=True)

    # load model
    if len(examples) > 0:
        available_gpus = os.environ['CUDA_VISIBLE_DEVICES'].split(',')
        # if the args.model_name_or_path is do not contain "gpt-3.5" and "gpt-4", we use the local LLM
        print ("args.model_name_or_path: ", args.model_name_or_path)
        if "gpt-3.5" not in args.model_name_or_path and "gpt-4" not in args.model_name_or_path:
            from vllm import LLM, SamplingParams
            llm = LLM(model=args.model_name_or_path, tensor_parallel_size=len(available_gpus), trust_remote_code=True, max_num_batched_tokens = 16000)
    samples = []
    for example in tqdm(examples, total=len(examples)):
        idx = example['idx']

        # parse question and answer
        example['question'] = parse_question(example, args.data_name)
        gt_cot, gt_ans = parse_ground_truth(example, args.data_name)
        full_prompt = construct_prompt(args, example)

        sample = {'idx': idx, 'question': example['question'], 'gt_cot': gt_cot, 'gt': gt_ans, 'prompt': full_prompt}

        # add remain fields
        for key in ['level', 'type', 'subject', 'unit', 'solution_type', 'choices', 'solution', 'ques_type', 'ans_type']:
            if key in example:
                sample[key] = example[key]
        samples.append(sample)  

    print("dataset:", args.data_name, "samples:", len(samples))
    if len(samples) > 0:
        print("-" * 50)
        # print("sample:", samples[0]['prompt'])
        print("-" * 50)

    # repeat n times
    remain_prompts = [sample['prompt'] for sample in samples for _ in range(args.n_sampling)]
    remain_prompts = [(i, prompt) for i, prompt in enumerate(remain_prompts)]
    end_prompts = []

    max_func_call = 1 if args.prompt_type in ['cot', 'pal'] else args.max_func_call
    stop_tokens = ["</s>", "---", "```output"]

    if args.prompt_type in ["cot"]:
        stop_tokens.append("\n\n\n\n")
    elif args.prompt_type in ['wizard_zs', 'platypus_fs']:
        stop_tokens.extend(["Instruction", "Response"])
    elif args.prompt_type in ["cr"]:
        stop_tokens.extend(["## Problem"])

    # start inference
    # measure time use
    start_time = time.time()
    for epoch in range(max_func_call):
        print("=" * 50, "Epoch", epoch)
        current_prompts = remain_prompts
        if len(current_prompts) == 0:
            break
        # if (len(current_prompts) > 0):
            # print("current prompts[0]: ", current_prompts[0])

        # get all outputs
        prompts = [item[1] for item in current_prompts]
        outputs = []
    
        # Set the split token based on prompt type
        ans_split = "<|assistant|>" if args.use_train_prompt_format else "Question:"
        if args.prompt_type in ["cr"]: ans_split = "## Problem:"

        # if the args.model_name_or_path is do not contain "gpt-3.5" and do not contain "gpt-4", we use the local LLM
        if "gpt-3.5" not in args.model_name_or_path and "gpt-4" not in args.model_name_or_path:
            outputs = llm.generate(prompts, SamplingParams(
                        temperature=args.temperature,
                        top_p=args.top_p,
                        max_tokens=1024,
                        n=1,
                        stop=stop_tokens,
            ))
            outputs = sorted(outputs, key=lambda x: int(x.request_id)) # sort outputs by request_id
            outputs = [output.outputs[0].text for output in outputs]
        else: 
            for prompt in tqdm(prompts, desc="Requesting OpenAI API"):
                if args.verbose: print("<openai request>")
                # ChatCompletion API call with individual prompts; not batched
                response = completion_with_backoff(
                    model=args.model_name_or_path,
                    messages=[{"role": "system", "content": initial_system_prompt},
                              {"role": "user", "content": prompt}],
                    max_tokens=2048,
                    temperature=args.temperature,
                    top_p=args.top_p,
                    stop=stop_tokens
                )
    
                # Append the resulting output string to the outputs list
                outputs.append(response["choices"][0]["message"]["content"])
                if args.verbose:
                    print("<prompt>", prompt.split(ans_split)[-1], "</prompt>")
                if args.verbose: print("<output>", outputs[-1], "</output>")
                if args.verbose: print("</openai request>")
       
        assert len(outputs) == len(current_prompts)

        # process all outputs
        remain_prompts = []
        remain_codes = []
        
        for (i, query), output in zip(current_prompts, outputs):
            output = output.rstrip()
            query += output
            if args.prompt_type == "pal":
                remain_prompts.append((i, query))
                if "```python" in output:
                    output = extract_program(output)
                remain_codes.append(output)
            elif args.prompt_type == "cot":
                end_prompts.append((i, query))
            # elif "boxed" not in output and output.endswith("```"):
            #     program = extract_program(output, last_only= not args.code_concat)
            #     remain_prompts.append((i, query))
            #     remain_codes.append(program)
            elif (epoch <= max_func_call - 2) and ("boxed" not in output) and (output.strip().endswith("```") or ("execute " in query.split(ans_split)[-1].strip().split("```python")[-1].split("```")[-1].lower()) or ("run the " in query.split(ans_split)[-1].strip().split("```python")[-1].split("\n")[-1].lower())): 
                program = extract_program(query.split(ans_split)[-1], last_only= not args.code_concat)
                # if args.verbose: print("<extracted program>\n", program, "\n</extracted program>\n")
                remain_prompts.append((i, query))
                remain_codes.append(program)
            elif args.prompt_type in ["cr"]:
                splited_query = query.split(ans_split)[-1]
                if args.verbose: print("<check if the output contains the final answer>")
                if ("#### Final Answer" in splited_query or "#### Revised Final Answer" in splited_query or "#### Conclusion" in splited_query or "final answer " in splited_query or " conclusion" in splited_query) and "boxed" in splited_query:
                    end_prompts.append((i, query))
                    if args.verbose: print("</check if the output contains the final answer:yes>")
                elif "### Final Answer" in splited_query:
                    query += "\n<warning>\nRecall the Mathematical Formatting Instruction, please make sure that the final answer is presented using the latex box format and devoid of any units.\n</warning>\n#### Revised Final Answer\n"
                    remain_prompts.append((i, query))
                    remain_codes.append("")
                elif (args.model_name_or_path == "gpt-4" and len(query) > MAX_PROMPT_LENGTH_GPT4) or (args.model_name_or_path in ["gpt-3.5-turbo-1106", "gpt-3.5-16k"] and len(query) > MAX_PROMPT_LENGTH_GPT35):
                    query += "\n<warning>\nPlease finish you reasoning within 1000 words.\n </warning>\n### Final Solution:\n"
                    end_prompts.append((i, query))
                    if args.verbose: print("</check if the output contains the final answer:yes>")
                elif epoch == max_func_call - 2:
                    query += "\n<warning>\nPlease finish you reasoning without using using python code.\n </warning>\n### Final Solution\n"
                    remain_prompts.append((i, query))
                    remain_codes.append("")
                    if args.verbose: print("</check if the output contains the final answer:no, has tried too many times>")
                else: 
                    remain_prompts.append((i, query))
                    remain_codes.append("")
                    if args.verbose: print("</check if the output contains the final answer:no>")
            else:
                end_prompts.append((i, query))

        # execute the remain prompts
        remain_results = executor.batch_apply(remain_codes)
        for k in range(len(remain_prompts)):
            i, query = remain_prompts[k]
            pred, report = remain_results[k]
            pred, report = str(pred).strip(), str(report).strip()
            if len(pred) > 100:
                pred = pred[:50] + "..." + pred[-50:]
            max_report_len = 200 if args.code_exec_warning else 100
            if len(report) > max_report_len:
                report = report[:int(max_report_len / 2)] + "..." + report[-int(max_report_len / 2):]
            exec_result = pred if pred else report
            if "pal" in args.prompt_type:
                exec_result = "\\boxed{" + exec_result + "}"
            exec_result = f"\n```output\n{exec_result}\n```\n"
            if args.code_exec_warning and exec_result.strip() == "":
                exec_result += "<warning>\nDid you forget to use print()?\n</warning>\n"
            if args.code_exec_warning and 'Error' in exec_result:
                # Split the query string
                split_query = query.split("Tried Times: 0")

                # Check if the split result has at least one element and if the last element is not empty
                if split_query and split_query[-1]:
                    # Count the occurrences of the warning message in the last part of the split query
                    tried_times = split_query[-1].count("<warning>\nThe previous code block") + 1
                else:
                    # If the split result is empty or the last element is empty, set tried_times to 0
                    tried_times = 0 
                # Convert the integer tried_times to a string and append the warning message to exec_result
                if tried_times <= (MAX_CODE_FIX_RETRIES - 1):
                    if args.verbose: print("Errors haven been occured.\n<extracted program>\n", remain_codes[k], "\n</extracted program>\n")
                    exec_result += "<warning>\nThe previous code block is not executable, will be removed from the code execution context. Please rewrite and fix this code block. (Tried Times: " + str(tried_times) + ")\n</warning>\n"
                    if args.code_concat and tried_times >= 1:
                        exec_result += "<current_full_code_context>\n" + remain_codes[k] + "\n</current_full_code_context>\n"
                else:
                    exec_result += "<warning>\nYou have tried to execute the code block " + str(tried_times) + " times, but it is still not executable. Please stop writing code for this question and try to solve this question manually.\n</warning>\nLet's think step by step, without using code. "
            if remain_codes[k] == "":
                exec_result = ""
            query += exec_result
            if epoch == max_func_call - 2: query += "\n<system>\nReach the max reponse limit, you must finish your reasoning and give your final solution in next reponse without resorting python code.\n</system>\n"
            # not end
            if epoch == max_func_call - 1:
                query += "\nReach max function call limit."
            remain_prompts[k] = (i, query)
        

    # unsolved samples
    print("Unsolved samples:", len(remain_prompts))
    end_prompts.extend(remain_prompts)
    # sort by idx
    end_prompts = sorted(end_prompts, key=lambda x: x[0])
    codes = [prompt.split(ans_split)[-1].strip() for _, prompt in end_prompts]
    final_programs = [extract_program(code, last_only= not args.code_concat) for code in codes]
    if len(codes) > 0:
        print("codes[0]:", codes[0])

    # extract preds
    results = [run_execute(executor, code, args.prompt_type) for code in codes]
    time_use = time.time() - start_time
    if len(results) > 0:
        print("results[0]:", results[0])

    # put results back to examples
    all_samples = []
    for i, sample in enumerate(samples):
        code = codes[i*args.n_sampling: (i+1)*args.n_sampling]
        final_program = final_programs[i*args.n_sampling: (i+1)*args.n_sampling]
        result = results[i*args.n_sampling: (i+1)*args.n_sampling]
        preds = [item[0] for item in result]
        reports = [item[1] for item in result]

        sample.pop('prompt')
        sample.update({'code': code, 'pred': preds, 'report': reports, 'final_program': final_program})
        all_samples.append(sample)

    # add processed samples
    all_samples.extend(processed_samples)
    save_jsonl(all_samples, out_file)

    result_str = evaluate(samples=all_samples, data_name=args.data_name, prompt_type=args.prompt_type, use_train_prompt_format=args.use_train_prompt_format, code_concat = args.code_concat, max_func_call = args.max_func_call, code_exec_warning=args.code_exec_warning, max_code_fix_retries = args.max_code_fix_retries, execute=True)
    result_str += f"\nTime use: {time_use:.2f}s"
    time_str = f"{int(time_use // 60)}:{int(time_use % 60):02d}"
    result_str += f"\nTime use: {time_str}"

    with open(out_file.replace(".jsonl", f"_{args.prompt_type}.metrics"), "w") as f:
        f.write(result_str)

if __name__ == "__main__":
    args = parse_args()
    set_seed(args.seed)
    main(args)
    