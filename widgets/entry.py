from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
window.title("Button")
window.geometry("500x400")


label1 = Label(window, text="Enter Your Name")
label1.pack()

name_entry = Entry(window)
name_entry.pack()

def submit_button_click():
    messagebox.showinfo("Message", "Your Name: " + name_entry.get()) 

submit_button = Button(window, text = "Submit", command = submit_button_click)
submit_button.pack()

window.mainloop()