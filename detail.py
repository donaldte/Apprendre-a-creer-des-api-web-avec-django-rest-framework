import requests

endpoint = "http://127.0.0.1:8000/product/retrieve/<int:5>"
response = requests.get(endpoint)
print(response.json())
print(response.status_code)