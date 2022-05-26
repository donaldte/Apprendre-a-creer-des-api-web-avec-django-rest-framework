import requests

endpoint = "http://httpbin.org/anything"
response = requests.get(endpoint, data={'bonjour':'hello'})
print(response.text)

# HTTP RESQUEST --> HTML
# REST API HTTP ---> JSON JAVASCRIPT OBJECT NOTATION
{'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.27.1', 'X-Amzn-Trace-Id': 'Root=1-628fffaf-65183b5b7686933f18f568c6'}, 'json': None, 'method': 'GET', 'origin': '129.0.76.71', 'url': 'http://httpbin.org/anything'}
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.27.1", 
    "X-Amzn-Trace-Id": "Root=1-62900011-2aebefd83e94ea5e78f4a126"
  }, 
  "json": null, 
  "method": "GET", 
  "origin": "129.0.76.71", 
  "url": "http://httpbin.org/anything"
}