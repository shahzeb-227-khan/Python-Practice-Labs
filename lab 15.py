from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pyodbc

m=Tk()
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()



def display():
    con=pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                        r'DBQ=C:\Users\shahz\OneDrive\Documents\lab14work.accdb'))
    cursor1=con.cursor()
    cursor1.execute("select * from Teacher")
    rows=cursor1.fetchall()
    if len(rows)!=0:
        for i in rows:
            stable.insert('',END,values=i)
    con.close()



l1=Label(m,text="Student Management System",fg="black",bg="gold",font=('Times New Roman',30,"bold"),borderwidth=15,relief=SUNKEN)
l1.pack(side=TOP,fill=X)

f1=Frame(m,bg="lightgreen")
f1.place(x=10,y=100,width=450,height=700)
img=PhotoImage(file=r"ned.png")

img2=img.subsample(2,2)
limg=Label(f1,image=img2).grid(row=0,column=0)

l2=Label(f1,text="Tid",fg="darkblue",bg="lightblue",width=15,bd=5,font=("Arial",18,"bold"),relief=RIDGE).grid(row=1,column=0,padx=20,pady=20)
l3=Label(f1,text="name",fg="darkblue",bg="lightblue",width=15,bd=5,font=("Arial",18,"bold"),relief=RIDGE).grid(row=2,column=0,padx=20,pady=20)
l4=Label(f1,text="designation",fg="darkblue",bg="lightblue",width=15,bd=5,font=("Arial",18,"bold"),relief=RIDGE).grid(row=3,column=0,padx=20,pady=20)
l5=Label(f1,text="salary",fg="darkblue",bg="lightblue",width=15,bd=5,font=("Arial",18,"bold"),relief=RIDGE).grid(row=4,column=0,padx=20,pady=20)


e1=Entry(f1,textvariable=var1,width=15,bg="White",fg="black",bd=5).grid(row=1,column=1,padx=50,pady=20)
e2=Entry(f1,textvariable=var2,width=15,bg="White",fg="black",bd=5).grid(row=2,column=1,padx=50,pady=20)
e3=Entry(f1,textvariable=var3,width=15,bg="White",fg="black",bd=5).grid(row=3,column=1,padx=50,pady=20)
e4=Entry(f1,textvariable=var4,width=15,bg="White",fg="black" ,bd=5).grid(row=4,column=1,padx=50,pady=20)

lli=Label(f1,text="Programs")
lli.grid(row=6,column=1)
li=Listbox(f1)
li.insert(1,"software")
li.insert(2,"electrical")
li.insert(3,"mechanical")
li.insert(4,"datascience")
li.grid(row=7,column=1)



f2=Frame(m,bg="lightgreen")
f2.place(x=450,y=75,width=950,height=700)
stable=ttk.Treeview(f2,height=650,columns=('Tid','name','designation','salary'))
stable.pack()
m.mainloop()





#
# b2=Button(f1,text="Insert",bg="Yellow",fg="black",width=15,bd=5,command=add).grid(row=6,column=1,padx=50,pady=10)
# b3=Button(f1,text="Delete",bg="Yellow",fg="black",width=15,bd=5,command=delete).grid(row=7,column=0,padx=50,pady=10)
# b4=Button(f1,text="Update",bg="Yellow",fg="black",width=15,bd=5,command=update).grid(row=7,column=1,padx=50,pady=10)