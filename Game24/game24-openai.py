# Game of 24 with Cumulative Reasoning
# @Jingqin Yang

import guidance
import re
import sympy
import ast
import os
import json
import pandas as pd
import argparse
import openai
# openai.proxy = "http://..."

os.environ["OPENAI_API_KEY"] = 'sk-...'

def get_parser():
    parser = argparse.ArgumentParser(description="Cumulative Reasoning")
    parser.add_argument('--trycnt', type=int, choices=range(0, 1001), default=50, help='numbers of try times')
    parser.add_argument('--model', type=str, default='gpt-4-0314', help='model to use')
    parser.add_argument('--resume', type=int, default=0, help='resume point')
    parser.add_argument('--resume_cor', type=int ,default=0, help='resume pre correct cnt')
    parser.add_argument('--b', type=int, default=1, help='number of branches, default is set to be 1')
    return parser

parser = get_parser()
args = parser.parse_args()

guidance.llm = guidance.llms.OpenAI(
    args.model,
    caching=False
)

import numpy
from tqdm import tqdm


valid_output = ["sure", "likely", "impossible"]

def is_sure(output):
    return output == 'sure'

expand_program = guidance(
    ''' 
    {{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. You are very good at basic arithmetic operations. Use numbers and basic arithmetic operations (+ - * /) to obtain 24 with input numbers. You need to combine the given intermediate steps step by step into a complete expression.{{/system}}
    
    {{#user}}    
    Input: 1, 1, 4, 6
    Intermediate steps:
    1 * 4 = 4 (left 1, 4, 6)
    1 * 4 * 6 = 24
    {{/user}}
    {{#assistant}}
    Draft:
    Because 1 * 4 * 6 = 24, while 1 * 4 = 4. So 1 * (1 * 4) * 6 = 24.  
    Output:
    1 * (1 * 4) * 6 = 24
    {{/assistant}}
    
    
    {{#user}}    
    Input: 1, 10, 11, 12
    Intermediate steps:
    12 - 10 = 2 (left 1, 2, 11)
    1 + 11 = 12 (left 2, 12)
    12 * 2 = 24
    {{/user}}
    {{#assistant}}
    Draft:
    Because 12 * 2 = 24, while 12 = 1 + 11. So (1 + 11) * 2 = 24. 
    Because (1 + 11) * 2 = 24, while 2 = 12 - 10. So (1 + 11) * (12 - 10) = 24. 
    Output:
    (1 + 11) * (12 - 10) = 24
    {{/assistant}}
    
    {{#user}}    
    Input: 5, 6, 6, 9
    Intermediate steps:
    6 * 9 = 54 (left 5, 6, 54)
    5 * 6 = 30 (left 30, 54)
    54 - 30 = 24
    {{/user}}
    {{#assistant}}
    Draft:
    Because 54 - 30 = 24, while 5 * 6 = 30. So 54 - (5 * 6) = 24.
    Because 54 - (5 * 6) = 24, while 6 * 9 = 54. So (6 * 9) - (5 * 6) = 24.
    Output:
    (6 * 9) - (5 * 6) = 24.    
    {{/assistant}}
    
    {{#user}}    
    Input: 2 7 8 9
    Intermediate steps:
    7 + 9 = 16 (left 2, 8, 16)
    2 * 16 = 32 (left 8, 32)
    32 - 8 = 24
    {{/user}}
    {{#assistant}}
    Draft:
    Because 32 - 8 = 24, while 32 = 2 * 16. So (2 * 16) - 8 = 24.
    Because (2 * 16) - 8 = 24, while 7 + 9 = 16. So (2 * (7 + 9)) - 8 = 24.
    Output:
    (2 * (7 + 9)) - 8 = 24
    {{/assistant}}
    
    {{#user}}    
    Input: 3 5 8 9
    Intermediate steps:
    8 - 5 = 3 (left 3, 3, 9)
    3 * 9 - 3 = 24
    {{/user}}
    {{#assistant}}
    Draft:
    Because 3 * 9 - 3 = 24, while 3 = 8 - 5. So 3 * 9 - (8 - 5) = 24.
    Output:
    3 * 9 - (8 - 5) = 24
    {{/assistant}}
    
    {{#user}}
    Input: {{input}}
    Intermediate steps:
    {{intermediate_steps}}
    {{/user}}
    {{#assistant}}
    Draft:
    {{/assistant}}
    {{#assistant}}{{gen "draft" temperature=temperature max_tokens=max_tokens stop='Output:\n'}}{{/assistant}}
    {{#assistant}}
    Output:
    {{/assistant}}
    {{#assistant}}{{gen "output" temperature=temperature max_tokens=max_tokens stop='\n'}}{{/assistant}}
        ''', silent=True
)

