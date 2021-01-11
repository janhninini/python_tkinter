from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox
import home


class Loginwindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Login")
        self.geometry("500x400")

        s = Style()
        s.configure('Header.TFrame', background="pink")

        header_frame = Frame(self, style='Header.TFrame')
        header_frame.pack(fill=X)

        s.configure('Header.TLabel', background='pink', foreground='white', font=('Arial', 25))

        header_label = Label(header_frame, text="My Contact Book", style='Header.TLabel')
        header_label.pack(pady=10)

        s.configure('Content.TFrame', background="white")

        content_frame = Frame(self, style='Content.TFrame')
        content_frame.pack(fill=BOTH, expand=TRUE)

        s.configure('Login.TFrame', background="white")

        login_frame = Frame(content_frame, style='Login.TFrame')
        login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        s.configure('Login.TLabel', background='white', font=('Arial', 12))

        l1 = Label(login_frame, text ='Username : ', style='Login.TLabel')
        l1.grid(row = 0, column = 0)

        self.username_entry = Entry(login_frame, font=('Arial', 12))
        self.username_entry.grid(row=0, column=1)

        l2 = Label(login_frame, text='Password : ', style='Login.TLabel')
        l2.grid(row=1, column=0)

        self.password_entry = Entry(login_frame, show="*", font=('Arial', 12))
        self.password_entry.grid(row=1, column=1, pady=10)

        s.configure('Login.TButton', font=("Arial", 12))

        login_button = Button(login_frame, text='Login', style='Login.TButton', command = self.login_button_click)
        login_button.grid(row=2, column=1, pady=10)

    def login_button_click(self):
        con = connect('mycontacts.db')
        cur = con.cursor()
        cur.execute('''select * from Login where
        Username = ? and Password = ?''', (self.username_entry.get(), self.password_entry.get()))
        row = cur.fetchone()
        if row is not None:
            self.destroy()
            home.Homewindow()
        else:
            messagebox.showerror('Error Message', 'Invalid Username or Password')





if __name__=='__main__':
    lw = Loginwindow()
    lw.mainloop()