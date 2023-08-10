# AutoTNLI with Cumulative Reasoning + CoT
# @Jingqin Yang

import guidance
import torch
import ast
import datasets
import numpy as np
import argparse


def get_parser():
    parser = argparse.ArgumentParser(description="Cumulative Reasoning")
    parser.add_argument('--temperature', type=float, default=0.0, help='temperature')
    parser.add_argument('--max_tokens', type=int, default=50, help='max tokens')
    parser.add_argument('--save_suffix', type=str, default='example-suffix', help='save suffix')
    parser.add_argument('--sc_cnt', type=int, choices=range(1, 30), default=1, help='number of sc cnt')
    parser.add_argument('--model', type=str, default='/data/model/llama-13b', help='model to use')
    parser.add_argument('--dataset', type=str, default='/data/datasets/AutoTNLI', help='dataset to use')
    parser.add_argument('--verbose', action='store_true', help='verbose mode')
    return parser


parser = get_parser()
args = parser.parse_args()

guidance.llm = guidance.llms.transformers.LLaMA(args.model, device_map="auto", token_healing=True,
                                                torch_dtype=torch.bfloat16, caching=False)

import json
import time
import numpy
from tqdm import tqdm

examples = [
    {
        'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
        'propositions': 'Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
        'conclusion': 'A Czech person wrote a book in 1946.',
        'judgement': 'entail'},
    {
        'premises': 'All eels are fish. No fish are plants. A thing is either a plant or animal. Nothing that breathes is paper. All animals breathe. If a sea eel is either an eel or a plant, then a sea eel is an eel or an animal.',
        'propositions': 'No eels are plants. All eels are animals.',
        'conclusion': 'Sea eel is an eel.',
        'judgement': 'contradict'},
    {
        'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
        'propositions': 'Miroslav Venhoda specialized in the performance of Renaissance and Baroque music.',
        'conclusion': 'No choral conductor specialized in the performance of Renaissance.',
        'judgement': 'contradict'},
]

gen_proposition_examples = [
    {'premises': 'All eels are fish. No fish are plants. ',
     'proposition': 'No eels are plants.',
     'conclusion': 'Sea eel is an eel.',
     'explanation': 'This expression is deduced from the two premises as follows: if x is an eel, then it is a fish (from Premise 1), and if it is a fish, then it is not a plant (from Premise 2). Thus, if x is an eel, then it is not a plant.'},
    {'premises': 'All eels are fish. A thing is either a plant or animal.',
     'proposition': 'All eels are animals.',
     'conclusion': 'Sea eel is an eel.',
     'explanation': 'This statement follows from the premises as follows: If x is an eel, then it is a fish (from Premise 1). If x is a thing (which includes being a fish, hence an eel), then it is either a plant or an animal (from Premise 2). Since it cannot be a plant (because it is a fish and no fish is a plant), it must be an animal. Thus, if x is an eel, it is an animal.'},
    {'premises': 'A thing is either a plant or animal. All animals breathe.',
     'proposition': 'All things that breathe are animals.',
     'conclusion': 'Sea eel is an eel.',
     'explanation': 'This statement is deduced from the premises as follows: If x is a thing, then it is either a plant or an animal (from Premise 1), and if x is an animal, then it breathes (from Premise 2). Therefore, if a thing breathes, it must be an animal, because it can not be a plant that breathes based on these premises.'},
    {
        'premises': 'All people who regularly drink coffee are dependent on caffeine. People either regularly drink coffee or joke about being addicted to caffeine. ',
        'proposition': 'All people who joke about being addicted to caffeine are not dependent on caffeine.',
        'conclusion': 'Rina is either a person who regularly drinks coffee or a person who is unaware that caffeine is a drug.',
        'explanation': 'Since all people who regularly drink coffee are dependent on caffeine, those who just joke about being addicted (and don\'t regularly drink coffee) are not dependent on caffeine.'},
    {
        'premises': 'Any choral conductor is a musician. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
        'proposition': 'Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
        'conclusion': 'A Czech person wrote a book in 1946',
        'explanation': 'This follows from the universal rule that any choral conductor is a musician (Premise 1), so since Miroslav Venhoda is a choral conductor who published a book in 1946 called Method of Studying Gregorian Chant (Premise 2), he is therefore a musician.'
    }
]

