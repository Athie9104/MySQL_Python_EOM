from tkinter import messagebox
from tkinter import*
# import mysql.connector


def cellNo():
    contact = entNum.get()
    messagebox.showinfo('Successfully logged', 'Welcome to Life Choices Online')


root = Tk()
root.title('Lifechoices Online')
root.geometry('400x400')
root.configure(bg='#F49F1C')
photo = PhotoImage(file="img1.png")
w = Label(root, image=photo, width=350, height=133)
w.pack()

lbl_password = Label(root,  bg='#F49F1C', fg='white', text='Enter Contact Number',)
lbl_password.place(x=140, y=200)

entNum = Entry(root, width=45)
entNum.place(x=140, y=240, width=120)

btnSubm = Button(root, text='Submit', bg='#0F52BA', fg='white', command=cellNo)
btnSubm.place(x=120, y=280, width=80)

btnLogOut = Button(root, text='Log out', bg='#0F52BA', fg='white', command='')
btnLogOut.place(x=220, y=280, width=80)

root.mainloop()
