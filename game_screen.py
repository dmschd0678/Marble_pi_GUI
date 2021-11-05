from tkinter import *
import tkinter.font as tkfont
import requests
import serial
import buyLand
import showGoldenKey
from collections import deque
import threading
import useKey

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

bg_color = '#EBF4FD'

player_color = [
    "#FF5A5A",
    "#5A88FF",
    "#FFD15A",
    "#63D868"
]

url = {"init" : "http://15.165.88.215:8888/init",
       "toll" : "http://15.165.88.215:8080/player/toll?userID={}&cityID={}&usingShield={}",
       "buy"  : "http://15.165.88.215:8080/area/buy?userID={}&cityID={}",
       "key"  : "http://15.165.88.215:8080/key",
       "upgrade" : "http://15.165.88.215:8080/area/upgrade?user_id={}"}

mapImages = ["images/Start.png","images/Island.png","images/SpaceTravel.png","images/Fund.png"]

player_names = ["Emma","Arthur","Dorothy","Martin"]

sequence = []   # 순서 list

fund = 0            # 사회 복지금 모인 것
fund_cost = 10000   # 사회 복지금 내는 단위

spaceDestination = []   # 우주 여행 도착지


# 플레이어 클래스
class Player():
    def __init__(self, frame, name, color):
        self.name = name
        self.money = 500000
        self.goldenkey = []
        self.total_assets = self.money

        self.island_turn = 0
        self.spaceTravel = False

        self.location = [0,0]

        font = tkfont.Font(size = 20)

        self.playerFrame = LabelFrame(frame, borderwidth = 3, width = 350, height = 100, bg = "white")
        self.playerFrame.pack(side="top", padx=10,ipady = 10, expand=True)
        self.playerFrame.pack_propagate(0)

        NameFrame = Frame(self.playerFrame, bg = 'white')
        NameFrame.pack(side = "top", fill = 'x', expand = True)

        Name = Label(NameFrame, text = name, bg = color, font = font, fg = "white")
        Name.pack(side="top", anchor = NW)

        font = tkfont.Font(size = 15)

        self.moneyInfo = Label(self.playerFrame,text = "보유 마블   : " + self.moneyStr(self.money), font = font, bg = 'white', fg = color)
        self.moneyInfo.pack(side="top", anchor = NW)

        self.total_assetsInfo = Label(self.playerFrame, text = "총 자산      : " + self.moneyStr(self.total_assets), font = font, bg = 'white', fg = color)
        self.total_assetsInfo.pack(side="top", anchor = NW)

        self.goldenKeyInfo = Label(self.playerFrame, text = "황금열쇠    : " + self.goldenKeyStr(self.goldenkey), font = font, bg = 'white', fg = color)
        self.goldenKeyInfo.pack(side="top", anchor = NW)

    # 돈 출력 형식
    def moneyStr(self, money):
        return f"{money // 10000}만" + ("원" if money % 10000 == 0 else str(money % 10000) + "원")

    # 황금열쇠 출력 형식
    def goldenKeyStr(self,goldenKey):
        string = ""
        for i in goldenKey:
            string += i + " "
        return string

    # 비용 지불
    def cost(self, money):
        self.money -= money
        self.total_assets -= money
        self.update()

    # 돈 얻음
    def addMoney(self, money):
        self.money += money
        self.total_assets += money
        self.update()

    # 보관되는 황금열쇠
    def key(self, G_key):
        self.goldenkey.append(G_key)

    # 정보 갱신
    def update(self):
        self.moneyInfo.configure(text = "돈 : " + self.moneyStr(self.money))
        self.total_assetsInfo.configure(text = "총 자산 : " + self.moneyStr(self.total_assets))
        self.goldenKeyInfo.configure(text = "황금열쇠    : " + self.goldenKeyStr(self.goldenkey))

    # 파산
    def bankruptcy(self):
        self.playerFrame.destroy()


# 판 구현

