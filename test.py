import requests

req = requests.post("http://15.165.88.215:8888/init")
print(req.text)

req = requests.get("http://15.165.88.215:8888/key/1")
print(req.text)