from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Creating New Window")
root.iconbitmap("images/tkinter.ico")

def open():
    global my_image
    top = Toplevel()
    top.title("This is secondary window")
    top.iconbitmap("images/tkinter.ico")

    # label = Label(top,text="Hello World!").pack()
    my_image = ImageTk.PhotoImage(Image.open("images/ironman.jpg"))
    my_label = Label(top, image=my_image).pack()

    btn2 = Button(top,text="Close Me!",command=top.destroy).pack() # top.destroy will destroy/close the second window

btn = Button(root,text="Open Second Window",command=open).pack()

root.mainloop()