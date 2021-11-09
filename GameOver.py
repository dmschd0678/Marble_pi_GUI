from tkinter import *
import tkinter.font as tkfont

bg_color = "yellow"

def gameOver(player, name, color):
    w = 500
    h = 300
    x = (1920 - w) // 2
    y = (1080 - h) // 2
    root = Tk()
    root.title("GameOver")
    root.resizable(False, False)
    root.geometry("{}x{}+{}+{}".format(w, h, x, y))

    font = tkfont.Font(size=30, family="malgun gothic")

    frame = Frame(root, bg = bg_color)
    frame.pack(expand = True, fill = "both")

    text = Label(frame, text = "WINNER IS {}!".format(name), font = font, bg = bg_color, fg = color)
    text.pack()

    image = PhotoImage(file = "FirstPlayer/{}.png".format(player))
    imageLabel = Label(frame, image = image)
    imageLabel.image = image
    imageLabel.pack(pady = 50)

    root.mainloop()


if __name__ == "__main__":
    gameOver(0, "EMMA", "#FF5A5A")