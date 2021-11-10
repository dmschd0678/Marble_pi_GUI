from tkinter import *

def gameOver(player):
    w = 700
    h = 400
    x = (1920 - w) // 2
    y = (1080 - h) // 2
    root = Tk()
    root.title("GameOver")
    root.resizable(False, False)
    root.geometry("{}x{}+{}+{}".format(w, h, x, y))

    frame = Frame(root,bg = "white")
    frame.pack(fill = "both", expand = True)
    frame.pack()
    image = PhotoImage(file = "images/winner{}.png".format(player + 1))
    imageLabel = Label(frame, image = image, bg = "white")
    imageLabel.image = image

    imageLabel.pack()
    root.mainloop()


if __name__ == "__main__":
    gameOver(0)