valid_judgement=["Valid", "Invalid"]

valid_program = guidance('''
    {{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. You are very good at basic arithmetic operations. Use numbers and basic arithmetic operations (+ - * /) to obtain 24 with input numbers. Evaluate if given intermediate step is correct and only use two existing numbers. {{/system}}
    
    {{#user}}    
    Input: 10, 14
    Intermediate step: 10 + 14 = 24
    {{/user}}
    {{#assistant}}
    The intermediate step is valid.
    Judgement:
    Valid
    {{/assistant}}
    
    {{#user}}    
    Input: 4, 4, 10
    Intermediate step: 10 + 5 = 15
    {{/user}}
    {{#assistant}}
    The intermediate step uses non-exists number "5".
    Judgement:
    Invalid
    {{/assistant}}
    
    {{#user}}    
    Input: 4, 4, 8
    Intermediate step: 4 * 8 = 24
    {{/user}}
    {{#assistant}}
    The intermediate step has a wrong calculation.
    Judgement:
    Invalid
    {{/assistant}}
    
    {{#user}}    
    Input: 4, 4, 8
    Intermediate step: 4 * 8 = 32
    {{/user}}
    {{#assistant}}
    The intermediate step is valid.
    Judgement:
    Valid
    {{/assistant}}
    
    {{#user}}    
    Input: 4, 4, 8
    Intermediate step: We can not obtain 24.
    {{/user}}
    {{#assistant}}
    The intermediate step is not a valid math formula.
    Judgement:
    Invalid
    {{/assistant}}
    
    {{#user}}
    Input: {{remaining_numbers}}
    Intermediate step: {{intermediate_step}}
    {{/user}}
    
    {{#assistant}}{{gen "reason" temperature=temperature max_tokens=max_tokens stop="Judgement:\n"}} {{/assistant}}
    {{#assistant}}
    Judgement:
    {{/assistant}}
    {{#assistant}}{{select "judgement" options=valid_judgement}} {{/assistant}}
    '''
)
verifier_program = guidance(
    '''
        {{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. You are very good at basic arithmetic operations. Use numbers and basic arithmetic operations (+ - * /) to obtain 24 with input numbers. Evaluate if given numbers can reach 24 (sure/likely/impossible) {{/system}}
    
    {{#user}}    
    Input: 10, 14
    Draft:
    {{/user}}
    {{#assistant}}
    14 - 10 = 4
    14 * 10 = 140
    10 / 14 = 5/7
    14 / 10 = 1.4
    10 + 14 = 24
    {{/assistant}}
    {{#user}}
    Output:
    {{/user}}
    {{#assistant}}
    sure
    10 + 14 = 24
    {{/assistant}}
    
    {{#user}}    
    Input: 4, 4, 10
    Draft:
    {{/user}}
    {{#assistant}}
    10 - 4 + 4 = 6 + 4 = 10
    4 + 4 + 10 = 8 + 10 = 18
    4 * 4 + 10 = 16 + 10 = 26
    4 * 10 - 4 = 40 - 4 = 36
    (10 - 4) * 4 = 6 * 4 = 24
    {{/assistant}}
    {{#user}}
    Output:
    {{/user}}
    {{#assistant}}
    sure
    (10 - 4) * 4 = 6 * 4 = 24
    {{/assistant}}
    
    {{#user}}    
    Input: 5 15
    Draft:
    {{/user}}
    {{#assistant}}
    5 + 15 = 20
    5 - 15 = -10
    5 * 15 = 75
    5 / 15 = 1/3
    15 - 5 = 10
    15 / 5 = 3
    The input only has two numbers, so I tried all possibility, but no one reached 24.
    {{/assistant}}
    {{#user}}
    Output:
    {{/user}}
    {{#assistant}}
    impossible
    {{/assistant}}
    
    {{#user}}    
    Input: 4, 9, 11
    Draft:
    {{/user}}
    {{#assistant}}
    4 + 9 + 11 = 24
    {{/assistant}}
    {{#user}}
    Output:
    {{/user}}
    {{#assistant}}
    sure
    4 + 9 + 11 = 24
    {{/assistant}}
    
    {{#user}}    
    Input: 1, 5, 20
    Draft:
    {{/user}}
    {{#assistant}}
    1 + 5 + 20 = 26
    1 * 5 + 20 = 25
    20 / 5 + 1 = 5
    1 * (20 - 5) = 15
    1 * (20 + 5) = 25
    1 - 5 + 20 = 16
    5 - 1 + 20 = 24
    {{/assistant}}
    {{#user}}
    Output:
    {{/user}}
    {{#assistant}}
    sure
    5 - 1 + 20 = 24
    {{/assistant}}
    
    {{#user}}    
    Input: 1, 2, 11
    Draft:
    {{/user}}
    {{#assistant}}
    1 * 2 + 11 = 13
    1 + 2 + 11 = 14
    2 * (11 - 1) = 10
    11 * 2 - 1 = 21
    2 / 1 * 11 = 22
    (11 - 1) / 2 = 5
    11 - 1 * 2 = 9
    1 * (2 + 11) = 13
    1 * (11 - 2) = 9
    2 * 11 + 1 = 22
    2 * (11 + 1) = 24
    {{/assistant}}
    {{#user}}
    Output:
    {{/user}}
    {{#assistant}}
    sure
    2 * (11 + 1) = 24
    {{/assistant}}
    
    {{#user}}    
    Input: 5, 7, 8
    Draft:
    {{/user}}
    {{#assistant}}
    5 * 8 - 7 = 33
    5 * 7 - 8 = 27
    5 * 7 + 8 = 43
    5 * (7 + 8) = 75
    5 + 7 + 8 = 12 + 8 = 20
    (8 - 5) * 7 = 3 * 7 = 21
    I cannot obtain 24 now, but numbers are within a reasonable range
    {{/assistant}}
    {{#user}}
    Output:
    {{/user}}
    {{#assistant}}
    likely
    {{/assistant}}
    
    {{#user}}    
    Input: 10, 10, 11
    Draft:
    {{/user}}
    {{#assistant}}
    10 + 10 - 11 = 9
    10 * 11 + 10 = 120
    11 * (10 / 10) = 11
    (11 - 10) + 10 = 11
    10 + 10 + 11 = 31
    (11 - 10) * 10 = 10
    I cannot obtain 24 now, but numbers are within a reasonable range
    {{/assistant}}
    {{#user}}
    Output:
    {{/user}}
    {{#assistant}}
    likely
    {{/assistant}}
    
    
    {{#user}}    
    Input: 10, 10, 10
    Draft:
    {{/user}}
    {{#assistant}}
    10 10 10 are all too big
    {{/assistant}}
    {{#user}}
    Output:
    {{/user}}
    {{#assistant}}
    impossible
    {{/assistant}}
    
    {{#user}}    
    Input: 1, 3, 3
    Draft:
    {{/user}}
    {{#assistant}}
    1 + 3 + 3 = 7
    1 + 3 * 3 = 10
    (3 - 1) * 3 = 6
    1 * 3 * 3 = 9
    (1 + 3) * 3 = 12
    I cannot obtain 24 now, and numbers are not within a reasonable range
    {{/assistant}}
    {{#user}}
    Output:
    {{/user}}
    {{#assistant}}
    impossible
    {{/assistant}}
    
    {{#user}}
    Input: {{remaining_numbers}}
    Draft:
    {{/user}}
    {{#assistant}}{{gen "draft" temperature=temperature max_tokens=max_tokens}} {{/assistant}}
    {{#user}}
    Output:
    {{/user}}
    {{#assistant}}{{select "output" options=valid_output}} {{/assistant}}
    {{#assistant}}{{gen "output_equation" temperature=0.1 max_tokens=100}} {{/assistant}}
    ''', silent=True
)

