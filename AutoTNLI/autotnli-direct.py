# AutoTNLI with Direct
# @Jingqin Yang

import datasets
import guidance
import torch
import ast
import argparse
from transformers import AutoTokenizer, AutoModelForCausalLM

def get_parser():
    parser = argparse.ArgumentParser(description="Cumulative Reasoning")
    parser.add_argument('--model', type=str, default="/data/model/llama-13b", help='model to use')
    parser.add_argument('--data_dir', type=str, default="/data/datasets/AutoTNLI", help='dataset to use')
    return parser

parser = get_parser()
args = parser.parse_args()
from transformers import AutoTokenizer, AutoModelForCausalLM

dataset = datasets.load_dataset(args.data_dir, split='train')
guidance.llm = guidance.llms.transformers.LLaMA(args.model, device_map="auto", token_healing=True, torch_dtype=torch.bfloat16)

import json
import time
from tqdm import tqdm

valid_judgement = ["contradict", "entail"]

structure_program = guidance(
'''
### Instruction:
Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. Read and analyze the "Premises" first, then judge whether the "Premises" entail or contradict the "Hypothesis".
----

{{~! display the few-shot examples ~}}
{{~#each examples}}
### Input:
"Premises": "{{this.premises}}"
"Hypothesis": "{{this.hypothesis}}"

### Response:
"Judgement": "Now we know that the Premises {{this.label}} the Hypothesis."
---
{{~/each}}

{{~! place the real question at the end }}
### Input:
"Premises": "{{premises}}"
"Hypothesis": "{{hypothesis}}"

### Response:
"Judgement": "Now we know that the Premises {{select "judgement" options=valid_judgement logprobs='logprobs'}} the Hypothesis."
''')


t = time.localtime()
logfilename = 'results-autotnli-test-baseline--' + time.strftime("%Y-%m-%d-%H-%M-%S", t) + '.jsonl'
with open(logfilename, 'w') as f:
  f.write(time.strftime("%Y-%m-%d %H:%M:%S", t) + '\n')
  f.write("Model: " + args.model + "\n")
  f.write("Dataset: AutoTNLI\n")
  f.write("bf16: True\n")
  f.write("--------------------------------\n")
correct_predictions = 0
cnt = 0
total_cnt = len(dataset)

examples = [dataset[k+2] for k in range(2)]

for row in examples:
    row.update({"label": 'entail' if row['label'] == 'entailment' else 'contradict'})
print(examples)

for row in tqdm(dataset, desc="Evaluating", unit="example"):
    row.update({"label": 'entail' if row['label'] == 'entailment' else 'contradict'})
    cnt += 1
    print("-------------------------\n### Json Name: ", row['json_name'], "\t ( ", cnt, "/", total_cnt, " )")
    premises = row['premises']
    hypothesis = row['hypothesis']
    out = structure_program(
        examples=examples,
        premises=premises,
        hypothesis = hypothesis,
        valid_judgement = valid_judgement
    )

    if out["judgement"] == row["label"]:
        correct_predictions += 1

    print("[Prediction]: ", out["judgement"])
    print("[Actual]: ", row["label"])

    accuracy = correct_predictions / cnt


    print("[Running Average Accuracy]: ", accuracy)


    result = {
            "json_name": row["json_name"],
            "prediction": out["judgement"],
            "actual": row["label"],
            "accuracy": accuracy
    }
    with open(logfilename, 'a') as f:
        f.write(json.dumps(result) + '\n')
