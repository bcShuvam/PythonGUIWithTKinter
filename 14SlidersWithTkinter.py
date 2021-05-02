from tkinter import *

root = Tk()
root.title("Open Files Box Dialog")
root.iconbitmap("images/tkinter.ico")
root.geometry("300x600")

vertical = Scale(root,from_=0,to=600)
vertical.pack()

def slide():
    # mylabel = Label(root,text=horizontal.get()).pack()
    root.geometry(f"{horizontal.get()}x{vertical.get()}")

horizontal = Scale(root,from_=0,to=800,orient=HORIZONTAL)
horizontal.pack()

mybutton = Button(root,text="Click Me!",command=slide).pack()

root.mainloop()