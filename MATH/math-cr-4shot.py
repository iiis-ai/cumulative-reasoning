# MATH with Cumulative Reasoning (4-shot)

import guidance
import json
import time
from tqdm import tqdm
import argparse
import os
import re
import ast
import sympy

# os.environ["OPENAI_API_KEY"] = 'sk-...'

TRY_CNT = 16


def get_parser():
    parser = argparse.ArgumentParser(description="Cumulative Reasoning")
    parser.add_argument('--temperature', type=float, default=0.0, help='temperature')
    parser.add_argument('--majoritycnt', type=int, choices=range(1, 101), default=1,
                        help='numbers of majority voting times')
    parser.add_argument('--hintcnt', type=int, choices=range(0, 101), default=2, help='numbers of hints to generate')
    parser.add_argument('--questioncnt', type=int, choices=range(0, 101), default=8,
                        help='numbers of questions to generate')
    parser.add_argument('--questiontrycnt', type=int, choices=range(0, 101), default=4,
                        help='numbers of tries to generate questions')
    parser.add_argument('--answertrycnt', type=int, choices=range(0, 101), default=4, help='numbers of tries to answer')
    parser.add_argument('--verbose', type=ast.literal_eval, default=True, help='verbose mode')
    parser.add_argument('--model', type=str, default='gpt-3.5-turbo-16k-0613', help='model to use')
    parser.add_argument('--withcode', type=ast.literal_eval, default=False, help='whether to use code to verify answers')
    parser.add_argument('--dataset', type=str, default='data/test.jsonl', help='dataset to use')
    parser.add_argument('--problem_level_lower_bound', type=int, default=1,
                        help='lower bound of problem level [lower_bound, upper_bound]')
    parser.add_argument('--problem_level_upper_bound', type=int, default=5,
                        help='upper bound of problem level [lower_bound, upper_bound]')
    # parser.add_argument('--problem_numbers', type=int, default=500, help='problem numbers to be evaluated')
    parser.add_argument('--problem_interval_begin', type=int, default=1, help='problem interval begin [begin, end]')
    parser.add_argument('--problem_interval_end', type=int, default=500, help='problem interval end [begin, end]')
    parser.add_argument('--inverse_problem_order', type=ast.literal_eval, default=True, help='whether to inverse problem order')
    return parser


parser = get_parser()
args = parser.parse_args()

gpt4 = guidance.llms.OpenAI("gpt-4")
guidance.llm = guidance.llms.OpenAI(args.model, caching=True)

def try_wrapper(func):
    def inner(*args, **kwargs):
        try_cnt = 0
        while try_cnt < TRY_CNT:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"func() failed, try again... (No. {try_cnt + 1}). Error: {e}")
                try_cnt += 1
                if ('You cannot set text to an empty string. We interpret empty strings as None' in str(e)):
                    raise e
                time.sleep(min(1024, 2 ** (try_cnt / 2)))
                continue

    return inner


def get_time_str(trycnt=0):
    return "2023-06-01-12-00-" + str(trycnt).zfill(2)
    return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())


examples = [
]

example_prompt_string = '''
{{#user}}---
## **Question**: SOME QUESTION

### Hints:
Let's think step by step.
{{/user}}
{{#assistant}}
1. **Hint 1**: 
2. **Hint 2**: 
3. **Hint 3**: 
{{/assistant}}
{{#user}}
### Intermediate Steps:
{{/user}}
{{#assistant}}
Let's think step by step.
1. **Question 1**: 
- **Answer 1**: 
2. **Question 2**: 
- **Answer 2**: 
3. **Question 3**: 
- **Answer 3**: 
4. **Question 4**: 
- **Answer 4**: 
{{/assistant}}
{{#user}}
### Final Solution:
{{/user}}
{{#assistant}}
Let's think step by step.

{{/assistant}}
{{#user}}
### Final Answer:
{{/user}}
{{#assistant}}

{{/assistant}}
'''

