from tkinter import *
import tkinter.font as tkfont

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

def showGoldenKey(keyNum, name, content, type):

    global isStorage

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

    image = PhotoImage(file="goldenKeyImages/{}.png".format(name))
    KeyImage = Label(frame, bg = bg_color)
    KeyImage.configure(image=image, borderwidth=0)
    KeyImage.image = image
    KeyImage.pack(side = "top", pady = 10)

    font = tkfont.Font(size=15, family="malgun gothic")
    contentLabel = Label(frame, text = content, bg = bg_color, font = font, fg = "white")
    contentLabel.pack()

    buttonFrame = Frame(frame, bg = bg_color)
    buttonFrame.pack(side = "bottom", pady = 10)

    if name == "우대권" or name == "무인도 탈출":
        image = PhotoImage(file="goldenKeyImages/keeping.png")
        yesBtn = Button(buttonFrame, command = lambda : yesButton(root), image = image, bg = bg_color, borderwidth=0, activebackground= bg_color)
        yesBtn.image = image
        yesBtn.pack(side="right", padx=10)

        image = PhotoImage(file="goldenKeyImages/throw.png")
        noBtn = Button(buttonFrame, command = lambda : noButton(root), image = image, bg = bg_color, borderwidth=0, activebackground= bg_color)
        noBtn.image = image
        noBtn.pack(side = "left", padx = 10)

    else:
        chkBtn = Button(buttonFrame, text = "확인", font = font, fg = "white", bg = "#FFD43A", command = lambda : noButton(root))
        chkBtn.pack()

    root.mainloop()

    return isStorage

if __name__ == "__main__":
    showGoldenKey(1,"우대권","테스트용 황금열쇠 입니다.", "MOVE")