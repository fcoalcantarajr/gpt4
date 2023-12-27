import requests
import os
import dotenv

dotenv.load_dotenv()

HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")

headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
API_URL = "https://api-inference.huggingface.co/models/gpt2"
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query({"inputs": "What is love?"})
print(data)
