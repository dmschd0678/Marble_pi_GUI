import requests

# 땅 정보 모두 보기
# for i in range(40):
#     print(requests.get("http://15.165.88.215:8888/area/{}".format(i)).json())

print(requests.get("http://15.165.88.215:8888/player/0").json()["user"]["location"])
print(type(requests.get("http://15.165.88.215:8888/player/0").json()["user"]["location"]))
