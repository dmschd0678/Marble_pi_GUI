from tkinter import *
import tkinter.ttk as ttk
import game_screen

class ChoosePlayerNum():
    def __init__(self):
        self.window = Tk()
        self.window.title("Mable.py")
        self.window.resizable(False,False)

        startFrame = Frame(self.window)
        startFrame.pack(fill = 'both')


        label = Label(startFrame, text = "사람 수")
        label.pack()

        players = [str(i + 2) + "명" for i in range(4)]

        self.combobox = ttk.Combobox(startFrame, height = 3,values = players, state = "readonly", width = 30)
        self.combobox.current(0)
        self.combobox.pack()

        button = Button(startFrame, text = "시작", command = self.create_window)
        button.pack()

        self.window.mainloop()

    def create_window(self):
        game_screen.start(int(self.combobox.get().replace("명", "")))
        self.window.destroy()

if __name__ == '__main__':
    choosePlayer = ChoosePlayerNum()