validate_deduction_examples = [
    {'premises': 'All eels are fish. No fish are plants.',
     'proposition': 'No eels are plants.',
     'validation': 'True'},
    {'premises': 'All eels are fish. A thing is either a plant or animal.',
     'proposition': 'All eels are animals.',
     'validation': 'True'},
    {'premises': 'Nothing that breathes is paper. All animals breathe.',
     'proposition': 'All animals are paper.',
     'validation': 'False'},
    {'premises': 'A thing is either a plant or animal. All animals breathe.',
     'proposition': 'All things that breathe are animals.',
     'validation': 'True'},
    {
        'premises': 'All people who regularly drink coffee are dependent on caffeine. People either regularly drink coffee or joke about being addicted to caffeine.',
        'proposition': 'All people who joke about being addicted to caffeine are dependent on caffeine.',
        'validation': 'False'},
    {
        'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician.',
        'proposition': 'Miroslav Venhoda, being a Czech choral conductor specializing in Renaissance and Baroque music, is also a musician.',
        'validation': 'True'},
    {'premises': 'Any choral conductor is a musician. Some musicians love music.',
     'proposition': 'All choral conductor love music.',
     'validation': 'False'},
    {
        'premises': 'Any choral conductor is a musician. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
        'proposition': 'Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
        'validation': 'True'}
]

useful_deduction_examples = [
    {
        'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
        'proposition': 'Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
        'conclusion': 'A Czech person wrote a book in 1946.',
        'usefulness': 'Useful'},
    {
        'premises': 'All eels are fish. No fish are plants. A thing is either a plant or animal. Nothing that breathes is paper. All animals breathe. If a sea eel is either an eel or a plant, then a sea eel is an eel or an animal.',
        'proposition': 'No animals are paper.',
        'conclusion': 'Sea eel is an eel.',
        'usefulness': 'Unuseful'}
]

duplicated_deduction_examples = [
    {
        'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
        'proposition': 'Any choral conductor is a musician.',
        'conclusion': 'A Czech person wrote a book in 1946.',
        'duplicated': 'True'},
    {
        'premises': 'All eels are fish. No fish are plants. A thing is either a plant or animal. Nothing that breathes is paper. All animals breathe. If a sea eel is either an eel or a plant, then a sea eel is an eel or an animal.',
        'proposition': 'No animals are paper.',
        'duplicated': 'False'
    }
]

sourced_deduction_examples = [
    {'premises': 'All eels are fish. No fish are plants.',
     'proposition': 'No eels are plants.',
     'sourced': 'True'},
    {
        'premises': 'Nothing that breathes is paper. All animals breathe.',
        'proposition': 'All animals need food.',
        'sourced': 'False'}
]

# we can pre-define valid option sets
valid_judgement = ["entail", "contradict"]

# we can pre-define valid option sets
valid_validation = ["True", "False"]

# we can pre-define valid option sets
valid_usefulness = ["Useful", "Unuseful"]

# we can pre-define valid option sets
valid_duplicated = ["True", "False"]

# we can pre-define valid option sets
valid_sourced = ["True", "False"]

