import tkinter
from tkinter import *
# create screen
t=tkinter.Tk()
# size of the window
t.geometry('750x750')

C=Canvas(t,width=600,height=600,bg='pink')
C.place(x=20,y=20)
# to create a star
C.create_line(100,100,70,150,width='2',fill='red')

C.create_line(100,100,130,150,width='2',fill='blue')

C.create_line(130,150,180,150,width='2',fill='green')

C.create_line(70,150,20,150,width='2',fill='yellow')

C.create_line(20,150,70,180,width='2',fill='orange')

C.create_line(180,150,130,180,width='2',fill='black')

C.create_line(70,180,45,220,width='2',fill='white')

C.create_line(130,180,160,220,width='2',fill='brown')

C.create_line(45,220,100,190,width='2',fill='grey')

C.create_line(160,220,100,190,width='2',fill='purple')

# title of the screen / Page
t.title('My first screen')
# make screen visible
t.mainloop()
