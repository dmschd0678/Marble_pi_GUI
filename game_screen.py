from tkinter import *
import tkinter.font as tkfont
import requests


class Player():
    def __init__(self):
        self.money = 1000
        self.goldenKey = []
        self.total_assets = self.money

class PlayerInfo():


    def __init__(self, frame, name, color):
        font = tkfont.Font(size=30)

        self.player = Player()

        self.playerName = Label(frame, text = name, bg = color, font = font)
        self.playerName.pack(fill='x', side='top',anchor = "n")

        self.__moneyInfo = Label(frame, text = "보유 돈 : " +  str(self.player.money), bg = color, font = font)
        self.__moneyInfo.pack(fill = 'x', side = 'top',anchor = "n")

        self.__totalAssetsInfo = Label(frame, text = "총 자산 : " + str(self.player.total_assets), bg = color, font = font)
        self.__totalAssetsInfo.pack(fill = 'x', side = 'top', anchor = 'n')

        self.__goldenKeyInfo = Label(frame, text = "보유 황금열쇠 : " + str([i for i in self.player.goldenKey]), bg = color, font = font)
        self.__goldenKeyInfo.pack(fill = 'x', side = 'top',anchor = "n")

    @property
    def moneyInfo(self):
        return self.__moneyInfo

    @moneyInfo.setter
    def moneyInfo(self, money):
        self.__moneyInfo.set(money)

    @property
    def totalAssetsInfo(self):
        return self.__totalAssetsInfo

    @totalAssetsInfo.setter
    def totalAssetsInfo(self,value):
        self.__totalAssetsInfo.set("value")


class GameState():

    def __init__(self,playerNum):

        self._root = Tk()
        self._root.resizable(False,False)
        self._root.state('zoomed')

        self._playerNum = playerNum

        left_Frame = Frame(self._root)  # 왼쪽 프레임
        # left_Frame.pack(side = "left", expand = True,fill = 'both')
        left_Frame.pack(side = "left",fill = 'both')

        right_frame = Frame(self._root) # 오른쪽 프레임
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

        if self._playerNum >= 2:
            self.player1 = PlayerInfo(l_top_frame, "player1", '#FF7F50')
            self.player2 = PlayerInfo(r_top_frame, "player2", '#00FFFF')

            if self._playerNum >= 3:
                self.player3 = PlayerInfo(l_bototm_frame, "player3", '#FFD700')

                if self._playerNum >= 4:
                    self.player4 = PlayerInfo(r_bottom_frame, "player4",'#ADFF2F')


def start(playerNum):
    GameState(playerNum)
