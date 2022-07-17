
from distutils.log import error
import requests

API_KEY = "25661bc81e02dbbea872cbad3592c7fc"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


city = input("enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")   
else:
    print("error!!!")


