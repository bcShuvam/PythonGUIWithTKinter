from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Using SQLlite3 Databases")
root.iconbitmap("images/tkinter.ico")
root.geometry("400x400")

conn = sqlite3.connect('address_book.db')

c = conn.cursor()

# Create a function to delete a record
def delete():
    # CREATE a database or connect to existing one
    conn = sqlite3.connect('address_book.db')

    # Create a cursor
    c = conn.cursor()

    #Delete a record
    c.execute("DELETE from address WHERE oid = " + delete_box.get() )

    delete_box.delete(0,END)

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

# Create Submit function for database
def submit():
    # CREATE a database or connect to existing one
    conn = sqlite3.connect('address_book.db')

    # Create a cursor
    c = conn.cursor()

    # Insert into Table
    c.execute("INSERT INTO address VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                 'f_name':f_name.get(),
                 'l_name':l_name.get(),
                 'address':address.get(),
                 'city':city.get(),
                 'state':state.get(),
                 'zipcode':zipcode.get()
              })

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

# Create query gunction
def query():
    # CREATE a database or connect to existing one
    conn = sqlite3.connect('address_book.db')

    # Create a cursor
    c = conn.cursor()

    # Query the database
    c.execute("Select *,oid from address")
    records = c.fetchall()
    # print(records)

    # Loop the results
    print_records = ''
    for record in records:
        print_records += f"{str(record[0])} {str(record[1])} \t {str(record[6])}\n"

    query_label = Label(root,text=print_records)
    query_label.grid(row=11,column=0,columnspan=2)

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

# Create Text Boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
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

delete_box = Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)

# Create Text Box Labels
f_namel = Label(root,text="First Name")
f_namel.grid(row=0,column=0,pady=(10,0))
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
delete_box_label = Label(root,text="Delete ID")
delete_box_label.grid(row=9,column=0,pady=5)

# Create a submit button
submit_button = Button(root,text="Add Record To Database",command=submit)
submit_button.grid(row=6,column=0,columnspan=2,pady=2,padx=10,ipadx=100)

# Create a Query Button
query_button = Button(root,text="Show Records",command=query)
query_button.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

# Create a delete button
delete_button = Button(root,text="Delete Records",command=delete)
delete_button.grid(row=10,column=0,columnspan=2,pady=5,padx=10,ipadx=136)

root.mainloop()