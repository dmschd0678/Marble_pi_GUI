from tkinter import *
import tkinter.ttk as ttk

class game():

    def __init__(self,playerNum):
        self._root = Tk()
        self._root.resizable(False,False)
        self._root.state('zoomed')
        self._playerNum = int(playerNum.replace("명",""))

        leftFrame = Frame(self._root)
        leftFrame.pack(side = 'left',fill = 'both',expand = True)
        rightFrame = Frame(self._root)
        rightFrame.pack(side = 'right', fill = 'both',expand = True)

        player1 = Label(leftFrame, text = "player1", bg = '#FF7F50')
        player1.pack(fill='both', expand=True, side='top')

        player2 = Label(rightFrame, text="player2", bg = '#00FFFF')
        player2.pack(fill='both', expand=True, side='top')

        player3 = Label(leftFrame, text="player3", bg = '#FFD700')
        player3.pack(fill='both', expand=True, side='bottom')

        player4 = Label(rightFrame, text="player4", bg = '#ADFF2F')
        player4.pack(fill='both', expand=True, side='bottom')

class player():
    def __init__(self):
        self._money = 1000
        self._goldenKey = []
        self._property = self._money

    def buy(self):
        pass

    def pay(self):
        pass

