from tkinter import *

root = Tk()

def myclick():
    myLabel = Label(root,text="Look! You Clicked the button .")
    myLabel.pack()

# padx=50,pady=50 padding inside the button ,state=DISABLED will disable the button
mybutton = Button(root,text="Click Me",command=myclick,fg="#fff",bg="#2c3e50")
mybutton.pack()

root.mainloop()