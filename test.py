import requests

req = requests.get("http://15.165.88.215:8888/player/1").json()["user"]["money"]
print(type(req))