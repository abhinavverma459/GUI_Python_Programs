import tkinter
from tkinter import *
t=tkinter.Tk()
t.geometry('800x800')
def first():
    c3=Canvas(t,height=800,width=650,bg='yellow')
    c3.place(x=160,y=10)
    a=Label(c3,text='Name',fg='blue')
    a.place(x=100,y=50)
    b=Entry(c3,width=30)
    b.place(x=350,y=50)
    
c1=Canvas(t,height=800,width=150,bg='black')
c1.place(x=10,y=10)
b1=Button(c1,text='Insert',bg='black',fg='yellow',font=(18),command=first)
b1.place(x=10,y=20)
c2=Canvas(t,height=800,width=650,bg='red')
c2.place(x=160,y=10)

t.mainloop()