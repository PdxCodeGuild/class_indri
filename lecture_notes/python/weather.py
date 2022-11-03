import requests
import time
from keys import api_key
# Weather app

# Make 2 requests
zip_code = input("Enter your zip code: ")
# First request to get location key by zipcode
print(f"Fetching data for {zip_code}...")
time.sleep(2) # Adding delay for fun

location_url = f"http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey={api_key}&q={zip_code}"
response = requests.get(location_url)
locations = response.json()

print("Multiple locations found, please choose one:")
for i in range(len(locations)):
    print(i, locations[i]['EnglishName'])
choice = int(input("> "))

location = locations[choice]

print(f"Fetching weather data for {location['EnglishName']}...")
time.sleep(2) # Adding delay for fun



# Second request to get weather by location key