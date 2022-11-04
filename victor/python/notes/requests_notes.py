import requests
import time

TIME_OUT = 0
# Status code "200 - 299" means good to go!
# 300 means redirect
# 400 something wrong on client side(Me)
# 500 server side error(Them; or Google in this case.)
'''
 response = requests.get("https://google.com")
#  converts request into a json which can be converted to a python data type
print(response.json)
'''
#PokeAPI
'''
base_url = "https://pokeapi.co/api/v2/"
response = requests.get(base_url + "pokemon/ditto")
pokemon = response.json()
print(pokemon["weight"])
'''

# Weather app

#Make 2 requests
zip_code = input("What is your zip code: ")
#First request to get location key by zipcode
print(f"Fetching data for {zip_code}..")
time.sleep(TIME_OUT) # Adds delay for fun and "User Experience"


api_key = "" #can be protected by holding it in a separate file in your own device then add it to .gitignore
location_url = f"http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey={api_key}&q={zip_code}"
response = requests.get(location_url)
locations = response.json()


print("Multiple locations found, please choose one:")
for i in range(len(locations)):
    print(i, locations[i]["EnglishName"])
choice = int(input("> "))

location = locations[choice]
location_key = location["Key"]

print(f"Fetching weather data for {location['EnglishName']}...")
time.sleep(TIME_OUT)
# Second request to get weather by location key

weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}"
response = requests.get(weather_url)

current_weather = response.json()[0]

print(f"""
Current Time: {current_weather['LocalObservationDateTime']}
It's currently {current_weather["WeatherText"]}
Temperature: {current_weather["Temperature"]['Imperial']['Value']}
For more information please visit: {current_weather['Link']}
""")