# Define the guidance program
generate_program = guidance(
    '''
    {{#system}}Suppose you are one of the greatest AI scientists, logicians and mathematicians. You are very good at basic arithmetic operations. Use numbers and basic arithmetic operations (+ - * /) to obtain 24 with input numbers. In each step, You are only allowed to randomly choose arbitrary TWO of the input numbers to obtain a new number using arbitrary one basic arithmetic operation (AVOID duplicating with forbidden steps). Your calculation process must be correct.{{/system}} 
    
    {{#user}}
    Input: 
    4, 9, 10, 13
    Next Step:
    {{/user}}
    {{#assistant}}
    4 * 9 = 36
    {{/assistant}}
    {{#user}}
    Remaining Numbers:
    {{/user}}
    {{#assistant}}
    10, 13, 36
    {{/assistant}}
    
    {{#user}}
    Input: 
    1, 4, 8, 11
    Next Step:
    {{/user}}
    {{#assistant}}
    1 + 11 = 12
    {{/assistant}}
    {{#user}}
    Remaining Numbers:
    {{/user}}
    {{#assistant}}
    6, 8, 10
    {{/assistant}}
    
    {{#user}}
    Input: 
    2, 4, 4, 7
    Next step:
    {{/user}}
    {{#assistant}}
    7 - 2 = 5
    {{/assistant}}
    {{#user}}
    Remaining Numbers:
    {{/user}}
    {{#assistant}}
    4, 4, 5
    {{/assistant}}
    
    {{#user}}
    Input: 
    1, 4, 8, 12
    Next step:
    {{/user}}
    {{#assistant}} 
    12 / 4 = 3
    {{/assistant}}
    {{#user}}
    Remaining Numbers:
    {{/user}}
    {{#assistant}}
    1, 3, 8
    {{/assistant}}
    
    {{#user}}
    Input: 
    10, 12, 22
    Next step:
    {{/user}}
    {{#assistant}}
    10 + 22 = 32
    {{/assistant}}
    {{#user}}
    Remaining Numbers:
    {{/user}}
    {{#assistant}}
    12, 32
    {{/assistant}}
    
    {{#user}}
    Input:
    1, 8, 9, 11 
    Next step:
    {{/user}}
    {{#assistant}}
    9 - 1 = 8
    {{/assistant}}
    {{#user}}
    Remaining Numbers:
    {{/user}}
    {{#assistant}}
    8, 8, 11
    {{/assistant}}
    
    {{#user}}
    Input: 
    {{thoughts}}
    Forbidden Steps:
    {{forbidden_steps}}
    Next step:
    {{/user}}
    {{#assistant}}{{gen "next_step" temperature=temperature max_tokens=max_tokens}} {{/assistant}}
    {{#user}}
    Remaining Numbers:
    {{/user}}
    {{#assistant}}{{gen "remaining_numbers" temperature=0.1 max_tokens=max_tokens}} {{/assistant}}
    
    ''', silent=True)


