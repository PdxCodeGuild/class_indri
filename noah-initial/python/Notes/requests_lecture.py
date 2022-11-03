import requests
from keys import api_key
#use jsonplaceholder.com for practice placeholders
# response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# print(response.json())

# search_term = input('Enter a pokemon name: ')
# base_url = "https://pokeapi.com/api/v2/pokemon/"
# response = requests.get(base_url + search_term)

# if response.status_code == 200:
#     pokemon = response.json()

#     print(f"Name: {pokemon['name']}\nNo: {pokemon['id']}\n")
# elif response.status_code == 404:
#     print(f"{search_term} was not found.")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
zip_code = input("Enter your zip code: ")

location_url = f"https://developer.accuweather.com/accuweather-locations-api/apis/get/locations/v1/postalcodes/search?apikey={api_key}&q={zip_code}"
response = requests.get(location_url)

# print(response.json())
locations = response.json()

# print(locations[0]['EnglishName'])
if (len(locations) > 1):
    print("Multiple locations found, please choose one: ")
    for i in range(len(locations)):
     print(i, locations[1]['EnglishName'])
    choice = int(input("> "))
else:
    choice = 0


location = locations[choice]
location_key = location["Key"]

print(f"Fetching weather data for {locations[choice]['EnglishName']}...")

weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}"
response = requests.get(weather_url)
current_weather = response.json()[0]

print(f"""
Current Time: {current_weather['LocalObservationDateTime']}
It is currently {current_weather['WeatherText']}
Temperature: {current_weather['Temperature']['Imperial']['Value']} F
{current_weather['Link']}
""")