# Define the guidance program generate hints
program = guidance(
"""
{{#system}}
YOU ARE one of the GREATEST mathematicians, logicians, programmers, and AI scientists. You are intelligent and rational. You are prudent and cautious. Your mastery over Arithmetic, Combinatorics, Number Theory, Probability Theory, Algebra, Analysis, and Geometry is unparalleled. You THINK NATURAL, BROAD AND DEEP. Let's think step by step.
YOU will be given a mathematical question Q, and you need to generate intermediate questions to approach the answer of the given question Q. Before you begin to solve the question, you are asked to generate at most two helpful hints for yourself. In each turn, you must generate a new intermediate question and answer the question by yourself.
Prioritize generating foundational hints that are useful for solving the problem. Prioritize generating foundational questions that are useful for solving the problem. We will solve these simpler components later, and then leverage these intermediate results to deduce the final solution.
{{/system}}
    
{{#user}}---
## **Question**: Kevin Kangaroo begins hopping on a number line at 0. He wants to get to 1, but he can hop only $\\frac{1}{3}$ of the distance. Each hop tires him out so that he continues to hop $\\frac{1}{3}$ of the remaining distance. How far has he hopped after five hops? Express your answer as a common fraction.

### Hints:
Let's think step by step.
{{/user}}
{{#assistant}}
1. **Hint 1**: Recognize the problem as a geometric series with a given first term and common ratio.
2. **Hint 2**: Remember that the sum of a finite geometric series is given by: $S = \\frac{a(1-r^n)}{1-r}$, where $a$ is the first term, $r$ is the common ratio, and $n$ is the number of terms.
{{/assistant}}
{{#user}}
### Intermediate Steps:
{{/user}}
{{#assistant}}
Let's think step by step.
1. **Question 1**: What fraction of the distance does Kevin cover in his first hop?
- **Answer 1**: Kevin covers $\\frac{1}{3}$ of the distance in his first hop.
2. **Question 2**: What fraction of the remaining distance does Kevin cover in his second hop?
- **Answer 2**: Kevin covers $\\frac{1}{3}$ of the remaining distance, which is $\\frac{2}{3} \\times \\frac{1}{3}$.
3. **Question 3**: How far has Kevin hopped after the third hop?
- **Answer 3**: Kevin Kevin has hopped $\\frac{1}{3} + \\frac{2}{3} \\times \\frac{1}{3} + (\\frac{2}{3})^2 \\times \\frac{1}{3}$ after the third hop.
4. **Question 4**: Express the distance Kevin hops on his kkth hop in terms of $k$.
- **Answer 4**: Kevin hops forward $(\\frac{2}{3})^{k-1}(\\frac{1}{3})$ on his $k$th hop.
5. **Question 5**: Using the formula for the sum of a finite geometric series, how far has Kevin hopped after five hops?
- **Answer 5**: Kevin has hopped $\\frac{1}{3}(\\frac{1-(\\frac{2}{3})^5}{1-\\frac{2}{3}})$ after five hops.
{{/assistant}}
{{#user}}
### Final Solution:
{{/user}}
{{#assistant}}
Let's think step by step.
The total distance Kevin has hopped after five hops is given by the sum of a finite geometric series with first term $\\frac{1}{3}$, common ratio $\\frac{2}{3}$, and five terms. Thus, Kevin has hopped $\\frac{\\frac{1}{3}(1-(\\frac{2}{3})^5)}{1-\\frac{2}{3}} = \\boxed{\\frac{211}{243}}$.
{{/assistant}}
{{#user}}
### Final Answer:
{{/user}}
{{#assistant}}
\\frac{211}{243}
{{/assistant}}

{{#user}}---
## **Question**: What is the area of the region defined by the equation $x^2+y^2 - 7 = 4y-14x+3$?

### Hints:
Let's think step by step.
{{/user}}
{{#assistant}}
1. **Hint 1**: Rearrange the equation to group terms and then try completing the square.
2. **Hint 2**: Identify the center and radius of the circle.
3. **Hint 3**: Use the formula for the area of a circle to find the required area.
{{/assistant}}
{{#user}}
### Intermediate Steps:
{{/user}}
{{#assistant}}
Let's think step by step.
1. **Question 1**: Is the equation $x^2+y^2 - 7 = 4y-14x+3$ representative of a circle?
- **Answer 1**: Yes, the equation can be rewritten as $(x+7)^2 + (y-2)^2 = 63$, which is the standard form of a circle's equation.
2. **Question 2**: Given that the radius squared of the circle is 63, what is the actual radius?
- **Answer 2**: The radius is $\\sqrt{63}$.
3. **Question 3**: What is the area of a circle with radius $\\sqrt{63}$?
- **Answer 3**: The area is $63\\pi$.
{{/assistant}}
{{#user}}
### Final Solution:
{{/user}}
{{#assistant}}
Let's think step by step.
The region defined by the equation $x^2+y^2 - 7 = 4y-14x+3$ is a circle with center (-7, 2) and radius $\\sqrt{63}$. The area of this region is $\\boxed{63\\pi}$.
{{/assistant}}
{{#user}}
### Final Answer:
{{/user}}
{{#assistant}}
63\\pi
{{/assistant}}

{{#user}}---
## **Question**: If $x^2+y^2=1$, what is the largest possible value of $|x|+|y|$?

### Hints:
Let's think step by step.
{{/user}}
{{#assistant}}
1. **Hint 1**: The equation $x^2 + y^2 = 1$ represents a circle with radius 1 centered at the origin.
2. **Hint 2**: $|x|+|y|$ represents the sum of the absolute values of the x and y coordinates of a point on the circle. Consider points in different quadrants.
3. **Hint 3**: The maximum value for $|x|+|y|$ will occur when the point is on a line with a slope of -1 or 1 passing through the origin. This is because any deviation from this line will result in a decrease in the sum $|x|+|y|$.
{{/assistant}}
{{#user}}
### Intermediate Steps:
{{/user}}
{{#assistant}}
Let's think step by step.
1. **Question 1**: What is the equation of the line passing through the origin with a slope of 1?
- **Answer 1**: The equation is $y = x$.
2. **Question 2**:  Where does the line $y = x$ intersect the circle $x^2 + y^2 = 1$?
- **Answer 2**: Substituting for $y$ in the circle's equation from the line equation, we get $x^2 + x^2=1$ which gives $2 x^2=1$. Thus, $x=\\frac{\sqrt{2}}{2}$. Therefore, the point of intersection is $\\left(\\frac{\\sqrt{2}}{2}, \\frac{\\sqrt{2}}{2}\\right)$.
3. **Question 3**: Using the point from the second answer, what is the value of $|x|+|y|$?
- **Answer 3**: The value is $\\sqrt{2}$.
{{/assistant}}
{{#user}}
### Final Solution:
{{/user}}
{{#assistant}}
Let's think step by step.
For the equation $x^2 + y^2 = 1$, the largest possible value of $|x|+|y|$ is $\\boxed{\\sqrt{2}}$.
{{/assistant}}
{{#user}}
### Final Answer:
{{/user}}
{{#assistant}}
\\sqrt{2}
{{/assistant}}

{{#user}}---
## **Question**: If $f(x)=\frac{ax+b}{cx+d}, abcd\not=0$ and $f(f(x))=x$ for all $x$ in the domain of $f$, what is the value of $a+d$?

### Hints:
Let's think step by step.
{{/user}}
{{#assistant}}
1. **Hint 1**: Consider the fact that $f(f(x)) = x$ implies that the function $f(x)$ is its own inverse. Therefore, its graph is symmetrical about the line $y = x$.
2. **Hint 2**: With the given rational function form, there will be two asymptotes for the function. Try to determine their equations.
3. **Hint 3**: Think about the intersection of the asymptotes. In order for $f(x)$ to be its own inverse, where must this intersection lie on the coordinate plane?
{{/assistant}}
{{#user}}
### Intermediate Steps:
{{/user}}
{{#assistant}}
Let's think step by step.
1. **Question 1**: What does it mean for a function to be its own inverse and how does it relate to the line $y = x$?
- **Answer 1**: If a function is its own inverse, it means that applying the function twice will yield the original input. This property translates to the graph of the function being symmetric about the line $y = x$, as any point $(a, b)$ on the graph of the function would correspond to a point $(b, a)$ on the graph of its inverse.
2. **Question 2**: What are the asymptotes for the function $f(x) = \\frac{ax+b}{cx+d}$?
- **Answer 2**: The vertical asymptote is given by the values of $x$ for which the denominator is zero, i.e., $cx + d = 0 \\Rightarrow x = -\\frac{d}{c}$. The horizontal asymptote is $y = \\frac{a}{c}$.
3. **Question 3**: For the function to be its own inverse, where must the intersection of the asymptotes lie?
- **Answer 3**: In order for $f(x)$ to be its own inverse, the intersection of its asymptotes must lie on the line $y = x$. This ensures that the function and its inverse (which is itself in this case) reflect onto one another across the line $y = x$.
4. **Question 4**: Based on the intersection of the asymptotes lying on $y = x$, what can we deduce about the values of $a$, $c$, and $d$?
- **Answer 4**: -d = a. Therefore, a + d = 0.
{{/assistant}}
{{#user}}
### Final Solution:
{{/user}}
{{#assistant}}
Let's think step by step.
Given $f(x)=\\frac{ax+b}{cx+d}$, and using the fact that the function is its own inverse, we deduced that the graph of $f(x)$ must be symmetric about the line $y = x$. Analyzing the asymptotes of the function, we found the intersection of the asymptotes must lie on the line $y = x$. This led us to the conclusion that $a = -d$, giving $a + d = \\boxed{0}$.
{{/assistant}}
{{#user}}
### Final Answer:
{{/user}}
{{#assistant}}
0
{{/assistant}}

{{#user}}---
## **Question**: {{question_content}}

### Hints:
Let's think step by step.
{{/user}}
{{#assistant}}{{gen "hints" temperature=hint_temperature max_tokens=400}}{{/assistant}}
{{#user}}
### Intermediate Steps:
{{/user}}
{{#assistant}}{{gen "intermediate_steps" temperature=intermediate_temperature max_tokens=2000}}{{/assistant}}
{{#user}}
### Recall the Question:
**Question**: {{question_content}}

### Final Solution:
{{/user}}
{{#assistant}}{{gen "final_solution" temperature=sol_temperature max_tokens=2000}}{{/assistant}}
{{#user}}
### Final Answer:
{{/user}}
{{#assistant}}{{gen "final_answer" temperature=ans_temperature max_tokens=400}}{{/assistant}}
""")


