from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox


class Managecontactsframe(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.pack(fill=BOTH, expand=TRUE)

        s = Style()
        s.configure('TFrame', background='white')
        s.configure("TLabel", background='white', font=('Ariel', 12))
        s.configure("TButton", font=('Ariel', 12))

        self.con = connect('mycontacts.db')
        self.cur = self.con.cursor()

        self.create_view_all_contacts_frame()


    def create_view_all_contacts_frame(self):
        self.view_all_contacts_frame = Frame(self)
        self.view_all_contacts_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        add_new_contacts_button = Button(self.view_all_contacts_frame, text='Add New Contact',
                                         command=self.add_new_contacts_button_click)
        add_new_contacts_button.grid(row=0, column=0, columnspan=2, sticky=E, pady=10)

        name_label = Label(self.view_all_contacts_frame, text='Name :')
        name_label.grid(row=1, column=0, sticky=W)

        self.name_entry = Entry(self.view_all_contacts_frame, width=60, font=('Ariel', 12))
        self.name_entry.grid(row=1, column=1, sticky=W, pady=20)
        self.name_entry.bind('<KeyRelease>', self.name_entry_key_release)


        # Treeview is used to create a table

        self.contacts_treeview = Treeview(self.view_all_contacts_frame, show='headings',
                                     columns=('name', 'phone_number', "email_id", 'city'))
        self.contacts_treeview.grid(row=2, column=0, columnspan=2)
        self.contacts_treeview.heading('name', text='Name')
        self.contacts_treeview.heading('phone_number', text="Phone Number")
        self.contacts_treeview.heading('email_id', text='Email ID')
        self.contacts_treeview.heading('city', text='City')

        self.contacts_treeview.column('name', width=200)
        self.contacts_treeview.column('phone_number', width=100)
        self.contacts_treeview.column('email_id', width=200)
        self.contacts_treeview.column('city', width=100)
        self.contacts_treeview.bind('<<TreeviewSelect>>', self.contacts_treeview_row_selection)

        self.cur.execute("select * from Contact")
        self.fill_contacts_treeview()




    def add_new_contacts_button_click(self):
        self.view_all_contacts_frame.destroy()

        self.add_new_contacts_frame = Frame(self)
        self.add_new_contacts_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


        name_label = Label(self.add_new_contacts_frame, text='Name :')
        name_label.grid(row=0,column=0, sticky=W)

        self.name_entry = Entry(self.add_new_contacts_frame, width=30, font=('Ariel', 12))
        self.name_entry.grid(row=0, column=1, pady=10)

        phone_number_label = Label(self.add_new_contacts_frame, text='Phone Number :')
        phone_number_label.grid(row=1, column=0, sticky=W)

        self.phone_number_entry = Entry(self.add_new_contacts_frame, width=30, font=('Ariel', 12))
        self.phone_number_entry.grid(row=1, column=1, pady=10)

        email_id_label = Label(self.add_new_contacts_frame, text='Email ID :')
        email_id_label.grid(row=2, column=0, sticky=W)

        self.email_id_entry = Entry(self.add_new_contacts_frame, width=30, font=('Ariel', 12))
        self.email_id_entry.grid(row=2, column=1, pady=10)

        city_label = Label(self.add_new_contacts_frame, text='City :')
        city_label.grid(row=3, column=0, sticky=W)

        self.city_combobox = Combobox(self.add_new_contacts_frame, width=28, font=('Ariel', 12),
                                      values=('Noida', 'Greater Noida', 'New Delhi', 'Jhansi', 'Mathura', 'Agra'))
        self.city_combobox.grid(row=3, column=1, pady=10)

        add_button = Button(self.add_new_contacts_frame, text='Add', width=30, command=self.add_button_click)
        add_button.grid(row=4, column=1, pady=10)

    def add_button_click(self):

        self.cur.execute("""select * from Contact where EmailId = ?""", (self.email_id_entry.get(),))
        contact = self.cur.fetchone()


        if contact is None:
            self.cur.execute("""insert into Contact values(?, ?, ?, ?)""",
                             (self.name_entry.get(),
                              self.phone_number_entry.get(),
                              self.email_id_entry.get(),
                              self.city_combobox.get()))
            self.con.commit()
            messagebox.showinfo("Success Message", "Contact Details Added Successfully")
        else:
            messagebox.showerror("Error Message", "Contact Details are Already Added")

        self.add_new_contacts_frame.destroy()
        self.create_view_all_contacts_frame()

    def name_entry_key_release(self, event):
        self.cur.execute("select * from Contact where name like ?",
                         ("%"+ self.name_entry.get() +"%", ))

        self.fill_contacts_treeview()

    def fill_contacts_treeview(self):

        for contact in self.contacts_treeview.get_children():
            self.contacts_treeview.delete(contact)

        contacts = self.cur.fetchall()
        for contact in contacts:
            self.contacts_treeview.insert("", END, values=contact)

    def contacts_treeview_row_selection(self, event):
        contact = self.contacts_treeview.item(self.contacts_treeview.selection())['values']
        self.view_all_contacts_frame.destroy()

        self.update_delete_contacts_frame = Frame(self)
        self.update_delete_contacts_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        name_label = Label(self.update_delete_contacts_frame, text='Name :')
        name_label.grid(row=0, column=0, sticky=W)

        self.name_entry = Entry(self.update_delete_contacts_frame, width=30, font=('Ariel', 12))
        self.name_entry.grid(row=0, column=1, pady=10)
        self.name_entry.insert(END, contact[0])

        phone_number_label = Label(self.update_delete_contacts_frame, text='Phone Number :')
        phone_number_label.grid(row=1, column=0, sticky=W)

        self.phone_number_entry = Entry(self.update_delete_contacts_frame, width=30, font=('Ariel', 12))
        self.phone_number_entry.grid(row=1, column=1, pady=10)
        self.phone_number_entry.insert(END, contact[1])


        email_id_label = Label(self.update_delete_contacts_frame, text='Email ID :')
        email_id_label.grid(row=2, column=0, sticky=W)

        self.email_id_entry = Entry(self.update_delete_contacts_frame, width=30, font=('Ariel', 12))
        self.email_id_entry.grid(row=2, column=1, pady=10)
        self.email_id_entry.insert(END, contact[2])
        self.old_email_id = contact[2]

        city_label = Label(self.update_delete_contacts_frame, text='City :')
        city_label.grid(row=3, column=0, sticky=W)

        self.city_combobox = Combobox(self.update_delete_contacts_frame, width=28, font=('Ariel', 12),
                                      values=('Noida', 'Greater Noida', 'New Delhi', 'Jhansi', 'Mathura', 'Agra'))
        self.city_combobox.grid(row=3, column=1, pady=10)
        self.city_combobox.set(contact[3])

        update_button = Button(self.update_delete_contacts_frame, text='Update', width=20, command=self.update_button_click)
        update_button.grid(row=4, column=0, pady=10)

        delete_button = Button(self.update_delete_contacts_frame, text='Delete', width=20, command=self.delete_button_click)
        delete_button.grid(row=4, column=1, pady=10)

    def update_button_click(self):
        self.cur.execute("""update Contact set Name = ?, PhoneNumber = ?, EmailId = ?, City = ? where EmailId = ?""",
                         (self.name_entry.get(), self.phone_number_entry.get(), self.email_id_entry.get(),
                          self.city_combobox.get(), self.old_email_id))
        self.con.commit()
        messagebox.showinfo("Success Message", "Contact Details Updated Successfully")
        self.update_delete_contacts_frame.destroy()
        self.create_view_all_contacts_frame()

    def delete_button_click(self):
        messagebox.askquestion('Confirmation Message', )













