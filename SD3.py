import tkinter 
from tkinter import *
from tkinter import ttk
import pymysql

lis=tkinter.Tk()
lis.geometry("500x250+50+370")
lis.title("SHOW DATABASE")
lis.iconbitmap('LOGO.ico')

db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
cur=db.cursor()
sql="select * from slibrary"
cur.execute(sql)
     
my_tree=ttk.Treeview(lis)

#define columns
my_tree['columns']=("Student_Id","Book_Id","Issue_Date","Place")

#formate our columns
my_tree.column('#0',width=0,stretch=NO)
my_tree.column("Student_Id",anchor=W,width=80)
my_tree.column("Book_Id",anchor=W,width=80)
my_tree.column("Issue_Date",anchor=W,width=100)
my_tree.column("Place",anchor=W,width=150)



#create headings
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("Student_Id",text="Student Id",anchor=W)
my_tree.heading("Book_Id",text="Book Id",anchor=W)
my_tree.heading("Issue_Date",text="Issue Date",anchor=W)
my_tree.heading("Place",text="Place",anchor=W)



count=0
for record in cur:
    my_tree.insert(parent='',index='end',iid=count, text="",values=(record[0],record[1],record[2],record[3]))
    count += 1
    
hsb=ttk.Scrollbar(lis,orient="horizontal")
hsb.configure(command=my_tree.xview)
my_tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X,side=BOTTOM)

vsb=ttk.Scrollbar(lis,orient="vertical")
vsb.configure(command=my_tree.yview)
my_tree.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y,side=RIGHT)

my_tree.pack(padx=20,pady=50)

lis.mainloop()