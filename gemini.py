"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import google.generativeai as genai
import json
import glob

# Retrieve the API key from environment variables
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise KeyError("The environment variable GEMINI_API_KEY is not set")

print(f"API Key: {api_key}")  # Debugging: Verify if the API key is retrieved correctly

# Configure the genai with the API key
genai.configure(api_key=api_key)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 34,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

# Specify the directory containing JSON files
folder = 'info_insta'
res_folder = 'gemini_res'
os.makedirs(res_folder, exist_ok=True)

# Use glob to find all JSON files
files = glob.glob(os.path.join(folder, 'insta_*.json'))

# Loop through each JSON file
for i, file in enumerate(files):
    print(f"Processing file: {file}")

    with open(file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in '{file}': {e}")
            continue
        
    # Access the data
    username = data.get("username")
    description = data.get("description")
    
    if username and description:
        response = chat_session.send_message(f"Make a happy birthday message for {username} using this description: {description}")
        
        # Write response to file
        response_text = response.text
        base_filename = os.path.basename(file)
        filename_write = os.path.join(res_folder, os.path.splitext(base_filename)[0] + '.txt')
        with open(filename_write, "w", encoding="utf-8") as f:
            f.write(response_text)
    
    # Optionally remove the JSON file after processing
    #os.remove(file)

print("All files processed successfully.")





