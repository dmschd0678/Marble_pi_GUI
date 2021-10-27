from tkinter import *
import tkinter.font as tkfont
import requests
import serial
from PIL import ImageTk,Image

width = 0
height = 0


map = {"0,0" : "시작", "0,1" : "타이베이", "0,2" : "황금열쇠", "0,3" : "베이징", "0,4" : "마닐라", "0,5" : "제주도", "0,6" : "싱가포르", "0,7" : "황금열쇠", "0,8" : "카이로", "0,9" : "이스탄불", "0,10" : "무인도",
        "1,0" : "서울", "1,10" : "아테네",
        "2,0" : "사회복지기금", "2,10" : "황금열쇠",
        "3,0" : "뉴욕", "3,10" : "코펜하겐",
        "4,0" : "런던", "4,10" : "스톡홀롬",
        "5,0" : "황금열쇠", "5,10" : "콩코드여객기",
        "6,0" : "로마", "6,10" : "베른",
        "7,0" : "파리", "7,10" : "황금열쇠",
        "8,0" : "컬럼비아호", "8,10" : "베를린",
        "9,0" : "도쿄", "9,10" : "오타와",
        "10,0" : "우주 여행", "10,1" : "마드리드", "10,2" : "퀸 엘리자베스", "10,3" : "리스본", "10,4" : "하와이", "10,5" : "부산", "10,6" : "시드니", "10,7" : "상파울루", "10,8" : "황금열쇠", "10,9" : "부에노스\n아이레스", "10,10" : "사회복지기금\n접수처"
       }

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

        frame = Frame(self.rootFrame, pady = 20, padx = 20, bg = "black")
        frame.pack(fill = 'both', expand = True)

        self.bluemarble = Frame(frame, padx = 10)
        self.bluemarble.pack(fill = 'both',expand = True, side = "left")

        ranking = Frame(frame, pady = 10,padx = 10, bg = "white")
        ranking.pack(fill = 'both', side = "right")

        topPlayer = Label(ranking, width = 50, height = 5, text = "1등")
        topPlayer.pack()

        for i in range(playerNum):
            self.player.append(Player(ranking, i + 1, player_color[i]))

        image = PhotoImage(file="images/Mable_py.png", master=self.root)
        label = Label(self.bluemarble, image=image).grid(row=2, column=2, rowspan = 7, columnspan = 7)

        self.makeBoard()
        self.root.mainloop(-1)

    # 판 구현
    def makeBoard(self):
        self.land = [[0 for col in range(11)] for row in range(11)]

        for i in range(11):
            for j in range(11):

                if (i == 0 or i == 10) or (j == 0 or j == 10):

                    self.land[i][j] = Button(self.bluemarble, text=map[f"{i},{j}"], width = 16, height = 5, command = lambda x= i,y = j: self.selectButton(x,y))
                    self.land[i][j].grid(row=i, column=j, sticky=N + E + W + S)

                if (i == 0 or i == 10) and (j == 0 or j == 10):   # 꼭짓점 색칠
                    self.land[i][j].configure(bg = "orange")

        # Ybtn = Button(self.bluemarble, text="Yes", width = 13, height=4)
        # Ybtn.grid(row = 4, column = 3, sticky = N+E+W+S)
        #
        # Nbtn = Button(self.bluemarble, text="No", width = 13, height=4)
        # Nbtn.grid(row = 4, column = 6, sticky = N+E+W+S)



    def selectButton(self,x,y):
        print(x,y)

def gamePlay(screen):

    ser = serial.Serial('COM5',9600)
    while True:
        if ser.readable():
            diceNum = ser.readline().split()

            req = requests.get("")

            req = [0,8]
            diceNum = 6

            startingPoint = req

            destination = 0

            if req[0] == 0:
                if req[1] + diceNum > 10:       # ->↓
                    y = (req[1] + diceNum) % 10
                    destination = [y,10]
                else:   # ->
                    destination = [0, req[1] + diceNum]


            elif req[0] == 10:
                if req[1] + diceNum < 0:    # ↑<-       왼이
                    y = req[1] + abs(req[0] - diceNum)
                    destination[y, 0]
                else:               # <-
                    destination = [10, req[1] - diceNum]

            elif req[0] != 0 and req[1] == 10:
                if req[0] + diceNum > 10: # <- ↓
                    x = 10 - ((req[0] + diceNum) % 10)
                    destination = [10, x]
                else:                       # ↓
                    destination = [req[0] + diceNum, 10]

            elif req[0] != 10 and req[1] == 0:
                if req[0] - diceNum < 0:             # ↑ ->
                    x = abs(req[0] - diceNum)
                    destination[0,x]
                else:                               # ↑
                    destination[req[0] - diceNum, 0]
            serial.Serial.write(destination)






def start(playerNum):
    screen = window(playerNum)
    # gamePlay(screen)