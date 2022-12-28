import time
from tkinter import *
from time import sleep
import datetime


p1time = 0
p2time = 0
p1 = False
p2 = False
minute = 0
minutep2 = 0


def converterp1(time1):
    global p1time, p1, p2, pl1STR, p2time, minute
    print(f"p1:{minute}/{p1time}")
    minute += 1
    p1time = 0
    while True:
        p1time += 1
        time.sleep(1)
        pl1STR.set(f"{minute}/{p1time}")
        win.update()


def converter2(time2):
    global p1time, p1, p2, pl1STR, p2time, minutep2
    print(f"p1:{minutep2}/{p2time}")
    minutep2 += 1
    p2time = 0
    while True:
        p2time += 1
        time.sleep(1)
        pl12STR.set(f"{minutep2}/{p2time}")
        win.update()


def pl1click():
    global p1time, p1, p2, pl1STR, p2time, minute, pl12STR
    p1 = True
    p2 = False
    while p1 == True:
        time.sleep(1)
        p1time += 1
        pl1STR.set(f"{minute}/{p1time}")

        if p1time == 60:
            converterp1(p1time)

        if p1time == 1/60:
            p1time = 0
            minute = 2
            pl1STR.set(f"{minute}/{p1time}")
        win.update()


def pl2click():
    global p1time, p1, p2, pl1STR, p2time, pl12STR, minutep2
    p1 = False
    p2 = True
    while p2 == True:
        time.sleep(1)
        p2time += 1
        pl12STR.set(f"{minutep2}/{p2time}")

        if p2time == 60:
            converter2(p2time)

        if p2time == 1/60:
            p2time = 0
            minutep2 = 2
            pl12STR.set(f"{minutep2}/{p2time}")
        win.update()


win = Tk()
win.resizable(0, 0)
win.title("timer")
win.geometry("300x400")


pl1STR = StringVar()
pl12STR = StringVar()


player1_l = Label(win, text="player 1", width=10, height=5, bg="#d1d15e")
player1_l.grid(row=0, column=1, padx=105)

timer_l = Label(win, textvariable=pl1STR, width=10, height=3, bg="#d1d15e")
timer_l.grid(row=1, column=1, padx=105)

player1_B = Button(win, text="player 1", width=30, height=3, command=pl1click, bg="#6491d9")
player1_B.grid(row=2, column=1)

player2_B = Button(win, text="player 2", width=30, height=3, command=pl2click, bg="#d15e5e")
player2_B.grid(row=3, column=1)

timer_l2 = Label(win,textvariable=pl12STR, width=10, height=3, bg="#d1d15e")
timer_l2.grid(row=4, column=1)

player2_l = Label(win, text="player 2", width=10, height=5, bg="#d1d15e")
player2_l.grid(row=5, column=1)


win.config(bg="#d1d15e")
win.mainloop()