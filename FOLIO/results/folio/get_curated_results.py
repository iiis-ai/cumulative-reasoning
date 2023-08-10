import json

def load_jsonl_with_error_handling(file_path):
    data = []
    errors = []
    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError as e:
                errors.append((i, line, str(e)))
    return data, errors

# Load the results data with error handling
results, errors = load_jsonl_with_error_handling("./results-*.jsonl")

# Check how many data points and errors we have
# print(len(results))

# Load the training data with error handling
train_data, train_errors = load_jsonl_with_error_handling("../../data/folio/folio-wiki-curated.jsonl")

# Check how many data points and errors we have
# print(len(train_data))

# Create dictionaries for easy access
results_dict = {entry['example_id']: entry for entry in results}
train_data_dict = {entry['example_id']: entry for entry in train_data}

# Find common example_ids between results and train_data
common_ids = set(results_dict.keys()).intersection(set(train_data_dict.keys()))

# Count correct predictions
correct_predictions = sum(results_dict[i]['prediction'] == train_data_dict[i]['label'] for i in common_ids)

# Calculate accuracy
accuracy = correct_predictions / len(common_ids)
print("Acc: ", accuracy * 100, "%")

