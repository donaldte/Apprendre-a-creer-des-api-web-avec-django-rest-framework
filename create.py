import requests

endpoint = "http://127.0.0.1:8000/products"
response = requests.post(endpoint, json={'name':'range', 'content':'', 'price':300})
print(response.json())
print(response.status_code)