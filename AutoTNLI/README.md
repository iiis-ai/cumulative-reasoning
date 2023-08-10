# Cumulative Reasoning on AutoTNLI

## Requirement

Download AutoTNLI Dataset from [HuggingFace](https://huggingface.co/datasets/metaeval/autotnli)

**You must use 0.0.61 version of guidance while testing LlaMa models.**

## Run paper experiment

### Direct
`python autotnli-direct.py --model=PATH/TO/YOUR/LLAMA --dataset=PATH/TO/AUTOTNLI`

### CoT(-SC)

`python autotnli-cot.py --sc_cnt=(1 or 16) --max_tokens=150 --temperature=0.1 --model=PATH/TO/YOUR/LLAMA --dataset=PATH/TO/AUTOTNLI`

Here `sc_cnt` means the k of majority vote, so `sc_cnt=1` means that majority vote is disabled .

### CR

`python autotnli-cr.py --trycnt=4 --max_tokens=150 --temperature=0.1 --model=PATH/TO/YOUR/LLAMA --dataset=PATH/TO/AUTOTNLI`

## Parameter Explanations

`--trycnt`: number of immediate steps in CR. 

`--sc_cnt`: k of majority vote. Set `--sc_cnt=1` to disable majority vote.
