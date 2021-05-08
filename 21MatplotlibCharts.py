from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Using SQLlite3 Databases")
root.iconbitmap("images/tkinter.ico")
root.geometry("400x200")
root.configure(background="#2d3436")

def graph():
    house_prices = np.random.normal(200000,25000,5000)
    # plt.hist(house_prices,120)
    # plt.pie(house_prices)
    plt.polar(house_prices)
    plt.show()

my_button = Button(root,text="Graphic",command=graph)
my_button.pack()

root.mainloop()