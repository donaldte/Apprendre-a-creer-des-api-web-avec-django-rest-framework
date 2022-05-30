import requests

endpoint = "http://127.0.0.1:8000/product/"
response = requests.get(endpoint)
print(response.json())
print(response.status_code)

# HTTP RESQUEST --> HTML
# REST API HTTP ---> JSON JAVASCRIPT OBJECT NOTATION
