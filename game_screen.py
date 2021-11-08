import binascii
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
        "10,0" : "우주 여행", "10,1" : "마드리드", "10,2" : "퀸 엘리자베스호", "10,3" : "리스본", "10,4" : "하와이", "10,5" : "부산", "10,6" : "시드니", "10,7" : "상파울루", "10,8" : "황금열쇠", "10,9" : "부에노스 아이레스", "10,10" : "사회복지기금 접수처"
       }

landLocation = ['0,0', '0,1', '0,2', '0,3', '0,4', '0,5', '0,6', '0,7', '0,8', '0,9', '0,10',
       '1,10', '2,10', '3,10', '4,10', '5,10', '6,10', '7,10', '8,10', '9,10', '10,10',
        '10,9', '10,8', '10,7', '10,6', '10,5', '10,4', '10,3', '10,2', '10,1', '10,0',
        '9,0', '8,0', '7,0', '6,0', '5,0', '4,0','3,0','2,0','1,0'
       ]

landNum = ["시작", "타이베이", "황금열쇠", "베이징", "마닐라", "제주도", "싱가포르", "황금열쇠", "카이로", "이스탄불", "무인도",
           "아테네", "황금열쇠", "코펜하겐", "스톡홀롬", "콩코드여객기", "베른", "황금열쇠", "베를린", "오타와", "사회복지기금 접수처",
           "부에노스아이레스", "황금열쇠", "상파울루", "시드니", "부산", "하와이", "리스본", "퀸 엘리자베스호", "마드리드", "우주여행",
           "도쿄", "컬럼비아호", "파리", "로마", "황금열쇠", "런던", "뉴욕", "사회복지기금", "서울"
           ]

bg_color = '#EBF4FD'

player_color = [
    "#FF5A5A",
    "#5A88FF",
    "#FFD15A",
    "#63D868"
]

url = {"init" : "http://15.165.88.215:8888/init",                                   # 초기화
       "playerInfo" : "http://15.165.88.215:8888/player/{}",
       "getGoldenKey" : "http://15.165.88.215:8888/key/{}",                         # 황금열쇠 받기
       "move" : "http://15.165.88.215:8888/player/move?user_id={}&dice_value={}",   # 움직임
       "bankruptcy" : "http://15.165.88.215:8888/player/bankruptcy/{}",             # 파산
       "pay" : "http://15.165.88.215:8888/player/toll?userID={}&cityID={}&usingShield={}",  # 통행료 지불
       "payInfo" : "http://15.165.88.215:8888/player/toll?cityID={}",                       # 통행료 정보
       "getLand" : "http://15.165.88.215:8888/area/{}",                                     # 땅 정보 가져오기
       "Landcost" : "http://15.165.88.215:8888/area/buy/{}/cost?villa=1&building=0&hotel=0", # 구입 금액
       "buyLand" : "http://15.165.88.215:8888/area/buy/{}?userID={}&villa=1&building=0&hotel=0",    # 땅 구입
       "upgradeLand" : "http://15.165.88.215:8888/area/upgrade/{}?user_id={}&villa={}&building={}&hotel={}", # 땅 업그레이드
       "upgradecost" : "http://15.165.88.215:8888/area/upgrade/{}/cost?villa={}&building={}&hotel={}",      # 땅 업그레이드 금액
       "funding" : 'http://15.165.88.215:8888/area/social/reception?user_id={}',    # 사회 복지기금 내기
       "fund" : "http://15.165.88.215:8888/area/social/dispatch?user_id={}"         # 사회 복지기금 받기
        }

mapImages = ["images/Start.png","images/Island.png","images/SpaceTravel.png","images/Fund.png"]

player_names = ["Emma","Arthur","Dorothy","Martin"]

sequence = deque()   # 순서 list

spaceDestination = []   # 우주 여행 도착지

