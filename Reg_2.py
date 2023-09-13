import tkinter
from tkinter import *
# Create Screen
t=tkinter.Tk()
# Size of the window
t.geometry("1920x1080")

# Background colour of the window
t.config(bg='green')

# Title of the window
t.title("Registration Module")

# To make half bg in red colore
c=Canvas(t,width=1000,height=100,bg="red")
c.place(x=120,y=0)

# To create a rectangle
c.create_rectangle(380,30,580,80,fill="Yellow",width=5)

# To write in the rectangle 
a=Label(t,text="REGISTRATION FORM")
a.place(x=535,y=45)

# for Course
b=Label(t,text="1. Course")
b.place(x=30,y=150)
c=Entry(t,width=30)
c.place(x=115,y=150)

# for Branch
d=Label(t,text="2. Branch")
d.place(x=320,y=150)
e=Entry(t,width=30)
e.place(x=390,y=150)

# for year
f=Label(t,text="3. Year")
f.place(x=600,y=150)
g=Entry(t,width=30)
g.place(x=670,y=150)

# for Semester
h=Label(t,text="4. Semester")
h.place(x=880,y=150)
i=Entry(t,width=30)
i.place(x=960,y=150)

# for Roll.no
j=Label(t,text="5. Roll.no.")
j.place(x=30,y=200)
k=Entry(t,width=70)
k.place(x=115,y=200)

# for Enrollment number
b=Label(t,text="6. Enrollment.no.")
b.place(x=600,y=200)
c=Entry(t,width=70)
c.place(x=715,y=200)

# for name of student
d=Label(t,text="7. Name of Student :")
d.place(x=30,y=250)
f=Label(t,text="In English")
f.place(x=30,y=300)
e=Entry(t,width=30)
e.place(x=160,y=300)

# for mother's name
d=Label(t,text="8. Mother's Name :")
d.place(x=30,y=350)
e=Entry(t,width=30)
e.place(x=160,y=350)

# for father's name
d=Label(t,text="9. Father's Name :")
d.place(x=30,y=400)
e=Entry(t,width=30)
e.place(x=160,y=400)

# for Address
d=Label(t,text="10. Postal Address :")
d.place(x=30,y=450)
e=Entry(t,width=70)
e.place(x=160,y=450)

# for PINCODE
d=Label(t,text="PIN CODE :")
d.place(x=600,y=450)
e=Entry(t,width=30)
e.place(x=710,y=450)





t.mainloop()
