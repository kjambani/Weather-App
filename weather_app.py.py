import tkinter as tk
import requests

def fetch_weather(city):
    api_key = "c6e315d09197cec231495138183954bd"  # Get your API key from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != "404":
        weather_info = data["main"]
        temperature = weather_info["temp"]
        humidity = weather_info["humidity"]
        pressure = weather_info["pressure"]
        weather_desc = data["weather"][0]["description"]
        result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nPressure: {pressure} hPa\nDescription: {weather_desc}")
    else:
        result_label.config(text="City not found")

def get_weather():
    city = city_entry.get()
    fetch_weather(city)

app = tk.Tk()
app.title("Weather App")
app.geometry("700x600+400+150")

city_label = tk.Label(app, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
