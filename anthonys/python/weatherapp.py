import requests
from keys import api_key
zip_code=input('Enter your zip code: ')
location_url=f'http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey={api_key}&q={}'
respone= requests.get(location_url)

print(respone.json())