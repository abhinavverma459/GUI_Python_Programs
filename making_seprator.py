import tkinter
from tkinter import *
t=tkinter.Tk()
t.geometry("750x750")
t.title("File edit format")

mb=Menu()
fm=Menu()
em=Menu()
form=Menu()

fm.add_command(label='New')
fm.add_separator()
fm.add_command(label='Open')
fm.add_separator()
fm.add_command(label='Save')
fm.add_separator()
fm.add_command(label='Exit')
fm.add_separator()
mb.add_cascade(menu=fm,label='File')

em.add_command(label='Cut')
em.add_separator()
em.add_command(label='Copy')
em.add_separator()
em.add_command(label='Paste')
em.add_separator()
mb.add_cascade(menu=em,label='Edit')

form.add_command(label='Font')
form.add_separator()
form.add_command(label='Colour')
form.add_separator()
mb.add_cascade(menu=form,label='Format')


t.config(menu=mb)















t.mainloop()