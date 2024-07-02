import emoji


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
    "max_output_tokens": 20,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

# Specify the directory containing JSON files
folder = 'contexto'

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
    contexto = data.get("contexto")
    
    if contexto:
        response = chat_session.send_message(f"Choose an emoji from the this API: https://carpedm20.github.io/emoji/docs/ using as context the following context: {contexto}. Your output should only be the string for the emoji code, with the following style ´:name_of_the_emoji:´")
        
        # Write response to file
        response_text = response.text
        filename_write = f"emojis/insta_{i+1}.txt"
        with open(filename_write, "w", encoding="utf-8") as f:
            f.write(response_text)
    
    # Optionally remove the JSON file after processing
    os.remove(file)
    print(response)
    #print(emoji.emojize(response))

print("All files processed successfully.")