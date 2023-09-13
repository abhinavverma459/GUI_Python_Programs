import tkinter
from tkinter import *
# create screen
t=tkinter.Tk()
# size of the window
t.geometry('750x750')

C=Canvas(t,width=550,height=550,bg='pink')
C.place(x=20,y=20)

C.create_rectangle(100,350,200,400,fill='yellow',width='5')
# title of the screen / Page
t.title('My first screen')
# make screen visible
t.mainloop()