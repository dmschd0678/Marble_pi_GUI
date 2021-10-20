from tkinter import *
import tkinter.font as tkfont
import requests
import serial

height_ratio = 216
width_ratio = 384

width = 0
height = 0

player_color = [
    "red",
    "blue",
    "yellow",
    "white"
]

url = {"init" : "15.165.88.215:8080/init",
       "toll" : "15.165.88.215:8080/player/toll?userID=1&cityID=2&usingShield=0",
       "buy"  : "15.165.88.215:8080/area/buy?userID=1&cityID=2",
       "key"  : "15.165.88.215:8080/key",
       "upgrade" : "15.165.88.215:8080/area/upgrade?user_id=1"}

class Player():
    def __init__(self, frame, text, color):
        # requests.post(url["init"])
        self.money = 500000
        self.goldenkey = []
        self.total_assets = self.money

        playerFrame = LabelFrame(frame, width = 50, height = 5)
        playerFrame.pack(side = "top", padx = 10, pady = 10, ipady = 20, expand = True)

        Name =Label(playerFrame,text = text, width = 40, bg = color, font = tkfont.Font(size = 20))
        Name.pack(side = "top", fill = 'x')

        moneyInfo = Label(playerFrame,text = "돈 : " + self.moneyStr(self.money))
        moneyInfo.pack(fill = 'x')

        total_assetsInfo = Label(playerFrame, text = "총 자산 : " + self.moneyStr(self.total_assets))
        total_assetsInfo.pack(fill = 'x')

    def moneyStr(self, money):
        return f"{money // 10000}만" + ("원" if money % 10000 == 0 else str(money % 10000) + "원")


class window():
    def __init__(self, playerNum):

        global width,height

        self.player = []

        self.root = Tk()
        self.root.resizable(False,False)
        self.root.state('zoomed')

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        print(width)
        print(height)

        # 노트북 화면 크기
        # width = 1536
        # height = 864

        # 모니터 화면 크기
        # width = 1920
        # height = 1080

        font = tkfont.Font(size = 30)

        rootFrame = Frame(self.root)
        rootFrame.pack(expand = True, fill = 'both', ipady = 10)

        logo = Label(rootFrame, text = "Marble.py", font = font, height = 4)
        logo.pack(fill = 'x', side = 'top')

        frame = Frame(rootFrame, pady = 20, padx = 20, bg = "black")
        frame.pack(fill = 'both', expand = True)

        bluemarble = Frame(frame, padx = 10,bg = "green")
        bluemarble.pack(fill = 'both',expand = True, side = "left")

        ranking = Frame(frame, pady = 10,padx = 10, bg = "white")
        ranking.pack(fill = 'both', side = "right")

        for i in range(playerNum):
            self.player.append(Player(ranking, i, player_color[i]))

        font = tkfont.Font()

        Ybtn = Button(rootFrame, text = "Yes", height = 2, font = font)
        Ybtn.pack(side = "left", fill = "x",expand = True, padx = 10)

        Nbtn = Button(rootFrame, text = "No", height = 2, font = font)
        Nbtn.pack(side = "right", fill = "x",expand = True, padx = 10)

def start(playerNum):
    window(playerNum)