import tkinter
from tkinter import *
# create screen
t=tkinter.Tk()
# size of the window
t.geometry("750x750")
t.title("My first screen")
# for refistration
a=Label(t,text="Registration Form",font=('arial',30),fg="blue")
a.place(x=350,y=20)
# for name

b=Label(t,text="Name")
b.place(x=30,y=60)

#for Entery
c=Entry(t,width=30)
c.place(x=250,y=60)

#for Address
d=Label(t,text="Password")
d.place(x=30,y=100)

#for Entery
e=Entry(t,width=30,show='*')
e.place(x=250,y=100)

# for gender
f=Label(t,text="Gender")
f.place(x=30,y=140)

# for radio buttons
x=IntVar()
rm=Radiobutton(t,text="Male",variable=x,value=1)
rf=Radiobutton(t,text="Female",variable=x,value=0)
rm.place(x=250,y=140)
rf.place(x=350,y=140)

# for hobbies
g=Label(t,text="Hobbies")
g.place(x=30,y=180)

# check button
p=IntVar()
r=IntVar()
cs=Checkbutton(t,text="Sport",variable=p,onvalue=1,offvalue=0)
cm=Checkbutton(t,text="Music",variable=r,onvalue=1,offvalue=0)
cs.place(x=250,y=180)
cm.place(x=350,y=180)

# for qualification
h=Label(t,text="Qualification")
h.place(x=30,y=220)

# for list box
lt=Listbox(t,height=3)
lt.insert(1,"BTECH")
lt.insert(2,"BSC")
lt.insert(3,"BCOM")
lt.insert(4,"BA")
lt.place(x=250,y=220)

# for Age
j=Label(t,text='Age')
j.place(x=30,y=300)

# for spinbox
sp=Spinbox(t,from_=1,to=150)
sp.place(x=250,y=300)

# for scale
k=Label(t,text="Range")
k.place(x=30,y=340)
sc=Scale(t,from_=1,to=20,orient=HORIZONTAL)
sc.place(x=250,y=340)
bt=Button(t,text="Save")
bt.place(x=130,y=380)
btc=Button(t,text="Cancel")
btc.place(x=250,y=380)








t.mainloop()