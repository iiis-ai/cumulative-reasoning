# Cumulative Reasoning on FOLIO dataset

## Installation

```
pip install -r requirements.txt
```

**You must use 0.0.61 version of guidance while testing LlaMa models.**

## Setup OpenAI API

Please set `os.environ["OPENAI_API_KEY"]="YOUR_API_KEY"` in `*-openai.py`

Make sure that your device is able to connect to [OpenAI API](https://platform.openai.com/docs/api-reference)

## Example usage

```python
python folio-direct-openai.py
```

```python
python folio-cot-openai.py
```

```python
python folio-cr-openai.py
```
