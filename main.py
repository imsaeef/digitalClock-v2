from tkinter import *
import time

#create object
root = Tk()

#create window
root.geometry("640x400+400+80")
root.title("Digital clock v2")
root.config(bg="#242B2E")
root.iconbitmap("img/clk.ico")
root.resizable(0,0)


#title label
titleLabel = Label(root, text="SAEEF Digital Clock v2", font="exo 25 bold", bg="#242B2E", fg="darkcyan", bd=0)
titleLabel.place(x=0, y=40, width=640)


#logic or functions
def clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    AmPm = time.strftime("%p")
    labelH.config(text=hours)
    labelM.config(text=minutes)
    labelS.config(text=seconds)
    labelAmPm.config(text=AmPm)
    
    labelS.after(1000, clock)


#create 4 frame
frame1 = Frame(root, height=100, width=100, bg="#FFB5B5")
frame1.place(x=100, y=170)
frame2 = Frame(root, height=100, width=100, bg="#FF7272")
frame2.place(x=210, y=170)
frame3 = Frame(root, height=100, width=100, bg="#9B0000")
frame3.place(x=320, y=170)
frame4 = Frame(root, height=100, width=100, bg="#000B49")
frame4.place(x=430, y=170)


#create time label
labelH = Label(frame1, text="12", font="DS-Digital 45 bold", bg="#FFB5B5", fg="#FFFFFF", bd=0)
labelH.place(height=100, width=100)
labelM = Label(frame2, text="12", font="DS-Digital 45 bold", bg="#FF7272", fg="#FFFFFF", bd=0)
labelM.place(height=100, width=100)
labelS = Label(frame3, text="12", font="DS-Digital 45 bold", bg="#9B0000", fg="#FFFFFF", bd=0)
labelS.place(height=100, width=100)
labelAmPm = Label(frame4, text="PM", font="DS-Digital 45 bold", bg="#000B49", fg="#FFFFFF", bd=0)
labelAmPm.place(height=100, width=100)

#create frame name
hour = Label(root, text="HOURS", font="exo 10 bold", bg="#242B2E", fg="#FFB5B5", bd=0)
hour.place(x=130, y=280)
minute = Label(root, text="MINUTES", font="exo 10 bold", bg="#242B2E", fg="#FF7272", bd=0)
minute.place(x=230, y=280)
second = Label(root, text="SECONDS", font="exo 10 bold", bg="#242B2E", fg="#9B0000", bd=0)
second.place(x=340, y=280)
timeFormat = Label(root, text="FORMAT", font="exo 10 bold", bg="#242B2E", fg="#000B49", bd=0)
timeFormat.place(x=455, y=280)

# call time function
clock()
#execute window
root.mainloop()