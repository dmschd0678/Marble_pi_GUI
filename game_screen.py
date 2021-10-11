from tkinter import *

class game():

    def __init__(self,playerNum):

        self._root = Tk()
        self._root.resizable(False,False)
        self._root.state('zoomed')
        self._playerNum = int(playerNum.replace("명",""))

        left_Frame = Frame(self._root)
        left_Frame.pack(side = "left", expand = True,fill = 'both')

        right_frame = Frame(self._root)
        right_frame.pack(side = 'right', expand = True,fill = 'both')

        l_top_frame = Frame(left_Frame)
        l_top_frame.pack(side = 'top', expand = True,fill = 'both')

        l_bototm_frame = Frame(left_Frame)
        l_bototm_frame.pack(side = 'bottom', expand = True,fill = 'both')

        r_top_frame = Frame(right_frame)
        r_top_frame.pack(side = 'top', expand = True,fill = 'both')

        r_bottom_frame = Frame(right_frame)
        r_bottom_frame.pack(side = 'bottom', expand = True,fill = 'both')

        if playerNum == 2:
            pass


class player():
    def __init__(self):
        self._money = 1000
        self._goldenKey = []
        self._property = self._money

    def buy(self, price):
        pass

    def pay(self, price):
        pass