gen_proposition = guidance(
    '''
    ### Instruction:
    Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. Please deduce a "Proposition" from two given "Premises". 
    Please make sure that the "Proposition" is logically correct. 
    Please make sure that the "Proposition" is not a duplicate of the "Premises".
    Please remember that your "Proposition" should be useful to determine whether the "Premises" entail or contradict the "Hypothesis". 
    ----
    {{~! display the few-shot examples ~}}
    {{~#each examples}}
    ### Input:
    "Premises": "{{this.premises}}"
    We want to deduce more propositions to determine whether the "Premises" entail or contradict the following "Hypothesis":
    "Hypothesis": "{{this.conclusion}}"

    ### Response:
    "Proposition": "{{this.proposition}}"
    ---
    {{~/each}}

    {{~! place the real question at the end }}
    ### Input:
    "Premises": "{{premises}}"
    We want to deduce more propositions to determine whether the "Premises" entail or contradict the following "Hypothesis":
    "Hypothesis": "{{hypothesis}}"

    ### Response:
    "Proposition {{prop_id}}": "{{gen "proposition" temperature=0.7 max_tokens=50 stop='\"\\n'}}"
    ''')

# Define the guidance program
validate_deduction = guidance(
    '''
    ### Instruction:
    Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. Please determine whether the deduction of given "Premises" to a "Proposition" is True or False.

    {{~! display the few-shot examples ~}}
    {{~#each examples}}
    ### Input:
    "Premises": "{{this.premises}}"
    "Proposition": "{{this.proposition}}"

    ### Response:
    "Judgement": "Now we know that this deduction is {{this.validation}}"
    ---
    {{~/each}}

    {{~! place the real question at the end }}
    ### Input:
    "Premises": "{{premises}}"
    "Proposition": "{{proposition}}"

    ### Response:
    "Judgement": "Now we know that this deduction is {{select "validation" options=valid_validation logprobs='logprobs'}}"
    ''')

# Define the guidance program
useful_deduction = guidance(
    '''
    ### Instruction:
    Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. Please determine whether the deduction of two given "Premises" to a "Proposition" is useful to determine whether the "Premises" entail or contradict the "Hypothesis", reply with Useful or Unuseful.

    {{~! display the few-shot examples ~}}
    {{~#each examples}}
    ### Input:
    "Premises": "{{this.premises}}"
    "Proposition": "{{this.proposition}}"
    "Hypothesis": "{{this.conclusion}}"

    ### Response:
    "Judgement": "Now we know that this deduction is {{this.usefulness}} to determine whether the Premises entail or contradict the Hypothesis."
    ---
    {{~/each}}

    {{~! place the real question at the end }}
    ### Input:
    "Premises": "{{premises}}"
    "Proposition": "{{proposition}}"
    "Hypothesis": "{{hypothesis}}"

    ### Response:
    "Judgement": "Now we know that this deduction is {{select "usefulness" options=valid_usefulness logprobs='logprobs'}} to determine whether the Premises entail or contradict the Hypothesis."
    ''')

# Define the guidance program
duplicated_deduction = guidance(
    '''
    ### Instruction:
    Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. Please determine whether the "Proposition" is duplicated with the "Premises", reply with True or False.

    {{~! display the few-shot examples ~}}
    {{~#each examples}}
    ### Input:
    "Premises": "{{this.premises}}"
    "Proposition": "{{this.proposition}}"

    ### Response:
    "Judgement": "Now we know that this proposition is {{this.duplicated}} with the premises."
    ---
    {{~/each}}

    {{~! place the real question at the end }}
    ### Input:
    "Premises": "{{premises}}"
    "Proposition": "{{proposition}}"

    ### Response:
    "Judgement": "Now we know that this proposition is {{select "duplicated" options=valid_duplicated logprobs='logprobs'}} with the premises."
    ''')

# Define the guidance program
sourced_deduction = guidance(
    '''
    ### Instruction:
    Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. Please determine whether the "Proposition" is directly deduced from the "Premises" other than introducing unsourced informations by common sense reasoning, reply with True or False.

    {{~! display the few-shot examples ~}}
    {{~#each examples}}
    ### Input:
    "Premises": "{{this.premises}}"
    "Proposition": "{{this.proposition}}"

    ### Response:
    "Judgement": "Is this proposition directly deduced from the premises? {{this.sourced}}"
    ---
    {{~/each}}

    {{~! place the real question at the end }}
    ### Input:
    "Premises": "{{premises}}"
    "Proposition": "{{proposition}}"

    ### Response:
    "Judgement": "Is this proposition directly deduced from the premises? {{select "sourced" options=valid_sourced logprobs='logprobs'}}"
    ''')

