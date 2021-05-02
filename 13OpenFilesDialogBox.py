from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Open Files Box Dialog")
root.iconbitmap("images/tkinter.ico")

def open():
    global myimage
    root.filename = filedialog.askopenfilename(initialdir="images/",title="Select a File",filetypes=(("jpg files","*.jpg"),("all files","*.*")))
    mylabel = Label(root,text=root.filename).pack()
    myimage = ImageTk.PhotoImage(Image.open(root.filename))
    myimage_label = Label(image=myimage).pack()

my_button = Button(root,text="Open File",command=open).pack()

root.mainloop()