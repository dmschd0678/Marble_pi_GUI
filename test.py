import requests

l = [0,0,1]

req = requests.get("http://15.165.88.215:8888/area/upgrade/{}/cost?villa={}&building={}&hotel={}".format(33,*l)).json()["cost"]

print(type(req))
