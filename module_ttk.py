import tkinter
from tkinter import *
from tkinter import ttk

t=tkinter.Tk()
t.geometry("750x750")
t.title("module ttk")

a=Label(t,text="City")
a.place(x=30,y=50)

lt=['Noida','Delhi','Pune','Chennai']
cb=ttk.Combobox(t)
cb['values']=lt
cb.place(x=250,y=50)

pr=ttk.Progressbar(t)
pr['value']=50
pr.place(x=50,y=120)







t.mainloop()