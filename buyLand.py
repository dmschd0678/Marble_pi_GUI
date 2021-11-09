from tkinter import *
import tkinter.font as tkfont

bg_color = "#B85D5D"
color = "#F3CF98"

building = ['villa', 'building', "hotel"]
building_kor = ["주택", "빌딩", "호텔"]
special_Land = ["컬럼비아호", "콩코드여객기","퀸 엘리자베스","부산","제주","서울"]

is_buy = False

def yesButton(window):
    global is_buy
    is_buy = True
    window.destroy()

def noButton(window):
    global is_buy
    is_buy = False
    window.destroy()

# 돈 출력 형식
def moneyStr(self, money):
    str = ""
    if money // 100000000 > 1:
        str += f"{money // 100000000}" + "억"
        money %= 100000000
    elif money // 10000 > 1:
        str += f"{money // 10000}" + "만"
        money %= 10000
    elif money % 10000 != 0:
        str += money % 10000
    else:
        str += "0"
    str += "원"
    return str

def buyLand(name, buildingNum, pay):

    w = 400
    h = 600

    x = (1920 - w) // 2
    y = (1080 - h) // 2
    root = Tk()
    root.title(name)
    root.resizable(False, False)
    root.geometry("{}x{}+{}+{}".format(w, h, x, y))

    font = tkfont.Font(size=25, family="malgun gothic")

    boarder = Frame(root, padx=10, pady=10, bg=color)
    boarder.pack(fill="both", expand=True)

    frame = Frame(boarder, bg=bg_color, pady=10)
    frame.pack(fill="both", expand=True)

    KeyName = Label(frame, text="    " + name + "    ", bg= color, fg="white", font=font)
    KeyName.pack(side="top", pady = 10)

    if name in special_Land:
        image = PhotoImage(file = "Building/{}.png".format(name), master=root)

        buildingImage = Label(frame, bg=bg_color, image=image)
        buildingImage.image = image
        buildingImage.pack(side="top", pady=10)

        font = tkfont.Font(size=20, family="malgun gothic")
        contentLabel = Label(frame, text="{}\n건설 비용 -> {}".format(name, moneyStr(pay)), bg="#616161",font=font, fg="white")
        contentLabel.pack(pady=10)

    else:
        image = PhotoImage(file = "Building/{}.png".format(building[buildingNum]), master=root)

        buildingImage = Label(frame, bg=bg_color, image=image)
        buildingImage.image = image
        buildingImage.pack(side="top", pady=10)


        font = tkfont.Font(size=20, family="malgun gothic")
        contentLabel = Label(frame, text="{} 건설\n건설 비용 -> {}".format(moneyStr(pay)), bg="#616161", font=font, fg="white")
        contentLabel.pack(pady = 10)

    image = PhotoImage(file="Building/close.png", master=root)
    noBtn = Button(frame, command=lambda: noButton(root), image=image, bg=bg_color, borderwidth=0,activebackground=bg_color)
    noBtn.image = image
    noBtn.pack(side = "left", padx = 34)

    image = PhotoImage(file="Building/buy.png", master= root)
    yesBtn = Button(frame, command = lambda : yesButton(root), image = image, bg = bg_color, borderwidth=0, activebackground= bg_color)
    yesBtn.image = image
    yesBtn.pack(side = "right", padx = 34)

    root.mainloop()

    return is_buy
if __name__ == "__main__":
    print(buyLand("서울", 2, 1000000))