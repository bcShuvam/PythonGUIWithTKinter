from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Using SQLlite3 Databases")
root.iconbitmap("images/tkinter.ico")
root.geometry("400x400")

conn = sqlite3.connect('address_book.db')

c = conn.cursor()

# Create Submit function for database
def submit():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    """Clear the text boxes"""
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)


# Create Text Boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
address = Entry(root,width=30)
address.grid(row=2,column=1,padx=20)
city = Entry(root,width=30)
city.grid(row=3,column=1,padx=20)
state = Entry(root,width=30)
state.grid(row=4,column=1,padx=20)
zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)

# Create Text Box Labels
f_namel = Label(root,text="First Name")
f_namel.grid(row=0,column=0)
l_namel = Label(root,text="Last Name")
l_namel.grid(row=1,column=0)
addressl = Label(root,text="Address")
addressl.grid(row=2,column=0)
cityl = Label(root,text="City")
cityl.grid(row=3,column=0)
statel = Label(root,text="State")
statel.grid(row=4,column=0)
zipcodel = Label(root,text="Zip Code")
zipcodel.grid(row=5,column=0)

# Create a submit button
submit_button = Button(root,text="Add Record To Database",command=submit)
submit_button.grid(row=6,column=0,columnspan=2,pady=2,padx=10,ipadx=100)

root.mainloop()