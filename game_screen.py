from tkinter import *
import tkinter.font as tkfont
import requests
import serial

width = 0
height = 0

player_color = [
    "red",
    "blue",
    "yellow",
    "white"
]

url = {"init" : "15.165.88.215:8080/init",
       "toll" : "15.165.88.215:8080/player/toll?userID={}&cityID={}&usingShield={}",
       "buy"  : "15.165.88.215:8080/area/buy?userID={}&cityID={}",
       "key"  : "15.165.88.215:8080/key",
       "upgrade" : "15.165.88.215:8080/area/upgrade?user_id={}"}

class Player():
    def __init__(self, frame, text, color):
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

        goldenKeyInfo = Label(playerFrame, text = self.goldenKeyStr(self.goldenkey))

    def moneyStr(self, money):
        return f"{money // 10000}만" + ("원" if money % 10000 == 0 else str(money % 10000) + "원")

    def goldenKeyStr(self,goldenKey):
        pass

    def buy(self):
        pass

    def toll(self):
        pass

    def move(self):
        pass

    def upgrade(self):
        pass

    def key(self):
        pass

    def __lt__(self, other):
        return self.total_assets < other.total_assets

    def __repr__(self):
        return str(self.total_assets)


class window():
    def __init__(self, playerNum):

        global width,height

        self.player = []

        self.root = Tk()
        self.root.title("Marble.py")
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

        self.rootFrame = Frame(self.root)
        self.rootFrame.pack(expand = True, fill = 'both', ipady = 10)

        logo = Label(self.rootFrame, text = "Marble.py", font = font, height = 4)
        logo.pack(fill = 'x', side = 'top')

        frame = Frame(self.rootFrame, pady = 20, padx = 20, bg = "black")
        frame.pack(fill = 'both', expand = True)

        self.bluemarble = Frame(frame, padx = 10,bg = "green")
        self.bluemarble.pack(fill = 'both',expand = True, side = "left")

        ranking = Frame(frame, pady = 10,padx = 10, bg = "white")
        ranking.pack(fill = 'both', side = "right")

        topPlayer = Label(ranking, width = 50, height = 5, text = "1등")
        topPlayer.pack()

        for i in range(playerNum):
            self.player.append(Player(ranking, i + 1, player_color[i]))

        self.makeBoard()

    # 판 구현
    def makeBoard(self):
        self.land = [[0 for col in range(10)] for row in range(10)]
        for i in range(10):
            for j in range(10):
                if (i == 0 or i == 9) or (j == 0 or j == 9):
                    button = Button(self.bluemarble, text=f"{i,j}", width = 13, height = 4, command = self.selectButton)
                    button.grid(row=i, column=j, sticky=N + E + W + S)
                    self.land[i][j] = button
                if (i == 0 or i == 9) and (j == 0 or j == 9):   # 꼭짓점 색칠
                    self.land[i][j].configure(bg = "orange")

        Ybtn = Button(self.bluemarble, text="Yes", width = 13, height=4)
        Ybtn.grid(row = 4, column = 3, sticky = N+E+W+S)

        Nbtn = Button(self.bluemarble, text="No", width = 13, height=4)
        Nbtn.grid(row = 4, column = 6, sticky = N+E+W+S)

    def selectButton(self):
        pass

def gamePlay(screen):

    cmd = serial.Serial('COM5',9600)
    # while True:
    #     if cmd.readable():
    #         pass
            # cmd = serial.Serial.readline().split()

            # if cmd[0] == "":
            #     pass
            #
            # elif cmd[0] == "":
            #     pass
            #
            # elif cmd[0] == "":
            #     pass
            #
            # elif cmd[0] == "":
            #     pass
            #
            # elif cmd[0] == "":
            #     pass
            #
            # elif cmd[0] == "":
            #     pass

            # topPlayer = ""
            # for i in range(1,len(screen.player)):
            #     if screen.player[i].total_assets > screen.player[i + 1].total_assets:
            #         topPlayer



def start(playerNum):
    screen = window(playerNum)
    gamePlay(screen)