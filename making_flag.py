import tkinter
from tkinter import *
# create screen
t=tkinter.Tk()
# size of the window
t.geometry('750x750')

C=Canvas(t,width=600,height=600,bg='pink')
C.place(x=20,y=20)
# to create a Flag


C.create_line(200,100,200,500,width='5',fill='black')

C.create_line(200,100,400,100,width='5',fill='black')

C.create_line(200,125,400,125,width='5',fill='black')

C.create_line(200,150,400,150,width='5',fill='black')

C.create_line(200,175,400,175,width='5',fill='black')

C.create_line(400,100,400,175,width='5',fill='black')

C.create_line(150,500,250,500,width='5',fill='black')

C.create_line(150,500,150,525,width='5',fill='black')

C.create_line(250,500,250,525,width='5',fill='black')

C.create_line(100,525,300,525,width='5',fill='black')

C.create_line(100,525,100,550,width='5',fill='black')

C.create_line(300,525,300,550,width='5',fill='black')

C.create_line(75,550,325,550,width='5',fill='black')

C.create_line(75,575,325,575,width='5',fill='black')

C.create_line(75,550,75,575,width='5',fill='black')

C.create_line(325,550,325,575,width='5',fill='black')


# title of the screen / Page
t.title('My first screen')
# make screen visible
t.mainloop()
