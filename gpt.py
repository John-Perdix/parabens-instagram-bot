import openai

# Load API key from a file
with open("openai-key.txt", "r") as f:
    apiKey = f.read().strip()

client = openai.OpenAI(api_key=apiKey)


def get_gpt_response(user_input):
    message={
        "role":"user",
        "content": user_input
    }
    response = client.chat.completions.create(
        messages=[message],
        model="gpt-3.5-turbo"
    )
    return response.choices[0].message.content

def chat():
    while True:
        user_input = input("You: ")
        if user_input == "exit":
            print("ChaTtBot: Goodbye")
            break
        response = get_gpt_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__" :
    chat()