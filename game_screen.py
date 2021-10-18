from tkinter import *
import tkinter.font as tkfont
import requests

url = {"init" : "15.165.88.215:8080/init",
       "toll" : "15.165.88.215:8080/player/toll?userID=1&cityID=2&usingShield=0",
       "buy"  : "15.165.88.215:8080/area/buy?userID=1&cityID=2",
       "key"  : "15.165.88.215:8080/key",
       "upgrade" : "15.165.88.215:8080/area/upgrade?user_id=1"}


class Player():
    def __init__(self):
        self.money = 500000
        self.goldenKey = ["a","b","c","d"]
        self.total_assets = self.money

    def toll(self):
        pass

    def buy(self):
        pass


class PlayerInfo():


    def __init__(self, frame, name, color):
        font = tkfont.Font(size=30)

        self.player = Player()

        self.playerName = Label(frame, text = name, bg = color, font = font)
        self.playerName.pack(fill='x', side='top',anchor = "n")

        self.__moneyInfo = Label(frame, text = "보유 돈 : " + self.strMoney(self.player.money), bg = color, font = font)
        self.__moneyInfo.pack(fill = 'x', side = 'top',anchor = "n")

        self.__totalAssetsInfo = Label(frame, text = "총 자산 : " + self.strMoney(self.player.total_assets), bg = color, font = font)
        self.__totalAssetsInfo.pack(fill = 'x', side = 'top', anchor = 'n')

        self.__goldenKeyInfo = Label(frame, text = "보유 황금열쇠 : " + str(list(i for i in self.player.goldenKey)), bg = color, font = font)
        self.__goldenKeyInfo.pack(fill = 'x', side = 'top',anchor = "n")

    def strMoney(self, money):
        money = str(money // 10000) + "만" + \
                   (str(money % 10000) + "원"
                    if str(money % 10000) != "0" else "원")
        return money

    def setMoneyInfo(self):
        pass

    def setTotalAssetsInfo(self):
        pass

    def setGoldenKeyInfo(self):
        pass

class GameInit():
    def __init__(self,playerNum):

        root = Tk()
        root.resizable(False,False)
        root.state('zoomed')

        playerNum = playerNum

        left_Frame = Frame(root)  # 왼쪽 프레임
        # left_Frame.pack(side = "left", expand = True,fill = 'both')
        left_Frame.pack(side = "left",fill = 'both')

        right_frame = Frame(root) # 오른쪽 프레임
        # right_frame.pack(side = 'right', expand = True,fill = 'both')
        right_frame.pack(side = 'right',fill = 'both')

        l_top_frame = Frame(left_Frame) # 왼쪽 위 프레임
        # l_top_frame.pack(side = 'top', expand = True,fill = 'both')
        l_top_frame.pack(side = 'top',fill = 'both')

        l_bototm_frame = Frame(left_Frame)  # 왼쪽 아래 프레임
        # l_bototm_frame.pack(side = 'bottom', expand = True,fill = 'both')
        l_bototm_frame.pack(side = 'bottom',fill = 'both')

        r_top_frame = Frame(right_frame)    # 오른쪽 위 프레임
        # r_top_frame.pack(side = 'top', expand = True,fill = 'both')
        r_top_frame.pack(side = 'top', fill = 'both')

        r_bottom_frame = Frame(right_frame) # 오른쪽 아래 프레임
        # r_bottom_frame.pack(side = 'bottom', expand = True,fill = 'both')
        r_bottom_frame.pack(side = 'bottom',fill = 'both')

        if playerNum >= 2:
            self.player1 = PlayerInfo(l_top_frame, "player1", '#FF7F50')
            self.player2 = PlayerInfo(r_top_frame, "player2", '#00FFFF')

            if playerNum >= 3:
                self.player3 = PlayerInfo(l_bototm_frame, "player3", '#FFD700')

                if playerNum >= 4:
                    self.player4 = PlayerInfo(r_bottom_frame, "player4",'#ADFF2F')


def start(playerNum):
    # 초기화
    # url = "15.165.88.215:8080/init"
    # res = requests.get(url)
    GameInit(playerNum)