import tkinter
from tkinter import *
t=tkinter.Tk()
t.title("Simple")
t.geometry("1080x1080")

def one():
    x=Toplevel(t)
    x.geometry("200x400")
    
    a=Label(x,text="Name")
    a.place(x=10,y=10)
    x.mainloop()
    
def Two():
    y=Toplevel(t)
    y.geometry("200x400")
    
    b=Label(y,text="Class")
    b.place(x=10,y=10)
    y.mainloop()



a=Button(t,text="first",font=5,command=one)
a.place(x=500,y=200)

b=Button(t,text="second",font=5,command=Two)
b.place(x=600,y=200)

t.mainloop()