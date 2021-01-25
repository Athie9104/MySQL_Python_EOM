from tkinter import messagebox
from tkinter import*
import mysql.connector


def cellNo():
    contact = entNum.get()
    messagebox.showinfo('Successfully logged', 'Welcome to Life Choices Online')


def logout():
        mydb = mysql.connector.connect(user='lifechoices',
                                        password='@Lifechoices1234',
                                        host='127.0.0.1',
                                        database='LifechoicesOnline',
                                        auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()


root1 = Tk()
root1.title('Lifechoices Online')
root1.geometry('400x400')
root1.configure(bg='#F49F1C')
photo = PhotoImage(file="img1.png")
w = Label(root1, image=photo, width=350, height=133)
w.pack()

lbl_password = Label(root1,  bg='#F49F1C', fg='white', text='Enter Contact Number',)
lbl_password.place(x=140, y=200)

entNum = Entry(root1, width=45)
entNum.place(x=140, y=240, width=120)

btnSubm = Button(root1, text='Submit', bg='#0F52BA', fg='white', command=cellNo)
btnSubm.place(x=120, y=280, width=80)

btnLogOut = Button(root1, text='Log out', bg='#0F52BA', fg='white', command=logout)
btnLogOut.place(x=220, y=280, width=80)

root1.mainloop()
