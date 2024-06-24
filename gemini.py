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
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
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

chat_session = model.start_chat(
  history=[
  ]
)


# Specify the directory containing images
folder = 'info_insta'

# Use glob to find all image files with a specific extension (e.g., .jpg, .png)
files = glob.glob(os.path.join(folder, '*'))

username=""
description = ""

# Loop through each image file
for i, file in enumerate(files):
    print(f"Processing file: {file}")
    
    filename_read = f"info_insta/insta_{i+1}.json"
    with open(filename_read, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    # Access the data
    username = data.get("username")
    description = data.get("description")
    response = chat_session.send_message("Make an happy birthday message for the user" + username + "using has context this description from the instagram post: " + description)
    
    response_to_string = str(response.text)
    filename_write = f"gemini_res/insta_{i+1}.txt"
    with open(filename_write, "w", encoding="utf-8") as f:
        f.write(response)
    os.remove(file)

print(response.text)