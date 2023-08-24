# Cumulative Reasoning on MATH

## Setup OpenAI API

Please set `os.environ["OPENAI_API_KEY"]="YOUR_API_KEY"` in all python scripts.

Make sure that your device is able to connect to [OpenAI API](https://platform.openai.com/docs/api-reference). 

Make sure you are using guidance of version 0.0.64 .

## Run paper experiments

You can use any openai model (`gpt-3.5-turbo`, `gpt-4`, etc.) as `YOUR_MODEL`.
- Complex-CoT:
`python math-complex-cot.py --model=YOUR_MODEL`
- Complex-CoT + PHP:
`python math-php.py --model=YOUR_MODEL`
- CR(4-shot)
`python math-cr-4shot.py --model=YOUR_MODEL`
- CR(4-shot) + PHP
`python math-cr-4shot-php.py --model=YOUR_MODEL`

## Experiment log
We provide our paper experiment logs in `results` directory. 