# Try more times if failed to use OpenAI API
def run(program, MAX_RETRY=5, **kwargs):
    cnt = 0
    myout = {}
    while cnt < MAX_RETRY:
        try:
            myout = program(**kwargs)
            break
        except Exception as e:
            cnt += 1
            continue
    return cnt < MAX_RETRY, myout


def solve(input, pbar):
    records = [input]
    last_step = {}
    f = {}
    forbidden = {}
    forbidden[input] = []
    for i in range(args.trycnt):
        try:
            p = numpy.zeros_like(records, dtype='float64')
            if i < 1 / 2 * args.trycnt:
                if len(records) > 1:
                    p.fill(0.5 / (len(records) - 1))
                    p[0] = 0.5
                else:
                    p[0] = 1.
            else:
                p.fill(1. / len(records))
            tmp = numpy.random.choice(records, p=p)
            success, out = run(generate_program, temperature=1.0, max_tokens=64, thoughts=tmp, forbidden_steps=('\n'.join(forbidden[tmp])) if len(forbidden[tmp]) > 0 else 'No Forbidden Steps\n')
            if success:
                a = out['remaining_numbers'].strip().split('\n')[0].strip()
                if re.search("[^0-9+\-*/.(),=\s]" ,out['next_step'].strip()):
                    continue
                if not re.search("\S",out['next_step'].strip()) or not re.search("\S", out['remaining_numbers'].strip()):
                    continue
                _, judgement = run(valid_program, temperature=0.1, max_tokens=128, remaining_numbers=tmp, intermediate_step=out['next_step'].strip(), valid_judgement=valid_judgement)
                if judgement['judgement'] == 'Invalid':
                    continue
                _, verify_result = run(verifier_program, temperature=0.7, max_tokens=256, remaining_numbers=a, valid_output=valid_output, is_sure=is_sure)
                if is_sure(verify_result['output']):

                    pbar.write(f"{tmp} -- {out['next_step'].strip()} -> {a}")
                    tmp_steps = [verify_result['output_equation'].strip().split('\n')[0].strip()]
                    tmp_steps.append(out['next_step'].strip() + f' (left {a})')
                    while tmp != input:
                        tmp_steps.append(last_step[tmp] + f' (left {tmp})')
                        tmp = f[tmp]
                    tmp_steps.reverse()
                    _, expand_result=run(expand_program, temepratue=0.1, max_tokens=200, input=input, intermediate_steps='\n'.join(tmp_steps))
                    return True, i, expand_result['output']
                elif verify_result['output'] == 'likely':
                    a = a.strip()
                    if a not in records:
                        forbidden[tmp].append(out['next_step'].strip())
                        forbidden[a] = []
                        records.append(a)
                        f[a] = tmp
                        last_step[a] = out['next_step'].strip()
                        pbar.write(f"{tmp} -- {out['next_step'].strip()} -> {a}")
        except Exception as exception:
            pbar.write('Something goes wrong when calling OpenAI API')
            continue

    return False, args.trycnt, ""

