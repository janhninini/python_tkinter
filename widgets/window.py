from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("My first window")
window.geometry("800x500")

#label1 = Label(window, text="Welcome to Python GUI")
#label1.pack()

label00 = Label(window, text= "First Row First Column")
label00.grid(row = 0, column = 0)
label01 = Label(window, text= "First Row Second Column")
label01.grid(row = 0, column = 1)
label10 = Label(window, text= "Second Row First Column")
label10.grid(row = 1, column = 0)
label11 = Label(window, text= "Second Row Second Column")
label11.grid(row = 1, column = 1)








window.mainloop()
