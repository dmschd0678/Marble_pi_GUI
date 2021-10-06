from tkinter import *
import tkinter.ttk as ttk
import game_screen

def create_window():
    game_screen.game(combobox.get())

window = Tk()
window.title("Mable.pi")
# window.state("zoomed")
window.resizable(False,False)

startFrame = Frame(window)
startFrame.pack(fill = 'both')


label = Label(startFrame, text = "사람 수")
label.pack()

players = [str(i + 2) + "명" for i in range(4)]

combobox = ttk.Combobox(startFrame, height = 3,values = players, state = "readonly", width = 30)
combobox.current(0)
combobox.pack()

button = Button(startFrame, text = "시작", command = lambda : create_window())
button.pack()

window.mainloop()