from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Icons , Images and Exit Buttons")
root.iconbitmap(r'images/tkinter.ico')

myimg = ImageTk.PhotoImage(Image.open("images/ironman.jpg"))
my_label = Label(image=myimg).pack()

button_quit = Button(root,text="Exit program",command=root.quit).pack()

root.mainloop()