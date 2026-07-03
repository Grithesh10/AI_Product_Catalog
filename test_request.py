import requests

print("Checking Hugging Face connection...")

try:
    response = requests.get("https://huggingface.co", timeout=10)
    print("Status Code:", response.status_code)
except Exception as e:
    print("Error:", e)