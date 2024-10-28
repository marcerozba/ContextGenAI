# New Context Generation using Prompt AI and LangChain

This project involves sequential processing of JSON data using LangChain and GPT-based AI prompts to dynamically create new contexts. The workflow includes extracting specific fields, generating new text based on user-defined context, and updating the JSON file.

## Files Description

1. **json_text_extractor.py**
   - Extracts 'text' fields and parent 'type' from JSON.
   - Saves the results to `results.json`.

2. **contextual_text_generator.py**
   - Uses LangChain to prompt for a new context and generate related texts.
   - Saves generated texts in `new_context.json`.

3. **update_json_content.py**
   - Replaces the content in `test.json` with new texts from `new_context.json`.
   - Saves updated data to `test_context.json`.

4. **run.py**
   - Runs the three scripts sequentially.

5. **index.html**
   - Displays the results in the browser after processing.

## Running the Scripts

To execute all scripts in sequence, run:

```sh
python run.py
```


## Prerequisites

- Python 3.x
- Required libraries: `openai`, `langchain`

```sh
  pip install openai langchain
```

## Viewing the Changes

After completing the script execution, open `index.html` in a browser or use a local server:
```sh
python -m http.server 8000
```