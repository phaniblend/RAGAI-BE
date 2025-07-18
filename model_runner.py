import requests

def query_mixtral(prompt):
    response = requests.post(
        "http://localhost:8000/generate",
        json={"prompt": prompt, "max_tokens": 1024}
    )
    return response.json().get("text") 