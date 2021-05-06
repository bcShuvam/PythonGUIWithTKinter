from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Using SQLlite3 Databases")
root.iconbitmap("images/tkinter.ico")
root.geometry("400x400")

conn = sqlite3.connect('address_book.db')

c = conn.cursor()

# Create Edit function to update a record
def update():
    # CREATE a database or connect to existing one
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE address SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id
              })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

    editor.destroy()

def edit():
    global editor
    editor = Tk()
    editor.title("Update a record")
    editor.iconbitmap("images/tkinter.ico")
    editor.geometry("400x200")

    # CREATE a database or connect to existing one
    conn = sqlite3.connect('address_book.db')
    # Create a cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FROM address WHERE oid = " + record_id)
    records = c.fetchall()

    # Create global editor for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    # Create Text Box Labels
    f_namel = Label(editor, text="First Name")
    f_namel.grid(row=0, column=0, pady=(10, 0))
    l_namel = Label(editor, text="Last Name")
    l_namel.grid(row=1, column=0)
    addressl = Label(editor, text="Address")
    addressl.grid(row=2, column=0)
    cityl = Label(editor, text="City")
    cityl.grid(row=3, column=0)
    statel = Label(editor, text="State")
    statel.grid(row=4, column=0)
    zipcodel = Label(editor, text="Zip Code")
    zipcodel.grid(row=5, column=0)

    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create and Save button To save edited record
    edit_button = Button(editor, text="Edit Records", command=update)
    edit_button.grid(row=11, column=0, columnspan=2, pady=5, padx=10, ipadx=143)


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
    query_label.grid(row=12,column=0,columnspan=2)

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
delete_box_label = Label(root,text="Select ID")
delete_box_label.grid(row=9,column=0,pady=5)

# Create a submit button
submit_button = Button(root,text="Add Record To Database",command=submit)
submit_button.grid(row=6,column=0,columnspan=2,pady=2,padx=10,ipadx=110)

# Create a Query Button
query_button = Button(root,text="Show Records",command=query)
query_button.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

# Create a delete button
delete_button = Button(root,text="Delete Records",command=delete)
delete_button.grid(row=10,column=0,columnspan=2,pady=5,padx=10,ipadx=136)

# Create and Update button
edit_button = Button(root,text="Edit Records",command=edit)
edit_button.grid(row=11,column=0,columnspan=2,pady=5,padx=10,ipadx=143)

# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()