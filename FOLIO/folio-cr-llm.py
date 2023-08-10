# FOLIO with Cumulative Reasoning

import guidance
import ast
import torch
import argparse
import json
import time
import numpy
from tqdm import tqdm

TRY_CNT = 16


def get_parser():
    parser = argparse.ArgumentParser(description="Cumulative Reasoning")
    parser.add_argument('--temperature', type=float, default=0.1, help='temperature')
    parser.add_argument('--propnum', type=int, choices=range(0, 21), default=2, help='numbers of props')
    parser.add_argument('--reasoningnum', type=int, choices=range(0, 21), default=16, help='numbers of reasoning, when > 1, majority voting is used')
    parser.add_argument('--choices', type=int, choices=range(0, 21), default=3, help='numbers of premises to be chosen')
    parser.add_argument('--trycnt', type=int, choices=range(1, 1001), default=16, help='numbers of try times')
    parser.add_argument('--exploration_prob', type=float, default=1.00, help='exploration probability')
    parser.add_argument('--model', type=str, default='huggyllama/llama-65b', help='model to use')
    parser.add_argument('--dataset', type=str, default='data/folio/folio-wiki.jsonl', help='dataset to use')
    parser.add_argument('--verbose', type=ast.literal_eval, default=True, help='verbose mode')
    return parser

parser = get_parser()
args = parser.parse_args()

guidance.llm = guidance.llms.transformers.LLaMA(args.model, device_map="auto", token_healing=True, torch_dtype=torch.bfloat16, caching=False)



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
    {'premises': 'All people who regularly drink coffee are dependent on caffeine. People either regularly drink coffee or joke about being addicted to caffeine. ',
     'proposition': 'All people who joke about being addicted to caffeine are not dependent on caffeine.',
     'conclusion': 'Rina is either a person who regularly drinks coffee or a person who is unaware that caffeine is a drug.',
     'explanation': 'Since all people who regularly drink coffee are dependent on caffeine, those who just joke about being addicted (and don\'t regularly drink coffee) are not dependent on caffeine.'},
    {'premises': 'Any choral conductor is a musician. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
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
    {'premises': 'All people who regularly drink coffee are dependent on caffeine. People either regularly drink coffee or joke about being addicted to caffeine.',
     'proposition': 'All people who joke about being addicted to caffeine are dependent on caffeine.',
     'validation': 'False'},
    {'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician.',
     'proposition': 'Miroslav Venhoda, being a Czech choral conductor specializing in Renaissance and Baroque music, is also a musician.',
     'validation': 'True'},
    {'premises': 'Any choral conductor is a musician. Some musicians love music.',
     'proposition': 'All choral conductor love music.',
     'validation': 'False'},
    {'premises': 'Any choral conductor is a musician. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
     'proposition': 'Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
     'validation': 'True'}
]

useful_deduction_examples = [
    {'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
     'proposition': 'Miroslav Venhoda, who published a book in 1946 called Method of Studying Gregorian Chant, is a musician as he is a choral conductor.',
     'conclusion': 'A Czech person wrote a book in 1946.',
     'usefulness': 'True'},
    {'premises': 'All eels are fish. No fish are plants. A thing is either a plant or animal. Nothing that breathes is paper. All animals breathe. If a sea eel is either an eel or a plant, then a sea eel is an eel or an animal.',
     'proposition': 'No animals are paper.',
     'conclusion': 'Sea eel is an eel.',
     'usefulness': 'False'}
]

