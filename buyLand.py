from tkinter import *
import tkinter.font as tkfont

bg_color = "#B85D5D"
color = "#F3CF98"

building = ['villa', 'building', "hotel"]

is_buy = False

def yesButton(window):
    global is_buy
    is_buy = True
    window.destroy()

def noButton(window):
    global is_buy
    is_buy = False
    window.destroy()

def buyLand(name, buildingNum, pay):

    w = 400
    h = 600

    x = (1920 - w) // 2
    y = (1080 - h) // 2
    root = Tk()
    root.title(name)
    root.resizable(False, False)
    root.geometry("{}x{}+{}+{}".format(w, h, x, y))

    font = tkfont.Font(size=20, family="malgun gothic")

    boarder = Frame(root, padx=10, pady=10, bg=color)
    boarder.pack(fill="both", expand=True)

    frame = Frame(boarder, bg=bg_color, pady=10)
    frame.pack(fill="both", expand=True)

    KeyName = Label(frame, text="    " + name + "    ", bg= color, fg="white", font=font)
    KeyName.pack(side="top")

    image = PhotoImage(file = "Building/{}.png".format(building[buildingNum]))

    buildingImage = Label(frame, bg = bg_color, image = image)
    buildingImage.image = image
    buildingImage.pack(side = "top")

    font = tkfont.Font(size=15, family="malgun gothic")
    contentLabel = Label(frame, text="건설 비용 -> {}".format(pay), bg="#616161", font=font, fg="white")
    contentLabel.pack()

    image = PhotoImage(file="Building/close.png")
    noBtn = Button(frame, command=lambda: noButton(root), image=image, bg=bg_color, borderwidth=0,activebackground=bg_color)
    noBtn.image = image
    noBtn.pack()

    image = PhotoImage(file="Building/close.png")
    yesBtn = Button(frame, command = lambda : noButton(root), image = image, bg = bg_color, borderwidth=0, activebackground= bg_color)
    yesBtn.image = image
    yesBtn.pack()

    root.mainloop()

    return is_buy
if __name__ == "__main__":
    buyLand("런던", 1, 1000)