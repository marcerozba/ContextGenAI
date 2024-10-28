# import openai
import json
from collections import defaultdict
# import re
# from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Initialize the OpenAI client
# client = openai.OpenAI()
# llm = OpenAI(
llm = ChatOpenAI(
    model="gpt-3.5-turbo", 
    temperature=0.7
)

# Define the prompt template
# prompt_template = PromptTemplate(
# prompt = PromptTemplate.from_template(
#     input_variables=["context", "parent_type", "count"],
#     template="Generate {count} texts for {parent_type} based on the context: {context}."
# )
prompt = PromptTemplate.from_template("Generate {count} texts for {parent_type} based on the context: {context}.\n")
print("prompt")
print(prompt)


# Set up the LLMChain
chain = prompt | llm

# Define a function to prompt the user for new contexts and generate texts
def generate_new_texts():
    # Prompt the user for new contexts
    context = input("Please provide a new context for the page: ")

    # Load the existing result.json structure
    with open('results.json', 'r') as json_file:
        existing_data = json.load(json_file)

    # Count the number of texts needed for each parent_type
    parent_type_counts = defaultdict(int)
    for item in existing_data:
        parent_type_counts[item["parent_type"]] += 1

    # Generate new texts for each parent_type
    new_texts = {parent_type: [] for parent_type in parent_type_counts}
    print("new texts:")
    print(new_texts)

    for parent_type, count in parent_type_counts.items():
        # response = llm_chain.run({
        response = chain.invoke({
            "context": context,
            "parent_type": parent_type,
            "count": count
        })
        
        # Split the generated response by new lines to get individual texts
        # generated_texts = response.strip().split('\n')
        generated_texts = response.content.strip().split('\n')
        new_texts[parent_type].extend(generated_texts)

    # Construct the new result JSON structure
    new_result_json = []
    for item in existing_data:
        parent_type = item["parent_type"]
        new_text = new_texts[parent_type].pop(0)
        new_result_json.append({
            "text": new_text,
            "parent_type": parent_type
        })

    # Save the generated texts to new_context.json
    with open('new_context.json', 'w') as json_file:
        json.dump(new_result_json, json_file, indent=4)

    print("New context file has been created as 'new_context.json'.")

# Run the function
generate_new_texts()

    # Prepare messages for each parent_type dynamically
    # messages = {}
    # for parent_type, count in parent_type_counts.items():
    #     if parent_type == "LpButtonReact":
    #         messages[parent_type] = [
    #             {"role": "system", "content": "You are a helpful assistant."},
    #             {"role": "user", "content": f"Generate {count} new texts for a button based on the following context: {context}"}
    #         ]
    #     else:
    #         messages[parent_type] = [
    #             {"role": "system", "content": "You are a helpful assistant."},
    #             {"role": "user", "content": f"Generate {count} new texts for {parent_type} based on the following context: {context}"}
    #         ]

    # Store new texts
#     new_texts = {parent_type: [] for parent_type in parent_type_counts}

#     # Generate new texts for each parent_type
#     for parent_type, message in messages.items():
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=message,
#             max_tokens=50 * parent_type_counts[parent_type],
#             n=1
#         )

#         # Extract the generated texts based on parent_type
#         generated_texts = response.choices[0].message.content.strip().split('\n')
#         for text in generated_texts:
#             if text:
#                 new_texts[parent_type].append(text)

#     # Create the new result.json structure
#     new_result_json = []
#     for item in existing_data:
#         parent_type = item["parent_type"]
#         new_text = new_texts[parent_type].pop(0)
#         new_result_json.append({
#             "text": new_text,
#             "parent_type": parent_type
#         })

#     return new_result_json

# # Function to remove leading numbers from texts
# def remove_leading_numbers(text):
#     return re.sub(r'^\d+\.\s*', '', text)

# # Generate the new texts
# new_result_json = generate_new_texts()

# # Remove leading numbers from the texts
# for item in new_result_json:
#     item["text"] = remove_leading_numbers(item["text"])

# # Save the new result in new_context.json to a file
# with open('new_context.json', 'w') as json_file:
#     json.dump(new_result_json, json_file, indent=4)

# print("New context.json saved successfully.")