# we can pre-define valid option sets
valid_correctness = ["Correct", "Wrong", "Unknown"]

# Define the guidance program judger, define the {{final_answer}} are correct,
#   given the ground truth {{ground_truth_answer}}
judger = guidance(
    """
    {{#system}}YOU ARE one of the GREATEST mathematicians, logicians, programmers, and AI scientists. You are intelligent and rational. You are prudent and cautious. Your mastery over Arithmetic, Combinatorics, Number Theory, Probability Theory, Algebra, Analysis, and Geometry is unparalleled. You THINK NATURAL, BROAD AND DEEP. Let's think step by step. {{/system}}
    {{#system}}Your job is to judge whether the "final_answer" is correct based on "ground_truth_answer", do not be strict on the format, but check the content. Notice that unsolved half results are not Correct. {{/system}}
    {{#system}}Problem Subject: "{{question_subject}}", Problem Content: "{{question_content}}" {{/system}}
    {{#system}}Is the final_answer correct, given the ground truth answer? Reply with Correct, Wrong or Unknown. 
    "final_answer": "{{final_answer}}", "ground_truth_answer": "{{ground_truth_answer}}"{{/system}}
    {{#assistant}}{{select "correctness" options=valid_correctness}}{{/assistant}}
    """, llm=gpt4, valid_correctness=valid_correctness)


