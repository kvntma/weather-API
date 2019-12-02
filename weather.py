import api_config
import requests
import json

# url for data
call_weather = "http://api.openweathermap.org/data/2.5/weather?q="
city = input("Where would you like to check the weather?: ")
my_api = api_config.api_key
url = call_weather + city + "&appid=" + my_api

print(city)

response = requests.get(url)
parsed_r = response.json()

temperature = parsed_r['main']['temp']
t_int = int(temperature - 273)
weather = parsed_r['weather'][0]['description']


print("It is currently " + str(t_int) +
      " degrees celcius with a forecast of " + weather)
