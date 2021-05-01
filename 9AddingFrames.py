from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Adding Frames to your Program")
root.iconbitmap("images/tkinter.ico")

frame = LabelFrame(root,padx=50,pady=50)
frame.pack(padx=10,pady=10)

b1 = Button(frame,text="Don't Click Here!").grid(row=1)
b2 = Button(frame,text="...or Here!").grid(row=2,column=1)

root.mainloop()