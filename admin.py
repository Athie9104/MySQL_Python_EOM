from tkinter import messagebox
from tkinter import*
import mysql.connector


def saveTodb():
    id1 = entid.get()
    fullname = entfullname.get()
    username = entusername.get()
    password = entpassword.get()
    mydb = mysql.connector.connect(
                                    host="localhost",
                                    user="lifechoices",
                                    password="@Lifechoices1234",
                                    database="LifechoicesOnline"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO Users (id, full_name, username, password) VALUES (%s, %s, %s, %s)"
    val = (id1, fullname, username, password)
    mycursor.execute(sql, val)
    # mycursor.execute()
    mydb.commit()
    messagebox.showinfo("Registration", "Successfully Register")

    print(mycursor.rowcount, "record inserted.")


root = Tk()
root.title('Lifechoices Online')
root.geometry('600x500')
root.configure(bg='#F49F1C')

lbl_register = Label(root,  bg='#F49F1C', fg='#0F52BA', text='Register')
lbl_register.place(x=250, y=50)
lbl_register.config(font=('courier', '30', 'bold'))

lbl_id = Label(root,  bg='#F49F1C', fg='white', text='User id',)
lbl_id.place(x=200, y=100)

entid = Entry(root, width=45)
entid.place(x=300, y=100, width=120)

lbl_fullname = Label(root,  bg='#F49F1C', fg='white', text='Full name',)
lbl_fullname.place(x=200, y=140)

entfullname = Entry(root, width=45)
entfullname.place(x=300, y=140, width=120)

lbl_password = Label(root,  bg='#F49F1C', fg='white', text='Password',)
lbl_password.place(x=200, y=180)

entpassword = Entry(root, width=45)
entpassword.place(x=300, y=180, width=120)

lbl_username = Label(root,  bg='#F49F1C', fg='white', text='Username',)
lbl_username.place(x=200, y=220)

entusername = Entry(root, width=45)
entusername.place(x=300, y=220, width=120)

reg_btn = Button(root, text='Submit', bg='#0F52BA', fg='white', command=saveTodb)
reg_btn.place(x=280, y=300, width=80)

root.mainloop()
