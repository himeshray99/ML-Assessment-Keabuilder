import requests

def get_embedding(text):
    if not text.strip():
        return None

    response = requests.post(
        "http://localhost:11434/api/embeddings",
        json={
            "model": "nomic-embed-text",
            "prompt": text
        }
    )

    data = response.json()

    if "embedding" not in data or not data["embedding"]:
        return None

    return data["embedding"]