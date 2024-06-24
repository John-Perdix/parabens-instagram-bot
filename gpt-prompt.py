from openai import OpenAI

# Load API key from a file
with open("openai-key.txt", "r") as f:
    api_key = f.read().strip()
client = OpenAI(api_key=api_key)


def get_text_from_chatgpt(prompt):
    message={
        "role":"user",
        "content": prompt
    }
    response = client.chat.completions.create(
        messages=[message],
        model="gpt-3.5-turbo"
    )
    return response.choices[0].message.content
    #return response.choices[0].text.strip()

# Example prompt
prompt = "Hello"

# Get response from ChatGPT
text = get_text_from_chatgpt(prompt)
print(text)