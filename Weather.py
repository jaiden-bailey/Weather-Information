#Jaiden Bailey
import requests
import datetime as dt

def K_to_C_F(K):
    C = K - 273.15
    F = C * (9/5) + 32
    return C, F



baseurl = "http://api.openweathermap.org/data/2.5/weather?"

with open("api_key.txt", "r") as f:
    for line in f.readlines():
        API_key = line.rstrip()

City = input("Choose a city for the weather: ")
url = baseurl + "appid=" + API_key + "&q=" + City

response = requests.get(url).json()


temp_k = response['main']['temp']
temp_c, temp_f = K_to_C_F(temp_k)
feels_like_K = response['main']['feels_like']
feels_like_C, feels_like_F = K_to_C_F(feels_like_K)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"tempeture in {City}: {temp_c:.2f}°C or {temp_f:.2f}°F")
print(f"tempeture in {City} feels like: {feels_like_C:.2f}°C or {feels_like_F:.2f}°F")
print(f"humidity in {City}: {humidity}%")
print(f"wind speed in {City}: {wind_speed}m/s")
print(f"general weather in {City}: {description}")
print(f"sun rises in {City}: {sunrise_time}")
print(f"sun sets in {City}: {sunset_time}")
