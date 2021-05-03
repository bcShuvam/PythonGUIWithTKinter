from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Using SQLlite3 Databases")
root.iconbitmap("images/tkinter.ico")
root.geometry("400x400")

# CREATE a database or connect to existing one
conn = sqlite3.connect('address_book.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE address (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")

# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()