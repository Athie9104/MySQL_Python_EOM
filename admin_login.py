from tkinter import messagebox
from tkinter import*
import mysql.connector


def login_ad():
    adminPassword = entUserPass.get()

    mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="lifechoices",
                                    password="@Lifechoices1234",
                                    database="LifechoicesOnline")
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Admin WHERE password =%s'
    mycursor.execute(sql, [adminPassword])
    res = mycursor.fetchall()
    if res:
        for i in res:
            logged()
            break
    else:
        failed()


def logged():
    messagebox.showinfo('Correct', 'you have successfully logged into admin')
    import admin



def failed():
    messagebox.showinfo('Failed', 'Please enter correct admin password')
    entUserPass.focus()



root = Tk()
root.title('Lifechoices Online')
root.geometry('400x400')
root.configure(bg='#F49F1C')


lbl_password = Label(root,  bg='#F49F1C', fg='#0F52BA', text='Administrator Login Page')
lbl_password.place(x=50, y=50, width=300)
lbl_password.config(font=('courier', '14', 'bold'))


lbl_AdminPass = Label(root,  bg='#F49F1C', fg='white', text='Enter Admin Password')
lbl_AdminPass.place(x=150, y=100)

entUserPass = Entry(root, width=45)
entUserPass.place(x=140, y=150, width=120)

reg_btn = Button(root, text='Login', bg='#0F52BA', fg='white', command=login_ad)
reg_btn.place(x=155, y=200, width=80)

root.mainloop()
