from tkinter import *

root = Tk()

labelname = Label(root,text="Enter your Name.").pack()
e = Entry(root,width=50,bg="#2f3542",fg="#ffffff")
e.pack()
e.insert(0,"Full Name") # It's like placeholder but dosen't erase automatically .

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root,text=hello)
    myLabel.pack()

myButton = Button(root, text="Submit",bg="#16a085",fg="#ffffff",command=myClick)
myButton.pack()

root.mainloop()

# from tkinter import *
#
# root = Tk()
# root.title("Creating Input Fields")
#
# def myClick():
#     mylabel = Label(root,text=entry1.get())
#     mylabel.pack()
#
# userLabel = Label(root,text="Enter your name.").pack()
# # borderwidth=5 It adds width to the border
#
# entry1 = Entry(root,width=50,bg="#2f3542",fg="#ffffff").pack()
#
# mybutton = Button(root,text="Click Me!",bg="#2ed573",fg="#ffffff",command=myClick).pack()
#
# root.mainloop()