if __name__ == "__main__":
    df = pd.read_csv('24.csv')
    puzzles = []
    for i in range(len(df)):
        puzzles.append(df.iloc[i, 1].replace(' ', ', ').strip())

    puzzles = puzzles[900:1000]

    log_results = []
    cnt = args.resume_cor

    info = {'tot': args.resume, 'acc': 0.0, 'Solving': ''}

    pbar = tqdm(puzzles[args.resume:])

    total_try = 0
    for puzzle in pbar:
        this_result = {'puzzle': puzzle}
        info['Solving'] = puzzle
        if info['tot'] > 0:
            info['acc'] = cnt / info['tot']
            info['total_try'] = total_try
        pbar.set_postfix(info, refresh=True)

        info['tot'] = info['tot'] + 1
        for i in range(args.b):
            success, try_cnt, output = solve(puzzle, pbar)

            total_try += try_cnt
            this_result[f'try_cnt_branch_{i}'] = try_cnt
            if success:
                expression = output.strip().split('\n')[-1].lower().replace('answer: ', '').split('=')[0]
                pbar.write(f"PUZZLE:{info['Solving']}\nANSWER:{expression}\nTRY CNT:{try_cnt}")
                numbers = re.findall(r'\d+', expression)
                problem_numbers = re.findall(r'\d+', puzzle)
                if sorted(numbers) != sorted(problem_numbers):
                    pbar.write('INVALID ANSWER')
                    pass
                else:
                    this_result['output'] = expression
                    try:
                        if int(sympy.simplify(expression) == 24):
                            pbar.write('CORRECT!')
                            this_result['correct'] = True
                            cnt += 1
                        else:
                            this_result['correct'] = False
                            pbar.write('WRONG!')
                        break
                    except Exception as e:
                        pbar.write(e)
                        pbar.write('WRONG!')
                        break

        if 'output' not in this_result:
            this_result['output'] = 'NO OUTPUT'
            this_result['correct'] = False

        with open(f'game24_b={args.b}.log', 'a') as f_write:
            f_write.write(json.dumps(this_result) + '\n')