# 플레이어 클래스
class Player():
    def __init__(self, frame, name, color, num):
        self.name = name
        self.money = 500000
        self.goldenkey = []
        self.total_assets = self.money
        self.num = num

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
        str = ""
        if money // 100000000 > 1:
            str += f"{money // 100000000}" + "억"
            money %= 100000000
        if money // 10000 > 1:
            str += f"{money // 10000}" + "만"
            money %= 10000
        if money % 10000 != 0:
            str += money % 10000
        str += "원"
        return str

    # 황금열쇠 출력 형식
    def goldenKeyStr(self,goldenKey):
        string = ""
        for i in goldenKey:
            string += i + " "
        return string

    # 보관되는 황금열쇠
    def key(self, G_key):
        self.goldenkey.append(G_key)

    # 정보 갱신
    def update(self):
        req = requests.get(url["playerInfo"].format(self.num)).json()
        self.money = req["user"]["money"]
        self.total_assets = req["user"]["building_money"]
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
        self.root.attributes('-fullscreen', True)

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
            self.player.append(Player(ranking, player_names[i], player_color[i], i))

        sequence = deque(range(playerNum))

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

                    self.land[i][j] = Button(self.bluemarble, width = 130, height = 85, command = lambda y = i,x = j: self.selectButton(y,x), activebackground= bg_color)

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
    ser = serial.Serial('/dev/ttyACM0',9600)

    requests.post(url["init"])              # 서버 초기화

    while True:

        # 1등 플레이어
        assets = [i.total_assets for i in screen.player]

        index = assets.index(max(assets))

        image = PhotoImage(file = "FirstPlayer/{}.png".format(index))
        screen.topPlayerName.configure(fg = player_color[index], image = image)
        screen.topPlayerName.image = image

        playerNum = sequence[0]

        # 우주 여행
        if screen.player[playerNum].spaceTravel:

            spaceDestination = [-1,-1]

            while True:
                if spaceDestination[0] != -1 and spaceDestination[1] != -1:
                    break
            des = landLocation.index(f"{spaceDestination[0]},{spaceDestination[1]}")
            if des > 30:
                des = 40 - 30 + des
            else:
                des -= 30

            requests.patch(url["move"].format(playerNum,des))

            print("여행 실행")
            screen.player[playerNum].spaceTravel = False

        # 주사위를 굴려야 됨
        elif ser.readable():

            if screen.player[playerNum].island_turn > 0:        # 무인도에 갇혀 있다면
                if "무인도 탈출" in screen.player[playerNum].goldenkey:  # 무인도 탈출을 갖고 있다면
                    if useKey.useKey("무인도 탈출"):                     # 탈출카드를 쓴다면
                        screen.player[playerNum].island_turn = 0
                        del screen.player[playerNum].goldenKey[screen.player[playerNum].goldenKey.index("무인도 탈출")]
                    else:                                               # 계속 갇혀있기
                        screen.player[playerNum].island_turn -= 1
                        continue
                else:                                                   # 계속 갇혀있기
                    screen.player[playerNum].island_turn -= 1
                    continue

            # 주사위 값 받아오기
            diceNum = int(ser.readline().decode("utf-8"))
            print(diceNum)
            curLocation = requests.get(url["playerInfo"].format(playerNum))
            curLocation = landLocation[curLocation.json()["user"]["location"]]
            # 서버 주사위 값 넘기기
            requests.patch(url["move"].format(playerNum,diceNum))
            location = requests.get(url["playerInfo"].format(playerNum))
            location = landLocation[location.json()["user"]["location"]]

            ser.write((f"M {landLocation[curLocation]} {landLocation[location]}").encode("utf-8"))
            # ser.write(binascii.unhexlify(f"{landLocation[location]}"))


            y,x = landLocation[location].split(',')
            y,x = int(y), int(x)

        # 이동 후 기능
        special_land = ["황금열쇠", "사회복지기금", "사회복지기금 접수처", "우주여행","무인도"]

        if map[f"{y},{x}"] == "황금열쇠":

            req = requests.get(url["getGoldenKey"].format(playerNum))
            req = req.json()

            Storage = showGoldenKey.showGoldenKey(req["key_id"],req["title"],req["situation"] + "\n" + req["command"])               # --------------------------------------------------------------------

            if Storage:
                screen.player[playerNum].key(req["title"])

        if map[f"{y},{x}"] == "사회복지기금":
            requests.patch(url["funding"].format(playerNum))
            continue

        if map[f"{y},{x}"] == "사회복지기금 접수처":
            requests.patch(url["fund"].format(playerNum))
            continue

        if map[f"{y},{x}"] == "우주여행":
            screen.player[playerNum].spaceTravel = True
            continue

        if map[f"{y},{x}"] == "무인도":
            screen.player[playerNum].island_turn = 3
            continue

        if map[f"{y},{x}"] not in special_land:           # 나라를 밟았을 때

            area_id = landNum.index(map[f"{y},{x}"])

            req = requests.get(url["getLand"].format(area_id))      # 땅 정보 가져오기
            req = req.json()

            if req["city"]["owner"] >= 0:   # 주인이 있을 때


                if playerNum == req["city"]["owner"]: # 내가 주인 일 때
                    land_type = requests.get(url["getLand"].format(area_id))
                    land_type = land_type.json()["city"]["area_type"]

                    if land_type == "cant_build":
                        continue

                    buildings = req["city"]["villa_cnt"] + req["city"]["building_cnt"] + req["city"]["hotel_cnt"]

                    upgradeInfo = []
                    buildingNum = 0

                    if buildings == 1:      # 주택만 있을 때
                        upgradeInfo = [0,1,0]
                        buildingNum = 1
                    elif buildings == 2:    # 주택 + 빌딩이 있을 때
                        upgradeInfo = [0,0,1]
                        buildingNum = 2
                    else:                   # 다 있을 때
                        continue            # 아무것도 하지 않고 종료

                    upgradeCost = requests.get(url["upgradecost"].format(area_id, *upgradeInfo)).json()["cost"]
                    playerMoney = requests.get(url["playerInfo"].format(playerNum)).json()["user"]["money"]
                    if upgradeCost < playerMoney:

                        if buyLand.buyLand(req["city"]["city_name"], buildingNum, upgradeCost):
                            requests.patch(url["upgradeLand"].format(area_id,playerNum,upgradeInfo))

                            ser.write(f'L {landLocation[location]} {playerNum} {buildingNum + 1}').encode("utf-8")
                            # ser.write(binascii.unhexlify(f'L {landLocation[location]} {playerNum} {buildingNum + 1}'))

                    requests.patch(url["upgradeLand"].format(area_id,playerNum,*upgradeInfo))


                else:
                    cost = requests.get(url["payInfo"].format(area_id))
                    shield = 0
                    if "우대권" in screen.player[playerNum].goldenkey:
                        shield = useKey.useKey("우대권", cost)
                        del screen.player[playerNum].goldneKey[screen.player[playerNum].goldenKey.index("우대권")]

                    requests.patch(url["pay"].format(playerNum,area_id,shield))

            else:       #주인이 없을 때
                cost = int(requests.get(url["Landcost"].format(area_id)).json()["cost"])# ------------------------------------------------------------------
                playerMoney = int(requests.get(url["playerInfo"]).json()["user"]["money"])
                if playerMoney >= cost:

                    if buyLand.buyLand(map[f"{y},{x}"], 0, cost):

                        color = ""

                        if playerNum == 0:
                            color = "red"
                        elif playerNum == 1:
                            color = "blue"
                        elif playerNum == 2:
                            color = "yellow"
                        elif playerNum == 3:
                            color = "green"

                        requests.patch(url["buyLand"].format(area_id,playerNum))

                        image = PhotoImage(file = "{}Land/{}.png".format(color, map[f"{y},{x}"]))
                        screen.land[y][x].configure(image = image)

                        ser.write((f"L {landLocation[area_id]} {playerNum} {1}").encode("utf-8"))
                        # ser.write(binascii.unhexlify(f"L {landLocation[area_id]} {playerNum} {1}"))


        if screen.player[playerNum].money < 0:      # 파산 및 순서 돌리기
            lands = requests.put(url["bankruptcy"].format(playerNum)).json()    # 플레이어의 모든 땅 갖고 오기    # ---------------------------------------
            lands = lands["areas"]

            result = ""

            for i in lands:
                result += landLocation[landNum.index(i)]

            ser.write(f"B {result}".encode('utf-8'))
            # ser.write(binascii.unhexlify(f"B {result}"))

            screen.player[playerNum].bankruptcy()

            sequence.popleft()
        else:
            sequence.append(sequence.popleft())

        for i in sequence:
            screen.player[i].update()

def start(playerNum):
    window(playerNum)