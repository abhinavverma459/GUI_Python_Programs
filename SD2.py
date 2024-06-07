import tkinter 
from tkinter import *
from tkinter import ttk
import pymysql

lib=tkinter.Tk()
lib.geometry("500x250+750+370")
lib.title("SHOW DATABASE")
lib.iconbitmap('LOGO.ico')

db=pymysql.connect(host='localhost',user='root',password='root',database='scss')
cur=db.cursor()
sql="select * from books"
cur.execute(sql)
     
my_tree=ttk.Treeview(lib)

#define columns
my_tree['columns']=("Book_Id","Book_Name","Author","Edition","Price")

#formate our columns
my_tree.column('#0',width=0,stretch=NO)
my_tree.column("Book_Id",anchor=W,width=80)
my_tree.column("Book_Name",anchor=W,width=150)
my_tree.column("Author",anchor=W,width=200)
my_tree.column("Edition",anchor=W,width=100)
my_tree.column("Price",anchor=W,width=100)


#create headings
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("Book_Id",text="Book Id",anchor=W)
my_tree.heading("Book_Name",text="Book Name",anchor=W)
my_tree.heading("Author",text="Author",anchor=W)
my_tree.heading("Edition",text="Edition",anchor=W)
my_tree.heading("Price",text="Price",anchor=W)


count=0
for record in cur:
    my_tree.insert(parent='',index='end',iid=count, text="",values=(record[0],record[1],record[2],record[3],record[4]))
    count += 1
    
hsb=ttk.Scrollbar(lib,orient="horizontal")
hsb.configure(command=my_tree.xview)
my_tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X,side=BOTTOM)

vsb=ttk.Scrollbar(lib,orient="vertical")
vsb.configure(command=my_tree.yview)
my_tree.configure(yscrollcommand=vsb.set)
vsb.pack(fill=Y,side=RIGHT)

my_tree.pack(padx=20,pady=50)

lib.mainloop()