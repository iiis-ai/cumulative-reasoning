# Cumulative Reasoning with Large Language Models


[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/cumulative-reasoning-with-large-language/math-word-problem-solving-on-math)](https://paperswithcode.com/sota/math-word-problem-solving-on-math?p=cumulative-reasoning-with-large-language)
[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/2308.04371)
![Python 3.10](https://img.shields.io/badge/python-3.10-green.svg)

## Introduction

Official implementation of paper "Cumulative Reasoning with Large Language Models" (https://arxiv.org/abs/2308.04371).

- **Achieving 98% accuracy for the Game of 24 (+24% compared to Tree-of-Thoughts)!** 

- **Achieving 58% accuracy on the MATH dataset without code environment using GPT-4-0314 (+4.2% compared to PHP)!**

- **Achieving 43% relative improvement on the hardest Level 5 MATH problems (22.4% to 32.1%)!**

- **Achieving 72.2% accuracy on the MATH dataset with code environment using GPT-4-1106-preview (+20.2% compared to PAL (PoT) )!**

- **Focusing on Level 5 MATH problems, the CR Agent v0.1 showed a remarkable 66.8% improvement over PAL!**

## Installation

`pip install -r requirements.txt`

For more usage help, please refer to the README.md in each subdirectory.


## CR Agent: Solving MATH Problems with Code Environment

please see the `./CR-Agent` folder for the output log and prompts on the MATH dataset, we have released the code for CR Agent v0.1 (a minimalist implementation based on ToRA).

### Experimental Results

In this section, we employed GPT-4-Turbo (GPT-4-1106-preview) with a Python code environment, devoid of additional tools like external memory and retrieval systems. The experiment involved a minimalist setup where only one reasoning context session was utilized. This session was managed by simply accumulating and concatenating the context string, and the entire process was executed using a single LLM without the assistance of a verifier LLM. Notably, the implementation was carried out purely using Python strings, without leveraging any specialized frameworks such as Langchain or guidance.

The outcomes of this experimental setup revealed noteworthy results:
- PAL (Program-Aided Language models): Achieved an accuracy of 52%.
- ToRA (Tool-Integrated Reasoning Agent): Demonstrated a higher accuracy of 60.8%.
- CR Agent (Cumulative Reasoning Agent) v0.1: Significantly outperformed the aforementioned methods with an impressive accuracy of **72.2%**.
- Specifically focusing on **Level 5** problems, the CR Agent showed a remarkable **66.8%** improvement over PAL and a **12.7%** relative improvement over ToRA.

#### Category-wise Scores

| Method    | Algebra | Counting & Probability | Geometry | Intermediate Algebra | Number Theory | Prealgebra | Precalculus |
|-----------|---------|------------------------|----------|----------------------|---------------|------------|-------------|
| PAL (PoT) | 65.3    | 57.9                   | 31.7     | 30.9                 | 66.1          | 73.2       | 23.2        |
| ToRA      | 71.8    | 68.4                   | 48.8     | 49.5                 | 66.1          | 67.1       | 44.6        |
| CR Agent  | **86.3**| **71.1**               | **53.7** | **51.5**             | **88.7**      | **86.6**   | **51.8**    |

#### Difficulty Level Scores

| Method    | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 |
|-----------|---------|---------|---------|---------|---------|
| PAL (PoT) | 88.4    | 65.6    | 60.0    | 45.3    | 31.3    |
| ToRA      | 74.4    | 75.6    | 69.5    | 53.9    | 46.3    |
| CR Agent  | **90.7**| **90.0**| **81.9**| **66.4**| **52.2**|

The asterisks highlight the best-performing method in each category and difficulty level, clearly indicating the superiority of the CR Agent in this experimental setup.

These tables provide a comprehensive view of the performance of each method across various categories and difficulty levels in the MATH dataset. The CR Agent shows marked improvements in most categories and levels, illustrating its robustness and effectiveness in solving complex mathematical problems, even within the constraints of a simplified experimental setup.



## CR Agent Assistant v0.1 based on `Meta Prompting`

see `./CR-Agent-Assistant/cr-agent-assistant-v0.1.md` for a minimalist implementation based on OpenAI Assistant API.

See https://chat.openai.com/g/g-L3a4ZCIHx-cr-agent-v0-1 for an online demo.


**Meta Prompting (General Definition)**: [Meta Prompting](https://github.com/meta-prompting/meta-prompting) is a prompting technique inspired by type theory, emphasizing the structure and syntax of examples rather than their detailed content. It's an approach where the focus is on presenting the outline or framework of a problem or topic, offering a scaffold that can be filled with specific details as needed. This technique is particularly useful in situations where understanding the form and pattern of a problem or solution is more crucial than the specific content. 


## Acknowledgement

This repo is mainly based on [Guidance](https://github.com/microsoft/guidance), [HuggingFace](https://huggingface.co/), [Tree of Thoughts](https://github.com/princeton-nlp/tree-of-thought-llm) and [ToRA](https://github.com/microsoft/ToRA). Thanks for their wonderful work!

## Citations
Please cite the paper and star this repo if you use Cumulative Reasoning (CR) and find it interesting/useful, thanks! Feel free to contact zhangyif21@tsinghua.edu.cn | yangjq21@mails.tsinghua.edu.cn or open an issue if you have any questions.

```bibtex
@article{zhang2023cumulative,
  title={Cumulative Reasoning With Large Language Models},
  author={Zhang, Yifan and Yang, Jingqin and Yuan, Yang and Yao, Andrew Chi-Chih},
  journal={arXiv preprint arXiv:2308.04371},
  year={2023}
}
```
