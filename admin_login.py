from tkinter import messagebox
from tkinter import*
import mysql.connector

# def saveTodb():
#     id1 =
#     fullname =
#     username =
#     password =
#     mydb = mysql.connector.connect(
#                                     host="localhost",
#                                     user="lifechoices",
#                                     password="@Lifechoices1234",
#                                     database="LifechoicesOnline"
#     )
#
#     mycursor = mydb.cursor()
#
#     sql = "INSERT INTO Users (id, full_name, username, password) VALUES (%s, %s, %s, %s)"
#     val = (id1, fullname, username, password)
#     mycursor.execute(sql, val)
#     # mycursor.execute()
#     mydb.commit()
#     messagebox.showinfo("Registration", "Successfully Register")
#
#     print(mycursor.rowcount, "record inserted.")

def saveTodb():
    # userId =

    mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="lifechoices",
                                    password="@Lifechoices1234",
                                    database="LifechoicesOnline")

    mycursor = mydb.cursor()
    res = mycursor.fetchall()
    if res:
        for y in res:
            import admin
root = Tk()
root.title('Lifechoices Online')
root.geometry('400x400')
root.configure(bg='#F49F1C')


lbl_password = Label(root,  bg='#F49F1C', fg='#0F52BA', text='Administrator Login Page')
lbl_password.place(x=50, y=50, width=300)
lbl_password.config(font=('courier', '14', 'bold'))


lbl_AdminId = Label(root,  bg='#F49F1C', fg='white', text='Enter Admin Id')
lbl_AdminId.place(x=150, y=100)

entUserId = Entry(root, width=45)
entUserId.place(x=140, y=150, width=120)

reg_btn = Button(root, text='Login', bg='#0F52BA', fg='white', command='')
reg_btn.place(x=155, y=200, width=80)

# btnReg = Button(root, text='Register', bg='#0F52BA', fg='white', command='')
# btnReg.place(x=250, y=200, width=80)

root.mainloop()
