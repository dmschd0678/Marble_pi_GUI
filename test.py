import requests

req = requests.get("http://15.165.88.215:8888/area/32")
a = req["city"]["owner"]
print(a)