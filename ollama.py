import requests
import json

def thefun(user_message):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "phi3",
        "prompt": user_message,
        "stream": False  # fixed typo here
    }
    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
        timeout=120
    )
    if response.status_code == 200:
        result = response.json()
        bot_response = result.get("response", "sorry i am not able to answer your question")
        return bot_response.strip()
    else:
        return f"Error: {response.status_code} - {response.text}"
