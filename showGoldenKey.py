from tkinter import *
import tkinter.font as tkfont
import requests

bg_color = "#B85D5D"

isStorage = False   # 보관할 지 말 지 변수 False = 버리기, True = 보관

def yesButton(root):
    global isStorage
    isStorage = True

    root.destroy()

def noButton(root):
    global isStorage
    isStorage = False

    root.destroy()

def showGoldenKey(id, name, content):

    global isStorage

    if id == 5:
        name = name +"(제주도)"
    if id == 13:
        name = name +"(부산)"
    if id == 16:
        name = name +"(서울)"
    w = 400
    h = 600

    x = (1920 - w) // 2
    y = (1080 - h) // 2
    root = Tk()
    root.title(name)
    root.resizable(False, False)
    root.geometry("{}x{}+{}+{}".format(w,h,x,y))

    font = tkfont.Font(size=20, family = "malgun gothic")

    boarder = Frame(root,padx = 10, pady = 10, bg = "#FFD15A")
    boarder.pack(fill = "both", expand = True)

    frame = Frame(boarder, bg = bg_color, pady = 10)
    frame.pack(fill = "both", expand = True)

    KeyName = Label(frame, text = "    " + name + "    ", bg = "#FFD15A",fg = "white", font = font)
    KeyName.pack(side = "top")

    image = PhotoImage(file="goldenKeyImages/{}.png".format(name), master=root)
    KeyImage = Label(frame, bg = bg_color)
    KeyImage.configure(image=image, borderwidth=0)
    KeyImage.image = image
    KeyImage.pack(side = "top", pady = 10)

    font = tkfont.Font(size=10, family="malgun gothic")
    contentLabel = Label(frame, text = content, bg = bg_color, font = font, fg = "white")
    contentLabel.pack()

    buttonFrame = Frame(frame, bg = bg_color)
    buttonFrame.pack(side = "bottom", pady = 10)

    if name == "우대권" or name == "무인도 탈출":
        image = PhotoImage(file="goldenKeyImages/keeping.png", master=root)
        yesBtn = Button(buttonFrame, command = lambda : yesButton(root), image = image, bg = bg_color, borderwidth=0, activebackground= bg_color)
        yesBtn.image = image
        yesBtn.pack(side="right", padx=10)

        image = PhotoImage(file="goldenKeyImages/throw.png", master=root)
        noBtn = Button(buttonFrame, command = lambda : noButton(root), image = image, bg = bg_color, borderwidth=0, activebackground= bg_color)
        noBtn.image = image
        noBtn.pack(side = "left", padx = 10)

    else:
        chkBtn = Button(buttonFrame, text = "확인", font = font, fg = "white", bg = "#FFD43A", command = lambda : noButton(root), width = 10, height = 2)
        chkBtn.pack()

    root.mainloop()

    return isStorage

if __name__ == "__main__":
    while True:
        req = requests.get("http://15.165.88.215:8888/key/1").json()
        showGoldenKey(req["key_id"], req["title"], req["command"])