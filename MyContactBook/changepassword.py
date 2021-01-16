from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox


class Changepasswordframe(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.place(relx=0.5, rely=0.5, anchor=CENTER)

        s = Style()
        s.configure('TFrame', background='white')

        s.configure('TLabel', background='white', font=('Ariel', 12))

        old_password_label = Label(self, text='Old Password :')
        old_password_label.grid(row=0, column=0, sticky=W)

        self.old_password_entry = Entry(self, font=('Arial', 12), width=15)
        self.old_password_entry.grid(row=0, column=1, pady= 10)

        new_password_label = Label(self, text='New Password :')
        new_password_label.grid(row=1, column=0, sticky=W)

        self.new_password_entry = Entry(self, font=('Arial', 12), width=15)
        self.new_password_entry.grid(row=1, column=1, pady=10)

        confirm_password_label = Label(self, text='Confirm Password :', )
        confirm_password_label.grid(row=2, column=0, sticky=W)

        self.confirm_password_entry = Entry(self, font=('Arial', 12), width=15, show="*")
        self.confirm_password_entry.grid(row=2, column=1, pady=10)

        s.configure('TButton', font=("Arial", 12), width=15)

        change_password_button = Button(self, text='Change Password', command=self.change_password_button_click)
        change_password_button.grid(row=3, column=1, pady=10)

    def change_password_button_click(self):
        con = connect('mycontacts.db')
        cur = con.cursor()
        cur.execute("""select * from Login where Password = ?""", (self.old_password_entry.get(),))
        row = cur.fetchone()
        if row is not None:
            if self.new_password_entry.get()==self.confirm_password_entry.get():
                cur.execute("update Login set Password = ? where Password = ?",
                            (self.new_password_entry.get(), self.old_password_entry.get()))
                con.commit()
                messagebox.showinfo('Success Message', 'Password Changed Successfully')

            else:
                messagebox.showerror('Error Message', "New Password and Confirm Password Do Not Match")
        else:
            messagebox.showerror('Error Message', "Incorrect Old Password")