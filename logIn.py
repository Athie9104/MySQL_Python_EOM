import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox


def logging():
    UserId = entUserId.get()
    loginTodb(UserId)


def loginTodb(UserId):
    if UserId:
        mydb = mysql.connector.connect(user='lifechoices',
                                        password='@Lifechoices1234',
                                        host='127.0.0.1',
                                        database='LifechoicesOnline',
                                        auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

    else:
        mydb = mysql.connector.connect(user='lifechoices',
                                        password='@Lifechoices1234',
                                        host='127.0.0.1',
                                        database='LifechoicesOnline',
                                        auth_plugin='mysql_native_password')
        mycursor=mydb.cursor()
    myquery='INSERT INTO Login_out VALUES (%s, login_logout())'
    mycursor.execute("Select * from Login_out")

    val = int(UserId)
    try:
        mycursor.execute(myquery, val)
        result = mycursor.fetchall()
        if result:
            for x in result:
                messagebox.showinfo('Successfully logged')
                import user_number
        #     print(x)
        # print('Query successful')

    except:
        mydb.rollback()
        messagebox.showinfo('Error occurred', 'Go to the admin to register your details')

        print('Error occurred')


def reg():
        # mydb = mysql.connector.connect(user='lifechoices',
        #                                 password='@Lifechoices1234',
        #                                 host='127.0.0.1',
        #                                 database='LifechoicesOnline',
        #                                 auth_plugin='mysql_native_password')
        #
        # mycursor = mydb.cursor()
        # res = mycursor.fetchall()
        # if res:
        #     for y in res:
                messagebox.showinfo('Admin', 'You are in admin please enter your admin id')
                import admin_login


root = Tk()
root.title('Lifechoices Online')
root.geometry('600x600')
root.configure(bg='#F49F1C')
photo = PhotoImage(file="img1.png")
w = Label(root, image=photo, width=350, height=133)
w.pack()

lblId = Label(root, bg='#F49F1C', fg='white', text='Enter User id',)
lblId.place(x=200, y=200)

entUserId = Entry(root, width=45)
entUserId.place(x=350, y=200, width=100)

btnlogin = Button(root, text='Login', bg='#0F52BA', fg='white', command=logging)
btnlogin.place(x=150, y=300, width=80)

btnadmin = Button(root, text='Admin', bg='#0F52BA', fg='white', command=reg)
btnadmin.place(x=350, y=300, width=80)

root.mainloop()


