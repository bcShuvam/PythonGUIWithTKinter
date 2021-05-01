from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Adding Frames to your Program")
root.iconbitmap("images/tkinter.ico")

# Showinfo , showwarning , showerror , askquestion , askokcancel , askyesno

# False = 0 and True = 1
# cancel = 0 and ok = 1
# no = 0 and yes = 1

def popupShow():
    # messagebox: It takes 3 parameters 1st one is title , 2nd one us message
    # messagebox.showinfo("This is my popup","Hello World!") # Showinfo returns ok
    # messagebox.showwarning("This is my popup","Hello World!") # ShowWarning returns ok
    # messagebox.showerror("This is my popup","Hello World!") # ShowError returns ok

    response = messagebox.showinfo("This is my popup", "Hello World!")
    print(response)

    Label(root,text=response).pack()

def popupAsk():
    messagebox.askquestion("This is my popup","Hello World!") # askquestion returns 0 if no and 1 if ok
    messagebox.askokcancel("This is my popup","Hello World!") # askokcancel returns 0 if no and 1 if ok
    messagebox.askyesno("This is my popup","Hello World!") # askyesno returns 0 if no and 1 if ok

    response = messagebox.askyesno("This is my popup","Hello World!")

    if response == 1:
        Label(root,text="Yes! Yes! Yes!",fg="#38ada9").pack()
    else:
        Label(root,text="Noooooo !!!",fg="#eb2f06").pack()

    # Label(root,text=response).pack()

Button(root,text="PopUp Show",command=popupShow).pack()
Button(root,text="PopUp Ask",command=popupAsk).pack()

root.mainloop()