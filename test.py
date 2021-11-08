import requests

req = ""

while True:
    req = requests.get("http://15.165.88.215:8888/key/{1}").json()

    if req["title"] == "노벨 평화상":
        print(req)
        break
