import requests, json
import tkinter
from tkinter import *

def showWeather():
   try:
      city = textForCity.get()
      Api_Key = "4976409c5fc4acb53273d2a04b8b63a6"
      URL = "https://api.openweathermap.org/data/2.5/weather?"
      Complete_Url = URL + "q=" + city + "&appid=" + Api_Key + "&units=metric"
      response = requests.get(Complete_Url)
      if response.status_code == 200:
         complete_weather_info = response.json()  
         weatherInfo = complete_weather_info['main']

         current_temperature = str(weatherInfo['temp'])
         current_humidity = str(weatherInfo['humidity'])
         current_pressure = str(weatherInfo['pressure'])

         temperatureLabel.configure(text = "TEMPERATURE: " + current_temperature + chr(176) + "C")
         humidityLabel.configure(text = "HUMIDITY: " + current_humidity + "%")
         pressureLabel.configure(text = "PRESSURE: " + current_pressure + "hPa") 
       
   except Exception as e:
      temperatureLabel.configure(text = "Error occured." + str(e))
      humidityLabel.configure(text = "")
      pressureLabel.configure(text = "") 

      print("Error occured.", e)

window = tkinter.Tk()
window.geometry('500x200')
window.title("WEATHER REPORT")

label = Label(window, text = "Enter City name:", font = ("bold", 14))
label.grid(column = 0, row = 0)

textForCity = Entry(window, width = 15)
textForCity.grid(column = 1, row = 0)

button = Button(window, text = "submit", bg = "black", fg = "white", command = showWeather)
button.grid(column = 6, row = 0)

temperatureLabel = Label(window, text = "TEMPERATURE: 0 ", font = ("bold", 9))
temperatureLabel.grid(column = 1, row = 4)

humidityLabel = Label(window, text = "HUMIDITY: 0 ", font = ("bold", 9))
humidityLabel.grid(column = 1, row = 5)

pressureLabel = Label(window, text = "PRESSURE: 0 ", font = ("bold", 9))
pressureLabel.grid(column = 1, row = 6)

window.mainloop()