#from tkinter import *
import tkinter
from time import strftime

def tym():
    t = strftime("%H:%M:%S %p")
    lbl.config(text = t)
    lbl.pack()

    lbl.after(500 ,tym)
    pass

clock =  tkinter.Tk()
clock.title("The time is:")
clock.geometry("400x200")
clock.config(bg='black')


lbl_2 = tkinter.Button(clock, text ="Click" , fg = "red", font = ("Cosmic Sans MS",40,"bold")).pack()
lbl= tkinter.Label(clock,bg="black",fg="purple",height="10",font= ('Comic Sans MS',50,'bold'))
tym()
clock.mainloop()
