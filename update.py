import requests

endpoint = "http://127.0.0.1:8000/product/5/update"
response = requests.patch(endpoint, json={'name':'Orange', "price":200})
print(response.json())
print(response.status_code)