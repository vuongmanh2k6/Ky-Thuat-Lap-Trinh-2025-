import tkinter
import random

# danh sách màu
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']

score = 0
timeleft = 120   # thời gian chơi


# bắt đầu game
def startGame(event):
    global timeleft
    if timeleft == 120:
        countdown()
        nextColour()


# chọn màu tiếp theo
def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()

        # kiểm tra kết quả
        if e.get().lower() == colours[1].lower():
            score += 2      # đúng +2 điểm
        else:
            if e.get() != "":
                score -= 1  # sai -1 điểm

        e.delete(0, tkinter.END)

        random.shuffle(colours)

        # cập nhật chữ + màu
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # cập nhật điểm
        scoreLabel.config(text="Điểm: " + str(score))


# đếm ngược thời gian
def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Thời gian còn lại: " + str(timeleft))
        timeLabel.after(1000, countdown)


# tạo giao diện
root = tkinter.Tk()
root.title("TRÒ CHƠI MÀU SẮC")
root.geometry("450x260")

instructions = tkinter.Label(root,
                             text="Hãy nhập *màu sắc* của chữ, không phải nội dung chữ!",
                             font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Nhấn Enter để bắt đầu",
                           font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Thời gian còn lại: " + str(timeleft),
                          font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root, font=('Helvetica', 14))
e.pack()

root.bind('<Return>', startGame)
e.focus_set()

root.mainloop()
