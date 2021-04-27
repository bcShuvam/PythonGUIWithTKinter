from tkinter import *

root = Tk()

# Creating a Label Widget
mylabel1 = Label(root,text="Python tkinter")
mylabel11 = Label(root,text="               ").grid(row=0,column=0)
mylabel2 = Label(root,text="Positioning Grid System")
mylabel3 = Label(root,text="Rows And Columns")

# Dsiplaying it on the screen
mylabel1.grid(row=0,column=1)
# mylabel11.grid(row=0,column=0)
mylabel2.grid(row=1,column=1)
mylabel3.grid(row=2,column=0)

root.mainloop()