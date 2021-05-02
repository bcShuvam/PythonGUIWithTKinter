from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Open Files Box Dialog")
root.iconbitmap("images/tkinter.ico")
root.geometry("400x400")

# Drop Down Boxes

def show():
    myLabel = Label(root,text=clicked.get()).pack()

options = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

clicked = StringVar()
clicked.set(options[0])

# drop  = OptionMenu(root,clicked,"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday") #
drop  = OptionMenu(root,clicked,*options) #
drop.pack()

myButton = Button(root,text="Show Selection",command=show).pack()

root.mainloop()