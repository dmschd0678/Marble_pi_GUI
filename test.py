import requests
import serial


ser = serial.Serial()

ser.write(b"")
req = requests.get("http://15.165.88.215:8888/key/1")
req = req.json()
print(req["title"])
print(req)

l = [1,1,1]
req = requests.get("http://15.165.88.215:8888/player/1")
req = req.json()
print(req["user"]["user_id"])
