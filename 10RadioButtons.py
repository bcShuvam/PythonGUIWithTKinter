from tkinter import *

root = Tk()
root.title("Adding Frames to your Program")
root.iconbitmap("images/tkinter.ico")

# r = IntVar()
# r.set("2")

TOPPINGS = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text , mode in TOPPINGS:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    mylabel = Label(root, text=value).pack()

# Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda: clicked(r.get())).pack()
# Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda: clicked(r.get())).pack()

# mylabel = Label(root,text=r.get()).pack()
# myButton = Button(root,text="Click Me!",command=lambda: clicked(r.get())).pack()

# mylabel = Label(root,text=pizza.get()).pack()
myButton = Button(root,text="Click Me!",command=lambda: clicked(pizza.get())).pack()

root.mainloop()