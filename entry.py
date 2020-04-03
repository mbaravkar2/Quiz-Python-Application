from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector




mydb = mysql.connector.connect(host="localhost",user="root",password="root",auth_plugin='mysql_native_password',database='mahesh')
print("Database Connected")



def submit1():
    e = username_e.get()
    if e=="":
        MessageBox.showinfo("Insert Status","All fields are required")
    else:
        mydb = mysql.connector.connect(host="localhost",
                               user="root",password="root",
                               auth_plugin='mysql_native_password',database='mahesh')
        
        cur = mydb.cursor()
        insert = "insert into m values('" + e +"')"
        cur.execute(insert)
        MessageBox.showinfo("Insert Status","Added successfully")
        mydb.commit()


root = Tk()
root.title("GBSoftronics")
root.geometry('1366x738')
root.config(bg='white')
root.resizable(0,0)
username = Label(root,text="Username")
username.config(font=('Times new romen',20),bg='white')
username.pack(pady=20)
username_e = Entry(root)
username_e.pack()
submit = Button(root,text='Submit',bg='green',fg='black',width=15,height=2,command=submit1)
submit.pack(pady=30)
