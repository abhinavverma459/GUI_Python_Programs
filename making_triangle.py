import tkinter
from tkinter import *
# create screen
t=tkinter.Tk()
# size of the window
t.geometry('750x750')

C=Canvas(t,width=550,height=550,bg='pink')
C.place(x=20,y=20)

p=[50,250,300,50,400,250]
C.create_polygon(p,fill='yellow')


# title of the screen / Page
t.title('My first screen')
# make screen visible
t.mainloop()