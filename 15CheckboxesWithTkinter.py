from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Open Files Box Dialog")
root.iconbitmap("images/tkinter.ico")
root.geometry("400x400")

var = StringVar()

c = Checkbutton(root,text="Check this box",variable=var,onvalue="On",offvalue="Off")
c.deselect()
c.pack()

def show():
    mylabel = Label(root,text=var.get()).pack()

btn = Button(root,text="Click Me!",command=show).pack()


root.mainloop()
