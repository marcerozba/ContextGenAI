import json

# Load the JSON file
file_path = 'test.json'
with open(file_path, encoding="utf8") as file:
    data = json.load(file)

# RESULTS SAVED IN A FILE
# Initialize a list to store results
results = []

# Recursive function to find 'text' and its parent 'type'
def find_text_with_parent_type(obj, parent_type=None):
    if isinstance(obj, dict):
        if 'text' in obj:
            results.append({'text': obj['text'], 'parent_type': parent_type})
        current_type = obj.get('type', parent_type)
        for key, value in obj.items():
            find_text_with_parent_type(value, current_type)
    elif isinstance(obj, list):
        for item in obj:
            find_text_with_parent_type(item, parent_type)

# Extract text and its parent type
find_text_with_parent_type(data)

# Write results to a file
with open('results.json', 'w') as file:
    json.dump(results, file, indent=4)

print("Results saved to results.json")