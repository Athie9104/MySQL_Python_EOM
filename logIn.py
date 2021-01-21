import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox


def logging():
    UserN = entUser.get()
    passW = entpass.get()
    print(f"The name entered by you is {UserN} {passW}")
    loginTodb(UserN, passW)


def loginTodb(UserN, passW):
    if passW:
        mydb = mysql.connector.connect(user='lifechoices',
                                        password='@Lifechoices1234',
                                        host='127.0.0.1',
                                        database='LifechoicesOnline',
                                        auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

    mycursor.execute()
    sql = "INSERT INTO Login_out VALUES (%s, curtime())"
    mycursor.execute(sql, [int(input("Enter id\n"))])
    mydb.commit()

    mycursor.execute("Select * from Login_out")
    for i in mycursor:
        print(i)

def reg():
    import User_number
    
    logIn.withdraw

root = Tk()
root.title('Lifechoices Online')
root.geometry('600x600')
root.configure(bg='#F49F1C')
photo = PhotoImage(file="img1.png")
w = Label(root, image=photo, width=350, height=133)
w.pack()

lblpass = Label(root,  bg='#F49F1C', fg='white', text='Enter Password',)
lblpass.place(x=200, y=300)

entpass = Entry(root, width=45)
entpass.place(x=350, y=300, width=100)

lblUser = Label(root, bg='#F49F1C', fg='white', text='Enter Username',)
lblUser.place(x=200, y=200)

entUser = Entry(root, width=45)
entUser.place(x=350, y=200, width=100)

btnlogin = Button(root, text='Login', bg='#0F52BA', fg='white', command=logging)
btnlogin.place(x=200, y=400, width=80)

btnReg = Button(root, text='Register', bg='#0F52BA', fg='white', command='')
btnReg.place(x=400, y=400, width=80)

root.mainloop()


