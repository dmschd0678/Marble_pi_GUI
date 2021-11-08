import requests

req = int(requests.get("http://15.165.88.215:8888/player/0").json()["user"]["location"])

print(req)
