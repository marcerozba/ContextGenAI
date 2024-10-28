import json

file_path = 'test.json'
# Load the test.json file
with open(file_path, encoding="utf8") as file:
    test_data = json.load(file)

# Load the context.json file
with open('new_context.json', 'r') as file:
    context_data = json.load(file)

# Extract the content and replace it with context
def replace_content(obj, context_data):
    context_index = 0

    def recursive_replace(obj):
        nonlocal context_index
        if isinstance(obj, dict):
            # Handle 'doc' content replacement
            if 'content' in obj:
                for item in obj['content']:
                    if 'text' in item and 'type' in item:
                        item['text'] = context_data[context_index]['text']
                        item['type'] = context_data[context_index]['parent_type']
                        context_index += 1
            # Handle 'LpButtonReact' text replacement
            if 'type' in obj and obj['type'] == 'LpButtonReact' and 'options' in obj and 'text' in obj['options']:
                obj['options']['text'] = context_data[context_index]['text']
                context_index += 1
            # Recursively handle all other keys
            for key, value in obj.items():
                recursive_replace(value)
        elif isinstance(obj, list):
            for item in obj:
                recursive_replace(item)

    recursive_replace(obj)
    return obj

# Replace the content in test_data
updated_data = replace_content(test_data, context_data)

# Save the updated data to test_context.json
with open('test_context.json', 'w', encoding="utf8") as file:
    json.dump(updated_data, file, indent=4)

print("Content replaced and saved in 'test_context.json'")
