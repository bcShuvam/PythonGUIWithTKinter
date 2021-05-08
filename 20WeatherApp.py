from tkinter import *
import requests
import json

root = Tk()
root.title("Using SQLlite3 Databases")
root.iconbitmap("images/tkinter.ico")
root.geometry("600x100")
root.configure(background="#2d3436")

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=10&API_KEY=9049FF59-56C4-4AE1-BD9F-DECCAFFFA37F


def ziplookup():
    # print(zip.get())

    weather_color = ''
    api = ''
    city = ''
    quality = ''
    category = ''

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zip.get()+"&distance=10&API_KEY=9049FF59-56C4-4AE1-BD9F-DECCAFFFA37F")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        myLabel = Label(root, text=f"{city} Air Quality {quality} {category}", font=("Arial", 20), bg=weather_color,fg="#ffffff")
        myLabel.grid(row=1,column=0,columnspan=2)
    except EXCEPTION as e:
        api = "Error 404"

zip = Entry(root)
zip.grid(row=0,column=0,stick=W+E+N+S)

zipButton = Button(root,text="Lookup Zipcode",command=ziplookup)
zipButton.grid(row=0,column=1,stick=W+E+N+S)

root.mainloop()