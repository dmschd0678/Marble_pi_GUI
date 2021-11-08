import requests

req = int(requests.get("http://15.165.88.215:8888/area/buy/11/cost?villa=1&building=0&hotel=0").json()["cost"])

print(req)
