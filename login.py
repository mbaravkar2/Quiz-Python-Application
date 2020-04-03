from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector
import fetch_data_from_tablequestiondb




mydb = mysql.connector.connect(host="localhost",
                               user="root",password="root",
                              auth_plugin='mysql_native_password',database='signup')

print("Database Connected")


    
    
def destroy_login():
    #login from database
    p = username_e.get()
    u = password_e.get()
    
    if p=="" or u=="":
        MessageBox.showinfo("Insert Status","All fields are required")
    else:
        mydb = mysql.connector.connect(host="localhost",
                               user="root",password="root",
                               auth_plugin='mysql_native_password',database='signup')

        cur = mydb.cursor()
        find = "select * from submit where username=\"%s\" and password=\"%s\""%(p,u)
        print(find)
        cur.execute(find)
        mydb.close()
        fetch = cur.fetchall()
        rw = cur.rowcount
        
        if rw==1:
            root.destroy()
            root2 = Tk()
            root2.title("questions")
            root2.geometry('1366x738')
            root2.config(bg='white')
            root2.resizable(0,0)

            for i in range(0,len(fetch_data_from_tablequestiondb.optionC)+1):
                ques = fetch_data_from_tablequestiondb.que[i]
                print(ques)
                question_label = Label(root2,text=ques,font=("adobehebrew",18),bg='white')
                question_label.place(x=20,y=120)
                quea = fetch_data_from_tablequestiondb.opa[i]
                queb = fetch_data_from_tablequestiondb.opb[i]
                quec = fetch_data_from_tablequestiondb.opc[i]
                qued = fetch_data_from_tablequestiondb.opd[i]


            #QUESTTION
            quizlabel = Label(root2,text="Question Page",font=("adobehebrew",44),bg='white')
            quizlabel.pack()
            question_label = Label(root2,text="Question:",font=("adobehebrew",30),bg='white')
            question_label.place(x=20,y=60)
            opA=Radiobutton(root2,value=1,bg='white')
            opA.place(x=20,y=240)
            opB=Radiobutton(root2,value=2,bg='white', text="question")
            opB.place(x=20,y=270)
            opC=Radiobutton(root2,value=3,bg='white')
            opC.place(x=20,y=300)
            opD=Radiobutton(root2,value=4,bg='white')
            opD.place(x=20,y=330)

            #BUTTON TO NEXT
            next = Button(root2,text='NEXT',bg='silver',fg='black',width=15,height=2,command=submit1)
            next.place(x=650,y=450)
            next = Button(root2,text='SUBMIT',bg='silver',fg='black',width=15,height=2,command=submit1)
            next.place(x=450,y=450)
            
        else:
            MessageBox.showinfo("login","Login failed")
        
            
      
    
def signup1():
    root.destroy()
    root1 = Tk()
    root1.geometry('700x600')
    root1.config(bg='white')
    root1.resizable(0,0)
    signup_label = Label(root1,text="SignUP ",fg="gold",bg='white',font=("times new romen",50))
    signup_label.pack()
    #Information for signup
    name = Label(root1,text="Name",bg='white',font=('Times new romen',15))
    name.pack()
    global name_e
    global email_e
    global contact_e
    global username1_e
    global password1_e
    
    name_e = Entry(root1)
    name_e.pack()
    email = Label(root1,text="E-mail",bg='white',font=('Times new romen',15))
    email.pack()
    email_e = Entry(root1)
    email_e.pack()
    contact = Label(root1,text="Contact",bg='white',font=('Times new romen',15))
    contact.pack()
    contact_e = Entry(root1)
    contact_e.pack()
    username1 = Label(root1,text="Username",bg='white',font=('Times new romen',15))
    username1.pack()
    username1_e = Entry(root1)
    username1_e.pack()
    password1 = Label(root1,text="Password",bg='white',font=('Times new romen',15))
    password1.pack()
    password1_e = Entry(root1)
    password1_e.pack()

    #Submit
    submit = Button(root1,text='Submit',bg='green',fg='black',width=15,height=2,command=submit1)
    submit.pack(pady=30)
    Back = Button(root1,text='BackToLogin',bg='green',fg='black',width=15,height=2,command=login)
    Back.pack(pady=30)
    root1.destroy()

def submit1():
    n = name_e.get()
    e = email_e.get()
    c = contact_e.get()
    u = username1_e.get()
    p = password1_e.get()

    if n=="" or e=="" or c=="" or u=="" or p=="":
        MessageBox.showinfo("Insert Status","All fields are required")
    else:
        mydb = mysql.connector.connect(host="localhost",
                               user="root",password="root",
                               auth_plugin='mysql_native_password',database='signup')
        
        cur = mydb.cursor()
        insert = "insert into submit values('" + n +"','" + e +"','" + c +"','" + u +"','" + p +"')"
        cur.execute(insert)
        MessageBox.showinfo("Insert Status","Added successfully")
        mydb.commit()
        mydb.close()

def login():
        
#HOMEPAGE
    global root
    root = Tk()
    root.title("GBSoftronics")
    root.geometry('700x600')
    root.config(bg='white')
    root.resizable(0,0)
    height = 700
    width = 600
    x = int(width / 2 -  600 / 2)
    y  = int(height / 2 - 500 / 2)
    #Logo
    Logo = Label(root,text="GBSoftronics",fg="red",bg='white')
    Logo.config(font=("adobehebrew",44))
    Logo.pack(pady=20)

    #username and password
    global username
    global password
    global username_e
    global password_e
    username = Label(root,text="Username")
    username.config(font=('Times new romen',20),bg='white')
    username.pack(pady=20)
    username_e = Entry(root)
    username_e.pack()
    password = Label(root,text="Password")
    password.config(font=('Times new romen',20),bg='white')
    password.pack(pady=20)
    password_e = Entry(root , show="*")
    password_e.pack()
    

 
    #Button
    login = Button(text='Login',bg='red',fg='black',width=15,font=('times new romen',10),height=2,command=destroy_login)
    login.pack(pady=20)
    signup = Button(text='Signup',bg='red',fg='black',width=15,height=2,font=('times new romen',10),command=signup1)
    signup.pack()
    
    root.mainloop
    
login()