# Define the guidance program
structure_program = guidance(
    '''
    ### Instruction:
    Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. Read and analyze the "Premises" first, then judge whether the "Premises" entail or contradict the "Hypothesis".
    ----

    {{~! display the few-shot examples ~}}
    {{~#each examples}}
    ### Input:
    "Premises": "{{this.premises}}"
    "Hypothesis": "{{this.conclusion}}"

    ### Response:
    "Thoughts": "Let us think step by step. From the premises, we know that {{this.propositions}}"
    "Recall the Hypothesis": "{{this.conclusion}}"
    "Judgement": "Now we know that the Premises {{this.judgement}} the Hypothesis."
    ---
    {{~/each}}

    {{~! place the real question at the end }}
    ### Input:
    "Premises": "{{premises}}."
    "Hypothesis": "{{hypothesis}}"

    ### Response:
    "Thoughts": "Let us think step by step. From the premises, we know that {{gen "proposition" temperature=temperature max_tokens=max_tokens stop='\"\\n'}}. "
    "Recall the Hypothesis": "{{hypothesis}}"
    "Judgement": "Now we know that the Premises {{select "judgement" options=valid_judgement logprobs='logprobs'}} the Hypothesis."
    ''')

data = datasets.load_dataset(args.dataset, split='train')

t = time.localtime()
logfilename = f'results-autotnli-{args.save_suffix}--' + time.strftime("%Y-%m-%d-%H-%M-%S",
                                                                                                     t) + '.jsonl'
with open(logfilename, 'w') as f:
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", t) + '\n')  # write each result as a new line
    f.write("Model: " + args.model + "\n")
    f.write("Dataset: " + args.dataset + "\n")
    f.write(f"Temperature:{args.temperature}\n")
    f.write(f"Max Tokens:{args.max_tokens}\n")
    f.write("bf16: True\n")
    f.write("--------------------------------\n")

correct_predictions = 0
cnt = 0
total_cnt = len(data)

data_list = []
for i in data:
    if cnt == 1000:
        break
    data_list.append(i)
    cnt += 1

cnt = 0

for example in tqdm(data_list, desc="Evaluating", unit="example"):
    example.update({"label": 'entail' if example['label'] == 'entailment' else 'contradict'})
    cnt += 1
    conclusion = example['hypothesis']
    premises = [s + '.' for s in example['premises'].split('.')]
    premises_cnt = len(example['premises'])
    propositions = ""
    failed_cnt = 0

    if args.verbose: print("[Premises]: \t", premises)
    if args.verbose: print("[Hypothesis]: \t", conclusion)

    ans_dict = {}
    for i in valid_judgement:
        ans_dict[i] = 0

    for i in range(args.sc_cnt):
        out = structure_program(
            examples=examples,
            premises=(' '.join(premises)),
            hypothesis=conclusion,
            valid_judgement=valid_judgement,
            temperature=0.7,
            max_tokens=args.max_tokens
        )
        ans_dict[out['judgement']] = ans_dict[out['judgement']] + 1

    ans, ans_cnt = '', 0
    for i in ans_dict.keys():
        if ans_dict[i] > ans_cnt:
            ans = i
            ans_cnt = ans_dict[i]

    if ans == example["label"]:
        correct_predictions += 1

    print("[Prediction]: ", ans)
    print("[Actual]: ", example["label"])

    accuracy = correct_predictions / cnt

    print("[Running Average Accuracy]: ", accuracy)

    result = {
        "json_name": example["json_name"],
        "prediction": ans,
        "actual": example["label"],
        "accuracy": accuracy,
        "generated_propositions": propositions,
    }
    with open(logfilename, 'a') as f:
        f.write(json.dumps(result) + '\n') 
