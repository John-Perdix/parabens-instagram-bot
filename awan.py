import requests
import json

url = "https://api.awanllm.com/v1/completions"
AWANLLM_API_KEY = "f3a1876a-3e55-49b8-8e4d-f44e8bc3c27c"

payload = json.dumps({
  "model": "Awanllm-Llama-3-8B-Dolfin",
  "prompt": "Hello!",
  "repetition_penalty": 1.1,
  "temperature": 0.7,
  "top_p": 0.9,
  "top_k": 40,
  "max_tokens": 1024,
  "stream": True
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': f"Bearer {AWANLLM_API_KEY}"
}

try:
    response = requests.request("POST", url, headers=headers, data=payload)
    print(f"Response status code: {response.status_code}")
    
    if response.status_code == 200:
        try:
            response_json = response.json()
            generated_text = response_json['completions'][0]['text']
            print(generated_text)
        except json.decoder.JSONDecodeError:
            print("Error: Non-json response received.")
            print(response.text)
    else:
        print(f"Error: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")