duplicated_deduction_examples = [
    {'premises': 'Miroslav Venhoda was a Czech choral conductor who specialized in the performance of Renaissance and Baroque music. Any choral conductor is a musician. Some musicians love music. Miroslav Venhoda published a book in 1946 called Method of Studying Gregorian Chant.',
     'proposition': 'Any choral conductor is a musician.',
     'conclusion': 'A Czech person wrote a book in 1946.',
     'duplicated': 'True'},
    {'premises': 'All eels are fish. No fish are plants. A thing is either a plant or animal. Nothing that breathes is paper. All animals breathe. If a sea eel is either an eel or a plant, then a sea eel is an eel or an animal.',
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
valid_judgement = ["True", "False", "Unknown"]

# we can pre-define valid option sets
valid_validation = ["True", "False"]

# we can pre-define valid option sets
valid_something = ["True", "False"]

# we can pre-define valid option sets
valid_duplicated = ["True", "False"]

# we can pre-define valid option sets
valid_sourced = ["True", "False"]


# Define the guidance program
gen_proposition = guidance(
'''
### Instruction:
Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. Please use First-Order Logic (FOL) to deduce a "Proposition" from two given "Premises". 
Please make sure that the "Proposition" is logically correct. 
Please make sure that the "Proposition" is not a duplicate of the "Premises".
Please make sure your reasoning is directly deduced from the "Premises" and "Propositions" other than introducing unsourced common knowledge and unsourced information by common sense reasoning.
Please remember that your "Proposition" should be useful to determine whether the "Hypothesis" is True, False or Unknown.
----

{{~! display the few-shot examples ~}}
{{~#each examples}}
### Input:
"Premises": "{{this.premises}}"
We want to deduce more propositions to determine the correctness of the following "Hypothesis":
"Hypothesis": "{{this.conclusion}}"

### Response:
"Proposition": "{{this.proposition}}"
---
{{~/each}}

{{~! place the real question at the end }}
### Input:
"Premises": "{{premises}}"
We want to deduce more propositions to determine the correctness of the following "Hypothesis":
"Hypothesis": "{{conclusion}}"

### Response:
"Proposition": "{{gen "proposition" temperature=temperature max_tokens=50 stop=['\\n']}}"
''')


# Define the guidance program
validate_deduction = guidance(
'''
### Instruction:
Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Please use First-Order Logic (FOL) to determine whether the deduction of two given "Premises" to a "Proposition" is valid or note, reply with True or False.
----

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
"Judgement": "Now we know that this deduction is {{select "validation" options=valid_validation}}"
''')


# Define the guidance program
duplicated_deduction = guidance(
'''
### Instruction:
Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Please determine whether the "Proposition" is literally duplicated with the "Premises", reply with True or False.
----

{{~! display the few-shot examples ~}}
{{~#each examples}}
### Input:
"Premises": "{{this.premises}}"
"Proposition": "{{this.proposition}}"

### Response:
"Judgement": "Is this proposition duplicated with the premises? {{this.duplicated}}"
---
{{~/each}}

{{~! place the real question at the end }}
### Input:
"Premises": "{{premises}}"
"Proposition": "{{proposition}}"

### Response:
"Judgement": "Is this proposition duplicated with the premises? {{select "duplicated" options=valid_duplicated}}"
''')


# Define the guidance program
sourced_deduction = guidance(
'''
### Instruction:
Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Please determine whether the "Proposition" is directly deduced from the "Premises" other than introducing unsourced information by common sense reasoning, reply with True or False.
----

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
"Judgement": "Is this proposition directly deduced from the premises? {{select "sourced" options=valid_sourced}}"
''')


# Define the guidance program
structure_program = guidance(
'''
### Instruction:
Suppose you are one of the greatest AI scientists, logicians and mathematicians. Let us think step by step. 
Read and analyze the "Premises" first, then using First-Order Logic (FOL) to judge whether the "Hypothesis" is True, False or Unknown.
Please make sure your reasoning is directly deduced from the "Premises" and "Propositions" other than introducing unsourced common knowledge and unsourced information by common sense reasoning.
----

{{~! display the few-shot examples ~}}
{{~#each examples}}
### Input:
"Premises": "{{this.premises}}"
"Hypothesis": "{{this.conclusion}}"

### Response:
"Thoughts": "Let us think step by step. From the premises, we can deduce propositions: {{this.propositions}}"
"Reasoning": "Let us think step by step. {{this.reasoning}}"
"Recall the Hypothesis": "{{this.conclusion}}"
"Judgement": "Now we know that the Hypothesis is {{this.judgement}}
---
{{~/each}}

{{~! place the real question at the end }}
### Input:
"Premises": "{{premises}}"
"Hypothesis": "{{conclusion}}"

### Response:
"Thoughts": "Let us think step by step. From the premises, we can deduce propositions: {{propositions}} ..."
"Recall the Hypothesis": "{{conclusion}}"
"Judgement": "Now we know that the Hypothesis is {{select "judgement" options=valid_judgement}}"
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
    # args.model in format 'huggyllama/llama-65b' to 'huggyllama-llama-65b'
    model_name = args.model.replace('/', '-')
    logfilename = 'results/folio/results-folio-cr-llm--' + model_name + '--t' + str(args.temperature) + '--' + dataset_name + '--n_' + str(args.propnum) + '--' + time.strftime("%Y-%m-%d-%H-%M-%S", t) + '.jsonl'
    with open(logfilename, 'w') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", t) + '\n') # write each result as a new line
        f.write('propnum: ' + str(args.propnum) + '\n')
        f.write('reasnoningnum: ' + str(args.reasoningnum) + '\n')
        f.write('choices: ' + str(args.choices) + '\n')
        f.write('exploration_prob: ' + str(args.exploration_prob) + '\n')
        f.write('trycnt: ' + str(args.trycnt) + '\n')
        f.write("Model: " + args.model + "\n")
        f.write("Temperature: " + str(args.temperature) + "\n")
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
        conclusion = example['conclusion']
        premises = example['premises']
        propositions = []
        failed_cnt = 0

        if args.verbose: print("[Premises]: \t", premises)
        if args.verbose: print("[Hypothesis]: \t", conclusion)

        while (len(propositions) < args.propnum and failed_cnt < args.trycnt):
            failed_cnt += 1

            if args.verbose: print("\t# <No. {}>".format(len(propositions) + 1))

            # args.exploration_prob determines the probability of using premises + propositions as the input of gen_proposition
            if numpy.random.rand() < args.exploration_prob:
                tmp = numpy.random.choice(premises + propositions, size=min(len(premises + propositions), args.choices), replace=False)
            else: tmp = numpy.random.choice(premises, size=min(len(premises), args.choices), replace=False)

            # generate propositions
            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    t = gen_proposition(examples=gen_proposition_examples, premises=' '.join(tmp), conclusion=conclusion, temperature=args.temperature)
                    break
                except Exception as e:
                    print("gen_proposition() failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
                    try_cnt += 1
                    continue
            
            prop = t['proposition'].strip()
            if 'Proposition\": \"' in prop:
                prop = prop.split('Proposition\": \"')[1].split('\"')[0]
            # if the first char of prop is ", then remove it
            if len(prop) > 0 and prop[0] == '"':
                prop = prop[1:]
            # if the last char of prop is ", then remove it
            if len(prop) > 0 and prop[-1] == '"':
                prop = prop[:-1]

            if prop in premises or prop in propositions:
                if args.verbose:
                    print ("\t[Raw propositions]\t", prop) 
                    print("\t\t[Is not duplicated]:\t", 'False (literally)')
                continue

            if args.verbose: 
                print("\t[Raw propositions]\t", prop)
                print("\t\t[Deduced from Premises]:\t", tmp)

            # is something to be deduced
            is_something_selection = 'False'
            # if prop begin with 'There is no' or 'No valid' or 'None of the' , then skip
            if prop.startswith('There is no') or prop.startswith('There are no') or prop.startswith('No valid') or prop.startswith('None of the') or 'no information' in prop or 'No information' in prop or 'No direct' in prop or 'No proposition' in prop or 'It is not possible to' in prop or 'the correctness of the hypothesis' in prop:
                if args.verbose: print("\t\t[Deduced something]:\t", is_something_selection)
                continue

            # try_cnt = 0
            # while try_cnt < TRY_CNT:
            #     try:
            #         is_duplicated = duplicated_deduction(examples=duplicated_deduction_examples, premises=' '.join(propositions), proposition=prop, valid_duplicated = valid_duplicated)['duplicated']
            #         break
            #     except Exception as e:
            #         print("duplicated_deduction() failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
            #         try_cnt += 1
            #         continue

            # if args.verbose: print("\t\t[Is not duplicated]:\t", 'True' if is_duplicated=='False' else 'False')
            # if is_duplicated=='True': 
            #     continue
            
            # soucred deduction
            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    sourced_local = sourced_deduction(examples=sourced_deduction_examples, premises=' '.join(tmp), proposition=prop, valid_sourced = valid_sourced)['sourced']
                    break
                except Exception as e:
                    print("sourced_deduction() local failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
                    try_cnt += 1
                    continue        

            if args.verbose: print("\t\t[Sourced local]:\t", sourced_local)
            if sourced_local=='False':
                continue

            # validate propositions
            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    validation_local = validate_deduction(examples=validate_deduction_examples, premises=' '.join(tmp), proposition=prop, valid_validation = valid_validation)['validation']
                    break
                except Exception as e:
                    print("validate_deduction() local failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
                    try_cnt += 1
                    continue
        
            if args.verbose: print("\t\t[Validation local]:\t", validation_local)
            if validation_local=='False':
                continue

            try_cnt = 0
            while try_cnt < TRY_CNT:
                try:
                    validation_global = validate_deduction(examples=validate_deduction_examples, premises=premises + propositions, proposition=prop, valid_validation = valid_validation)['validation']
                    break
                except Exception as e:
                    print("validate_deduction() global failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
                    try_cnt += 1
                    continue   
        
            if args.verbose: print("\t\t[Validation global]:\t", validation_global)
            if validation_global=='False':
                continue   

            propositions.append(prop)
            failed_cnt = 0
            if args.verbose: print("\t\t<All Test Passed>: \t", prop)

        if args.verbose: print("[Generated Propositions]: \t", propositions)

        try_cnt = 0
        while try_cnt < TRY_CNT:
            try:
                out = structure_program(
                    examples = examples,   
                    premises = ' '.join(premises),
                    propositions = ' '.join(propositions),
                    conclusion = conclusion,
                    valid_judgement = valid_judgement,
                    temperature = args.temperature,
                ) 
                break
            except Exception as e:
                print("structure_program() failed, try again... (No. {})".format(try_cnt+1), "Error:", e)
                try_cnt += 1
                continue 
            
        # select the one with the highest count

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
                "generated_propositions": propositions,
            }

        # Write the result to a JSON file, note that we open the file in append mode ('a')
        with open(logfilename, 'a') as f:
            f.write(json.dumps(result) + '\n') # write each result as a new line



if __name__ == "__main__":
    main()
