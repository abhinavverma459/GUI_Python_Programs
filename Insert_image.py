import tkinter
from tkinter import *
# create screen
t=tkinter.Tk()
# size of the window
t.geometry('750x750')

C=Canvas(t,width=550,height=550,bg='pink')
C.place(x=20,y=20)
# used to insert image
pg=PhotoImage(file='image2.gif')
C.create_image(450,500,image=pg)

# title of the screen / Page
t.title('My first screen')
# make screen visible
t.mainloop()