class window():
    def __init__(self, playerNum):
        global width,height, sequence

        self.player = []

        self.root = Tk()
        self.root.title("Marble.py")
        self.root.resizable(False,False)
        self.root.state('zoomed')

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        self.playerNum = playerNum

        print(width)
        print(height)

        font = tkfont.Font(size = 30)

        self.rootFrame = Frame(self.root, bg = bg_color)
        self.rootFrame.pack(expand = True, fill = 'both', ipady = 10)

        frame = Frame(self.rootFrame, bg = bg_color)
        frame.pack(fill = 'both', expand = True, pady = 40, padx = 20)

        self.bluemarble = Frame(frame, bg = bg_color)
        self.bluemarble.pack(fill = 'both',expand = True, side = "left")

        ranking = Frame(frame, pady = 10,padx = 10, bg = bg_color, width = 400, height = 700)
        ranking.pack(fill = 'both', side = "right")
        ranking.pack_propagate(0)

        rankingFrame = Frame(ranking)
        rankingFrame.pack(side = "top")

        image = PhotoImage(file = "FirstPlayer/0.png")
        self.topPlayerName = Label(rankingFrame, image = image)
        self.topPlayerName.image = image
        self.topPlayerName.pack()

        for i in range(playerNum):                      # 플레이어 객체
            self.player.append(Player(ranking, player_names[i], player_color[i]))

        sequence = deque(range(1, playerNum + 1))

        image = PhotoImage(file="images/Mable_py.png", master=self.bluemarble)          # Marble.py 이미지 판 중간
        label = Label(self.bluemarble, image=image, bg = bg_color).grid(row=2, column=2, rowspan = 7, columnspan = 7)

        self.makeBoard()

    # 판 구현
    def makeBoard(self):
        self.land = [[0 for col in range(11)] for row in range(11)]

        index = 0

        landcnt = 1

        for i in range(11):
            for j in range(11):

                if (i == 0 or i == 10) or (j == 0 or j == 10):

                    self.land[i][j] = Button(self.bluemarble, text=map[f"{i},{j}"], width = 130, height = 85, command = lambda y = i,x = j: self.selectButton(y,x), activebackground= bg_color)

                    if (i == 0 or i == 10) and (j == 0 or j == 10):   # 꼭짓점 이미지 적용
                        image = PhotoImage(file= mapImages[index])
                        self.land[i][j].configure(image = image, borderwidth = 0, bg = bg_color)
                        self.land[i][j].image = image
                        index += 1

                    elif i == 2 and j == 0:                           # 사회 복지금 접수처 이미지 적용
                        image = PhotoImage(file = "images/Funding.png")
                        self.land[i][j].configure(image=image, borderwidth=0, bg=bg_color)
                        self.land[i][j].image = image

                    elif map[f"{i},{j}"] == "황금열쇠":                 # 황금 열쇠 이미지 적용
                        image = PhotoImage(file="images/Golden_Key.png")
                        self.land[i][j].configure(image=image, borderwidth=0, bg=bg_color)
                        self.land[i][j].image = image

                    else:                                               # 나라 이미지 적용
                        image = PhotoImage(file = "noneLand/none_{}.png".format(landcnt))
                        landcnt += 1
                        self.land[i][j].configure(image=image, borderwidth=0, bg=bg_color)
                        self.land[i][j].image = image
                    self.land[i][j].grid(row=i, column=j, sticky=N + E + W + S)

        t = threading.Thread(target=gamePlay, args=(self,))
        t.start()
        self.root.mainloop()
        t.join()

    def selectButton(self,y,x):
        global spaceDestination

        spaceDestination = [y, x]
        print(spaceDestination)

