# Cumulative Reasoning on Game of 24

## Setup OpenAI API

Please set `os.environ["OPENAI_API_KEY"]="YOUR_API_KEY"` in `game24-openai.py`

Make sure that your device is able to connect to [OpenAI API](https://platform.openai.com/docs/api-reference)

## Run paper experiment

`python game24-openai.py` for b=1 or `python game24-openai.py --b=2` for b=2

## Parameters

`--trycnt`: the limitation of states visited by CR. Default is set to be 50

`--model`: `gpt-3.5-turbo` or `gpt-4`. Default is set to be `gpt-4`. You can also choose some past version, such as `gpt-4-0314`.

`--b` : number of branches.
