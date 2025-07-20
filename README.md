# Cumulative Reasoning with Large Language Models

<div align="center">

[![TMLR](https://img.shields.io/badge/TMLR-Published-blue)]()
[![arXiv](https://img.shields.io/badge/arXiv-2308.04371-b31b1b.svg)](https://arxiv.org/abs/2308.04371)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Website](https://img.shields.io/badge/Project-Website-green)](https://cumulative-reasoning.github.io)

</div>

This is the official implementation for the paper **"Cumulative Reasoning with Large Language Models"**, published in Transactions on Machine Learning Research (TMLR).

Cumulative Reasoning (CR) is a structured framework that enhances LLM problem-solving by emulating human-like iterative and cumulative thought processes. CR orchestrates LLMs in three distinct roles—**Proposer**, **Verifier(s)**, and **Reporter**—to systematically decompose tasks, validate intermediate steps, and compose them into a final solution.

---

## 🚀 Key Achievements

CR demonstrates state-of-the-art performance across multiple complex reasoning benchmarks:

-   **Game of 24**: Achieves **98% accuracy**, a **+24%** absolute improvement over Tree-of-Thoughts (ToT).
-   **MATH Dataset (No Code Interpreter)**: Attains **58% accuracy** with GPT-4, outperforming Progressive-Hint Prompting (PHP) by **+4.2%**.
-   **MATH Dataset (Hardest Problems)**: Shows a **43% relative improvement** on Level 5 problems (from 22.4% to 32.1%).
-   **MATH Dataset (with Code Interpreter)**: The CR Agent reaches **72.2% accuracy**, surpassing PAL (PoT) by **+20.2%**. On Level 5 problems, this represents a **66.8% relative improvement** over PAL.

---

## 🔧 Installation

To get started, clone the repository and set up the environment:

```bash
# Clone the repository
git clone [https://github.com/iiis-ai/cumulative-reasoning.git](https://github.com/iiis-ai/cumulative-reasoning.git)
cd cumulative-reasoning

# Create and activate a conda environment
conda create -n cr python=3.10
conda activate cr

# Install the required packages
pip install -r requirements.txt
```

For detailed instructions on specific experiments, please refer to the `README.md` files within each subdirectory.

---

## 🤖 CR Agent: Solving MATH with a Code Environment

The `CR-Agent` directory contains our implementation for solving the MATH dataset using a code interpreter. This agent demonstrates how CR can be integrated with external tools for robust, semi-symbolic reasoning.

### Experimental Results

Our CR Agent, using `GPT-4-1106-preview`, significantly outperforms previous methods. The agent uses a minimalist setup, accumulating context as a simple string without complex frameworks.

#### Performance on MATH by Category

| Method | Algebra | Counting & Prob. | Geometry | Interm. Algebra | Num. Theory | Prealgebra | Precalculus | **Overall** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| PAL (PoT) | 65.3 | 57.9 | 31.7 | 30.9 | 66.1 | 73.2 | 23.2 | 52.0 |
| ToRA | 71.8 | 68.4 | 48.8 | 49.5 | 66.1 | 67.1 | 44.6 | 60.8 |
| **CR Agent** | **86.3** | **71.1** | **53.7** | **51.5** | **88.7** | **86.6** | **51.8** | **72.2** |

#### Performance on MATH by Difficulty

| Method | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| PAL (PoT) | 88.4 | 65.6 | 60.0 | 45.3 | 31.3 |
| ToRA | 74.4 | 75.6 | 69.5 | 53.9 | 46.3 |
| **CR Agent** | **90.7** | **90.0** | **81.9** | **66.4** | **52.2**|

---

## ✨ CR Agent Assistant & Meta Prompting

We also explore a simplified implementation of the CR Agent using the OpenAI Assistants API, guided by the principles of **Meta Prompting**.

-   **Demo**: Try the [**CR Agent v0.1 on the GPT Store**](https://chat.openai.com/g/g-L3a4ZCIHx-cr-agent-v0-1).
-   **Implementation**: See the minimalist prompt structure in `./CR-Agent-Assistant/cr-agent-assistant-v0.1.md`.

> **Meta Prompting** is a technique that emphasizes the structure and syntax of prompts, providing a scaffold for the LLM to generate complex, structured outputs. Learn more at the [meta-prompting repository](https://github.com/meta-prompting/meta-prompting).

---

## 🎮 Revisiting Game of 24

Using Meta Prompting, we created an agent that writes a Python program to solve all Game of 24 puzzles in a single pass, achieving **100% accuracy** at a speed of **0.08s per sample**. See the [meta-prompting repo](https://github.com/meta-prompting/meta-prompting) for details.

---

## 🙏 Acknowledgements

This work builds upon the excellent research and open-source contributions from the teams behind [Guidance](https://github.com/microsoft/guidance), [Hugging Face](https://huggingface.co/), [Tree of Thoughts](https://github.com/princeton-nlp/tree-of-thought-llm), and [ToRA](https://github.com/microsoft/ToRA). We thank them for their invaluable work.

---

## 📜 Citation

If you find Cumulative Reasoning useful in your research, please cite our paper and star this repository. Thank you!

For questions, please feel free to email `yifanzhangresearch@gmail.com` or open a GitHub issue.

```bibtex
@article{zhang2023cumulative,
  title={Cumulative Reasoning With Large Language Models},
  author={Zhang, Yifan and Yang, Jingqin and Yuan, Yang and Yao, Andrew Chi-Chih},
  journal={Transactions on Machine Learning Research; arXiv preprint arXiv:2308.04371},
  year={2023}
}
```
