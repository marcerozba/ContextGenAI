import subprocess

# Define the script files
scripts = [
    "json_text_extractor.py",
    "contextual_text_generator.py",
    "update_json_content.py"
]

for script in scripts:
    if script == "contextual_text_generator.py":
        # Prompt the user for the new context
        context_input = input("Please provide a new context for the page: ") + "\n"
        
        # Use Popen to handle interactive input
        process = subprocess.Popen(["python", script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Provide the input context
        stdout, stderr = process.communicate(input=context_input)

        print(stdout)
        if process.returncode != 0:
            print(f"Error occurred while running {script}:")
            print(stderr)
            break
    else:
        result = subprocess.run(["python", script], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Error occurred while running {script}:")
            print(result.stderr)
            break