def main():
    # Load the data from the JSONL file
    data = []
    with open(args.dataset, 'r', encoding='utf-8') as f:
        cnt = 0
        for line in f:
            if (json.loads(line)['level'] < args.problem_level_lower_bound): continue
            if (json.loads(line)['level'] > args.problem_level_upper_bound): continue
            data.append(json.loads(line))
            cnt += 1
            # if (cnt == args.problem_numbers):
            #     break
    data = data[args.problem_interval_begin-1:args.problem_interval_end]
    print(len(data))
    if args.inverse_problem_order == True:
        data = data[::-1]

    t = time.localtime()

    # extract 'test' from args.dataset in format 'data/test.jsonl'
    dataset_name = args.dataset.split('/')[1].split('.')[0]
    # change huggyllama/llama-13b to huggyllama-llama-13b
    model_name = args.model.replace('/', '-')
    logfilename = 'results/results-math-cr-4shot-openai--' + model_name + '--' + dataset_name + '--k_' + str(
        args.majoritycnt) + '--' + time.strftime("%Y-%m-%d-%H-%M-%S", t) + '.jsonl'
    with open(logfilename, 'w') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", t) + '\tv1.0.0 \n')  # write each result as a new line
        f.write("Model: " + args.model + "\n")
        f.write("Temperature: " + str(args.temperature) + "\n")
        f.write("Majority Cnt: " + str(args.majoritycnt) + "\n")
        f.write("Hint Cnt: " + str(args.hintcnt) + "\n")
        f.write("Question Cnt: " + str(args.questioncnt) + "\n")
        f.write("Dataset: MATH - " + args.dataset + "\n")
        f.write(
            f"Problem Level Interval: [{str(args.problem_level_lower_bound)}, {str(args.problem_level_upper_bound)}]\n")
        # f.write(f"Problem Numbers: First {str(args.problem_numbers)} Problems\n")
        f.write(f"Problem Interval: [{str(args.problem_interval_begin)}, {str(args.problem_interval_end)}]\n")
        f.write(f"Inverse Problem Order: {str(args.inverse_problem_order)}\n")
        f.write("--------------------------------\n")
    # Initialize counter for correct answers
    correct_answers = 0
    cnt = 0
    total_cnt = len(data)

    # Iterate over the data from the JSON file and call the solve function
    for example in tqdm(data, desc="Evaluating", unit="example"):
        cnt += 1

        print("-------------------------\n### Example ID: ", example["unique_id"], "\t ( ", cnt, "/", total_cnt, " )")
        print("Problem Level: ", example["level"])
        print("[Problem Subject]: ", example["subject"])
        print("[Problem Content]: ", example["problem"])
        # new Q for every example


        try_cnt = 0
        padding_string = ""
        while True:
            try_cnt += 1
            try:
                out = try_wrapper(program)(question_content=example['problem'] + padding_string, question_subject=example['subject'], hint_temperature=args.temperature, intermediate_temperature=args.temperature,
                                           sol_temperature=args.temperature, ans_temperature=args.temperature)

                judgement = try_wrapper(judger)(question_content=example['problem'][:], question_subject=example['subject'], final_answer=out['final_answer'], ground_truth_answer=example['answer'])

                print("[Hint]: ", out['hints'])
                print("[Intermediate Steps]: ", out['intermediate_steps'])
                print("[Final Solution]: ", out['final_solution'])
                print("[Final Answer]: ", out['final_answer'])
                # print("[Ground Truth Solution]: ", example["solution"])
                print("[Ground Truth Answer]: ", example["answer"])
                print("[Correctness]: ", judgement["correctness"])
                padding_string = ""
                break
            except Exception as e:
                print("Main Exception: ", e)
                if ('You cannot set text to an empty string. We interpret empty strings as None' in str(e)):
                    padding_string += "\nYou cannot set text to an empty string."
                time.sleep(min(1024, 2 ** (try_cnt / 2)))
                continue

        correct_answers += (judgement['correctness'] == 'Correct')
        # Calculate and print the running accuracy
        accuracy = correct_answers / cnt

        print("[Running Average Accuracy]: ", accuracy)

        result = {
            "accuracy": accuracy,
            "example_id": example["unique_id"],
            "level": example["level"],
            "problem_subject": example["subject"],
            "problem_content": example["problem"],
            "correctness": judgement["correctness"],
            "hints": out['hints'],
            "generated_simple_questions_and_answers": out['intermediate_steps'],
            "final_solution": out['final_solution'],
            "final_answer": out['final_answer'],
            "ground_truth_solution": example["solution"],
            "ground_truth_answer": example["answer"],
        }

        # Write the result to a JSON file, note that we open the file in append mode ('a')
        with open(logfilename, 'a') as f:
            f.write(json.dumps(result) + '\n')  # write each result as a new line


if __name__ == "__main__":
    main()
