from tkinter import *
import tkinter.ttk as ttk

class game():

    def __init__(self,playerNum):
        self._root = Tk()
        self._root.resizable(False,False)
        self._root.state('zoomed')
        self._playerNum = int(playerNum.replace("명",""))

class player():
    def __init__(self):
        self._money = 1000
        self._goldenKey = []
        self._property = self._money

    def buy(self):
        pass

    def pay(self):
        pass

