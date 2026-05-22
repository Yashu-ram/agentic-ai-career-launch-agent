import requests
import time

url = "http://localhost:11434/api/chat"

payload = {
    "model": "qwen2.5:3b",
    "messages": [
        {
            "role": "user",
            "content": "What is Python?"
        }
    ],
    "stream": False
}

start = time.time()

response = requests.post(url, json=payload)

end = time.time()

data = response.json()

print("\nModel Response:\n")
print(data["message"]["content"])

print(f"\nResponse Time: {end - start:.2f} seconds")

print("\nToken Usage:")
print("Prompt Tokens:", data.get("prompt_eval_count"))
print("Completion Tokens:", data.get("eval_count"))