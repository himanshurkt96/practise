import requests

response=requests.get("https://httpbin.org/#/get")

print(response.status_code)
res_json = response.json()

print(res_json)