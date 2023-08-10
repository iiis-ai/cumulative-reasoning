# FOLIO with Direct

import guidance
import torch
import argparse
import json
import time
import ast
from tqdm import tqdm


def get_parser():
    parser = argparse.ArgumentParser(description="Cumulative Reasoning")
    parser.add_argument('--verbose', type=ast.literal_eval, default=False, help='verbose mode')
    parser.add_argument('--model', type=str, default='huggyllama/llama-65b', help='model to use')
    parser.add_argument('--dataset', type=str, default='data/folio/folio-wiki.jsonl', help='dataset to use')
    return parser

parser = get_parser()
args = parser.parse_args()

# set the default language model used to execute guidance programs
guidance.llm = guidance.llms.transformers.LLaMA(args.model, device_map="auto", token_healing=True, torch_dtype=torch.bfloat16)



examples = [
    {'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
     'propositions': 'Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
     'conclusion': 'A Czech person wrote a book in 1946.',
     "reasoning": "Miroslav Venhoda, who is specified as a Czech choral conductor, published a book in 1946. Thus, it is true that a Czech person wrote a book in 1946.",
     'judgement': 'True'},
    {'premises': 'All eels are fish. No fish are plants. A thing is either a plant or animal. Nothing that breathes is paper. All animals breathe. If a sea eel is either an eel or a plant, then a sea eel is an eel or an animal.',
     'propositions': 'No eels are plants. All eels are animals.',
     'conclusion': 'Sea eel is an eel.',
     "reasoning": "all eels are fish and a sea eel is either an eel or a plant. It's also stated that no fish are plants. Therefore, a sea eel can't be a plant and must be an eel. However, there's no direct information about a sea eel being an eel.",
     'judgement': 'Unknown'},
    {'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
     'propositions': 'Miroslav Venhoda specialized in the performance of Renaissance and Baroque music.',
     'conclusion': 'No choral conductor specialized in the performance of Renaissance.',
     "reasoning": "Miroslav Venhoda, a choral conductor, specialized in the performance of Renaissance and Baroque music. Thus, it is false to conclude that no choral conductor specialized in the performance of Renaissance.",
     'judgement': 'False'},
]

# we can pre-define valid option sets
valid_judgement = ["True", "False", "Unknown"]


# Define the guidance program
structure_program = guidance(
'''
### Instruction:
Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Read and analyze the "Premises" first, then using First-Order Logic (FOL) to judge whether the "Hypothesis" is True, False or Unknown.
Please make sure your reasoning is directly deduced from the "Premises" other than introducing unsourced common knowledge and unsourced information by common sense reasoning.
----

{{~! display the few-shot examples ~}}
{{~#each examples}}
### Input:
"Premises": "{{this.premises}}"
"Hypothesis": "{{this.conclusion}}"

### Response:
"Judgement": "Now we know that the Hypothesis is {{this.judgement}}"
---
{{~/each}}

{{~! place the real question at the end }}
### Input:
"Premises": "{{premises}}"
"Hypothesis": "{{conclusion}}"

### Response:
"Judgement": "Now we know that the Hypothesis is {{select "judgement" options=valid_judgement logprobs='logprobs'}}"
''')



def main():
    # Load the data from the JSONL file
    data = []
    with open(args.dataset, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))

    t = time.localtime()

    # extract 'folio-train' from args.dataset in format 'data/folio/folio-train.jsonl'
    dataset_name = args.dataset.split('/')[2].split('.')[0]
    model_name = args.model.replace('/', '-')
    logfilename = 'results/folio/results-folio-direct-llm--' + model_name + '--' + dataset_name + '--' + time.strftime("%Y-%m-%d-%H-%M-%S", t) + '.jsonl'

    with open(logfilename, 'w') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", t) + '\n') # write each result as a new line
        f.write("Model: " + args.model + "\n")
        f.write("Dataset: " + args.dataset + "\n")
        f.write("--------------------------------\n")

    # Initialize counter for correct predictions
    correct_predictions = 0
    cnt = 0
    total_cnt = len(data)

    # Iterate over the data from the JSON file and call the solve function
    for example in tqdm(data, desc="Evaluating", unit="example"):
        cnt += 1
    
        print("-------------------------\n### Example ID: ", example["example_id"], "\t ( ", cnt, "/", total_cnt, " )")
        premises = ' '.join(example['premises'])
        conclusion = example['conclusion']
        out = structure_program(
            examples=examples,   
            premises=premises,
            conclusion = conclusion,
            valid_judgement = valid_judgement
        )

        # calculate the number of correct predictions
        if out["judgement"] == example["label"]:
            correct_predictions += 1

        print("[Prediction]: ", out["judgement"])
        print("[Actual]: ", example["label"])

        # Calculate and print the running accuracy
        accuracy = correct_predictions / cnt

        print("[Running Average Accuracy]: ", accuracy)

        result = {
                "example_id": example["example_id"],
                "prediction": out["judgement"],
                "actual": example["label"],
                "accuracy": accuracy,
            }

        # Write the result to a JSON file, note that we open the file in append mode ('a')
        with open(logfilename, 'a') as f:
            f.write(json.dumps(result) + '\n') # write each result as a new line



if __name__ == "__main__":
    main()
