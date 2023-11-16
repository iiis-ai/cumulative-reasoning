# Cumulative Reasoning with Large Language Models


[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/cumulative-reasoning-with-large-language/math-word-problem-solving-on-math)](https://paperswithcode.com/sota/math-word-problem-solving-on-math?p=cumulative-reasoning-with-large-language)
[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/2308.04371)
![Python 3.10](https://img.shields.io/badge/python-3.10-green.svg)

## Introduction

Official implementation of paper "Cumulative Reasoning with Large Language Models" (https://arxiv.org/abs/2308.04371).

- **Achieving 98% accuracy for the Game of 24 (+24% compared to Tree-of-Thoughts)!** 

- **Achieving 58% accuracy on the MATH dataset without code environment using GPT-4-0314 (+4.2% compared to PHP)!**

- **Achieving 43% relative improvement on the hardest Level 5 MATH problems (22.4% to 32.1%)!**

- **Achieving 72.2% accuracy on the MATH dataset without code environment using GPT-4-1106-preview (+20.2% compared to PAL (PoT))!**

## Installation

`pip install -r requirements.txt`

For more usage help, please refer to the README.md in each subdirectory.

## CR Agent: Solving MATH Problems with Code Environment

please see `/CR-Agent` folder for the output log and prompts on MATH dataset, we will update the code soon (based on ToRA).

## Acknowledgement

This repo is mainly based on [Guidance](https://github.com/microsoft/guidance), [HuggingFace](https://huggingface.co/) and [Tree of Thoughts](https://github.com/princeton-nlp/tree-of-thought-llm). Thanks for their wonderful work!

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