# 게임 플레이
def gamePlay(screen):
    print("check")

    global sequence, spaceDestination
    ser = serial.Serial('COM5',9600)

    requests.post(url["init"])              # 서버 초기화

    while True:

        # 1등 플레이어
        assets = [i.total_assets for i in screen.player]

        index = assets.index(max(assets))

        image = PhotoImage(file = "FirstPlayer/{}.png".format(index))
        screen.topPlayerName.configure(fg = player_color[index], image = image)
        screen.topPlayerName.image = image

        playerNum = sequence[0]

        if screen.player[playerNum].spaceTravel:

            spaceDestination = [-1,-1]

            while True:
                if spaceDestination[0] != -1 and spaceDestination[1] != -1:
                    break

            print("여행 실행")
            screen.player[playerNum].spaceTravel = False

        elif ser.readable():

            if screen.player[playerNum].island > 0:
                if screen.player[playerNum].goldenKey in "무인도 탈출":
                    if useKey.useKey("무인도 탈출"):
                        screen.player[playerNum].island = 0
                    else:
                        screen.player[playerNum].island -= 1
                        continue
                else:
                    screen.player[playerNum].island -= 1
                    continue

            # 주사위 값 받아오기
            diceNum = ser.readline()

            destination = []

            # 이동할 위치 계산
            if screen.player[playerNum].location[0] == 0:
                if screen.player[playerNum].location[1] + diceNum > 10:       # ->↓
                    y = (screen.player[playerNum].location[1] + diceNum) % 10
                    destination = [y,10]
                else:   # ->
                    destination = [0, screen.player[playerNum].location[1] + diceNum]


            elif screen.player[playerNum].location[0] == 10:
                if screen.player[playerNum].location[1] + diceNum < 0:    # ↑<-
                    y = screen.player[playerNum].location[1] + abs(screen.player[playerNum].location[0] - diceNum)
                    destination = [y, 0]
                else:               # <-
                    destination = [10, screen.player[playerNum].location[1] - diceNum]

            elif screen.player[playerNum].location[0] != 0 and screen.player[playerNum].location[1] == 10:
                if screen.player[playerNum].location[0] + diceNum > 10: # <- ↓
                    x = 10 - ((screen.player[playerNum].location[0] + diceNum) % 10)
                    destination = [10, x]
                else:                       # ↓
                    destination = [screen.player[playerNum].location[0] + diceNum, 10]

            elif screen.player[playerNum].location[0] != 10 and screen.player[playerNum].location[1] == 0:
                if screen.player[playerNum].location[0] - diceNum < 0:             # ↑ -> + 월급
                    x = abs(screen.player[playerNum].location[0] - diceNum)
                    destination = [0,x]
                    screen.player[playerNum].addMoney(20000)

                else:                               # ↑
                    destination = [screen.player[playerNum].location[0] - diceNum, 0]

            serial.Serial.write(destination)

            y,x = destination
            screen.player[playerNum].location = destination


        # 이동 후 기능

        if map[f"{y},{x}"] == "황금열쇠":
            req = requests.get()
            Storage = showGoldenKey.showGoldenKey(1,"","","")               # --------------------------------------------------------------------
            if Storage:
                screen.player[playerNum].goldenKey.append(req[0])
            else:
                pass

        elif map[f"{y},{x}"] == "사회복지기금":
            screen.player[playerNum].cost(fund_cost)
            fund += fund_cost

        elif map[f"{y},{x}"] == "사회복지기금 접수처":
            screen.player[playerNum].money += fund
            fund = 0

        elif map[f"{y},{x}"] == "우주여행":
            screen.player[playerNum].spaceTravel = True

        elif map[f"{y},{x}"] == "무인도":
            screen.player[playerNum].island = 3

        else:           # 나라를 밟았을 때

            if playerNum == "   ":   # 주인이 있을 때

                if player_names == "": # 내가 주인 일 때
                    pass

                else:
                    cost = requests.get()       # ------------------------------------------------------------

                    if screen.player[playerNum].goldenKey in "우대권":
                        useKey.useKey("우대권", cost)
                    elif screen.player[playerNum].money >= cost:
                        screen.player[playerNum].cost(cost)

            else:       #주인이 없을 때
                cost = requests.get()       # ------------------------------------------------------------------

                if buyLand.buyLand(map[f"{y},{x}"], 0, cost) and screen.player[playerNum].money >= cost:
                    screen.player[playerNum].money -= cost

                    color = ""

                    if playerNum == 0:
                        color = "red"
                    elif playerNum == 1:
                        color = "blue"
                    elif playerNum == 2:
                        color = "yellow"
                    elif playerNum == 3:
                        color = "green"

                    image = PhotoImage(file = "{}Land/{}.png".format(color, map[f"{y},{x}"]))
                    screen.land[y][x].configure(image = image)


        if screen.player[playerNum].money < 0:      # 파산 및 순서 돌리기
            screen.player[playerNum].location = requests.get()    # 플레이어의 모든 땅 갖고 오기    # ---------------------------------------
            ser.write(f"B {playerNum}")
            screen.player[playerNum].bankruptcy()

            sequence.remove(playerNum)
        else:
            sequence.append(sequence.popleft())

def start(playerNum):
    window(playerNum)