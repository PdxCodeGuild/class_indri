import requests
import time
from os import system
import webbrowser
from keys import api_key
# Weather app

TIME_OUT = 0

# Make 2 requests
zip_code = input("Enter your zip code: ")
# First request to get location key by zipcode
print(f"Fetching data for {zip_code}...")
time.sleep(TIME_OUT) # Adding delay for fun
system('clear')


location_url = f"http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey={api_key}&q={zip_code}"
response = requests.get(location_url)
locations = response.json()

if(len(locations) > 1):
    # Print out all locations from the API so user can choose their location.
    print("Multiple locations found, please choose one:")
    for i in range(len(locations)):
        print(i, locations[i]['EnglishName'])
    choice = int(input("> "))
else:
    choice = 0

# Pull chosen location from locations list
location = locations[choice]
location_key = location["Key"]

system('clear')

print(f"Fetching weather data for {location['EnglishName']}...")
time.sleep(TIME_OUT) # Adding delay for fun

system('clear')

# Second request to get weather by location key
# Build up url to get weather data using location key and api key
weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}"
response = requests.get(weather_url)

# response.json() is a list, we are using [0] to pull out the first item of the list
current_weather = response.json()[0]

# Access nested dictionaries by providing keys in series ie. ['key1']['key2']['etc...']
print(f"""
Current Time: {current_weather['LocalObservationDateTime']}
It is currently {current_weather['WeatherText']}
Temperature: {current_weather['Temperature']['Imperial']['Value']} F
""")
webbrowser.open(current_weather['Link'])