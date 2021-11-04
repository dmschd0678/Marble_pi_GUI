from tkinter import *
import tkinter.font as tkfont

bg_color = "#B85D5D"
color = "#F3CF98"

building = ['villa', 'building', "hotel"]

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

    buildingImage = Label(frame, bg = bg_color)
    buildingImage.image = image
    buildingImage.pack(side = "top")

    font = tkfont.Font(size=15, family="malgun gothic")
    contentLabel = Label(frame, text="건설 비용 -> {}".format(pay), bg=bg_color, font=font, fg="white")
    contentLabel.pack()

    root.mainloop()
if __name__ == "__main__":
    buyLand("런던")