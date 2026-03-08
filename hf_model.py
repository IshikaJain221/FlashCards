import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def query_model(prompt):

    payload = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",  # corrected model ID
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    if not response.ok:
        error_info = response.json().get("error", {})
        raise RuntimeError(
            f"API request failed [{response.status_code}]: "
            f"{error_info.get('message', response.text)}"
        )

    result = response.json()

    if "choices" not in result:
        raise KeyError(
            f"Unexpected API response — 'choices' key missing. Full response: {result}"
        )

    return result["choices"][0]["message"]["content"]