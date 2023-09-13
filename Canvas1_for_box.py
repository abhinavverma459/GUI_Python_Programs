import tkinter
from tkinter import *
# create screen
t=tkinter.Tk()
# size of the window
t.geometry('750x750')

C=Canvas(t,width=600,height=600,bg='pink')
C.place(x=20,y=20)
# to create a vetical line
C.create_line(100,100,200,220,width='5',fill='red')
# to create a straight line
C.create_line(50,220,300,220,width='5',fill='blue')

C.create_line(300,220,300,400,width='5',fill='green')


# title of the screen / Page
t.title('My first screen')
# make screen visible
t.mainloop()
