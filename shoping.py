import tkinter
from tkinter import *
t=tkinter.Tk()
t.geometry("750x750")
t.title("Login Page")

def calc():
    x=int(a.get())
    y=int(sp.get())
    z=x*y
    b.delete(0,100)
    b.insert(0,str(z))
    

a=Entry(t,width=30)
a.place(x=250,y=50)
sp=Spinbox(t,from_=1,to=50,command=calc)
sp.place(x=250,y=100)
b=Entry(t,width=30)
b.place(x=250,y=150)


t.mainloop()