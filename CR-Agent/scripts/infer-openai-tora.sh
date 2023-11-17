set -ex

MODEL_NAME_OR_PATH="gpt-3.5-turbo-1106"

# DATA_LIST = ['math', 'math-minival', 'gsm8k', 'gsm-hard', 'svamp', 'tabmwp', 'asdiv', 'mawps']

DATA="math-minival"

SPLIT="test"
PROMPT_TYPE="pal"
NUM_TEST_SAMPLE=-1

CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 TOKENIZERS_PARALLELISM=false \
python -m infer.inference \
--model_name_or_path ${MODEL_NAME_OR_PATH} \
--data ${DATA} \
--split ${SPLIT} \
--prompt_type ${PROMPT_TYPE} \
--max_func_call 16 \
--num_test_sample ${NUM_TEST_SAMPLE} \
--seed 0 \
--temperature 0 \
--n_sampling 1 \
--top_p 0.95 \
--start 0 \
--end -1 \
--verbose \
