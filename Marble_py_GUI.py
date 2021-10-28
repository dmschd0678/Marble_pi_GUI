from tkinter import *
import tkinter.ttk as ttk
import game_screen

class ChoosePlayerNum():
    def __init__(self):
        self.window = Tk()
        self.window.title("Mable.py")
        self.window.resizable(False,False)
        self.window.state("zoomed")

        startFrame = Frame(self.window)
        startFrame.pack(fill = 'both')


        label = Label(startFrame, text = "사람 수")
        label.pack()

        frame = Frame()

        players = [str(i + 2) + "명" for i in range(3)]

        self.combobox = ttk.Combobox(startFrame, height = 3,values = players, state = "readonly", width = 30)
        self.combobox.current(0)
        self.combobox.pack()

        button = Button(startFrame, text = "시작", command = self.create_window)
        button.pack()

        self.window.mainloop()

    def create_window(self):
        playerNumber = int(self.combobox.get().replace("명", ""))
        self.window.destroy()
        game_screen.start(playerNumber)

if __name__ == '__main__':
    choosePlayer = ChoosePlayerNum()