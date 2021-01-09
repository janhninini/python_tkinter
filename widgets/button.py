from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("Button")
window.geometry("500x400")

def button_click():
    label = Label(window, text = "You clicked the button!")
    label.pack()


button = Button(window, text = "Click Here", command = button_click)
button.pack()


window.mainloop()
