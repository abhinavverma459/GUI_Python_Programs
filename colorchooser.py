import tkinter
from tkinter import *
from tkinter import colorchooser
t=tkinter.Tk()
t.title("Simple")
t.geometry("1080x1080")

# to change color of bg
def change():
    x=colorchooser.askcolor()
    t.config(bg=x[1])

a=Button(t,text="Hello",font=5,command=change)
a.place(x=500,y=200)

t.mainloop()