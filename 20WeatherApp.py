from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import requests
import json

root = Tk()
root.title("Using SQLlite3 Databases")
root.iconbitmap("images/tkinter.ico")
root.geometry("450x40")
root.configure(background="#2d3436")

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=10&API_KEY=9049FF59-56C4-4AE1-BD9F-DECCAFFFA37F


try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=10&API_KEY=9049FF59-56C4-4AE1-BD9F-DECCAFFFA37F")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
except EXCEPTION as e:
    api = "Error 404"

myLabel = Label(root,text=f"{city} Air Quality {quality} {category}",font=("Arial",20),bg="#27ae60",fg="#ffffff")
myLabel.pack()

root.mainloop()