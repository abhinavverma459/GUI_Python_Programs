import tkinter 
from tkinter import *
from tkinter import ttk
import pymysql

sd=tkinter.Tk()
sd.geometry("1270x250+0+0")
sd.title("SHOW DATABASE")
sd.iconbitmap('LOGO.ico')

db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
cur=db.cursor()
sql="select * from teachers"
cur.execute(sql)
     
my_tree=ttk.Treeview(sd)

#define columns
my_tree['columns']=("Teacher_Id","Teacher_Name","DOB","Teacher_Mobile_No","Teacher_Email_Id","Aadhar_No","Tenth_Year","Twelfth_Year","Graduation_Year","Father_Name","Mother_Name","Father_Mobile_No","Father_Email_Id","Mother_Mobile_No","Address","Pincode","Joining_Date","Department","Salary","Password")

#formate our columns
my_tree.column('#0',width=0,stretch=NO)
my_tree.column("Teacher_Id",anchor=W,width=80)
my_tree.column("Teacher_Name",anchor=W,width=105)
my_tree.column("DOB",anchor=W,width=60)
my_tree.column("Teacher_Mobile_No",anchor=W,width=100)
my_tree.column("Teacher_Email_Id",anchor=W,width=200)
my_tree.column("Aadhar_No",anchor=W,width=100)
my_tree.column("Tenth_Year",anchor=W,width=70)
my_tree.column("Twelfth_Year",anchor=W,width=80)
my_tree.column("Graduation_Year",anchor=W,width=80)
my_tree.column("Father_Name",anchor=W,width=105)
my_tree.column("Mother_Name",anchor=W,width=105)
my_tree.column("Father_Mobile_No",anchor=W,width=100)
my_tree.column("Father_Email_Id",anchor=W,width=200)
my_tree.column("Mother_Mobile_No",anchor=W,width=100)
my_tree.column("Address",anchor=W,width=100)
my_tree.column("Pincode",anchor=W,width=100)
my_tree.column("Joining_Date",anchor=W,width=100)
my_tree.column("Department",anchor=W,width=100)
my_tree.column("Salary",anchor=W,width=100)
my_tree.column("Password",anchor=W,width=100)

#create headings
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("Teacher_Id",text="Teacher Id",anchor=W)
my_tree.heading("Teacher_Name",text="Teacher Name",anchor=W)
my_tree.heading("DOB",text="DOB",anchor=W)
my_tree.heading("Teacher_Mobile_No",text="Teacher No",anchor=W)
my_tree.heading("Teacher_Email_Id",text="Teacher Email",anchor=W)
my_tree.heading("Aadhar_No",text="Aadhar No",anchor=W)
my_tree.heading("Tenth_Year",text="Tenth year",anchor=W)
my_tree.heading("Twelfth_Year",text="Twelfth year",anchor=W)
my_tree.heading("Graduation_Year",text="Graduation Year",anchor=W)
my_tree.heading("Father_Name",text="Father Name",anchor=W)
my_tree.heading("Mother_Name",text="Mother Name",anchor=W)
my_tree.heading("Father_Mobile_No",text="Father No",anchor=W)
my_tree.heading("Father_Email_Id",text="Father Email",anchor=W)
my_tree.heading("Mother_Mobile_No",text="Mother No",anchor=W)
my_tree.heading("Address",text="Address",anchor=W)
my_tree.heading("Pincode",text="Pincode",anchor=W)
my_tree.heading("Joining_Date",text="Joining Date",anchor=W)
my_tree.heading("Department",text="Department",anchor=W)
my_tree.heading("Salary",text="Salary",anchor=W)
my_tree.heading("Password",text="Password",anchor=W)

count=0
for record in cur:
    my_tree.insert(parent='',index='end',iid=count, text="",values=(record[0],record[1],record[2],record[3],record[4],record[5],
    record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17],record[18],record[19]))
    count += 1
    
hsb=ttk.Scrollbar(sd,orient="horizontal")
hsb.configure(command=my_tree.xview)
my_tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X,side=BOTTOM)

vsb=ttk.Scrollbar(sd,orient="vertical")
vsb.configure(command=my_tree.yview)
my_tree.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y,side=RIGHT)

my_tree.pack(padx=20,pady=50)

sd.mainloop()