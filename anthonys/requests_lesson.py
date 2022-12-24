from urllib import response
import requests
search_term=input('Enter a pokemon name: ')
base_url= "https://pokeapi.co/api/v2/pokemon/"
response=requests.get(base_url + search_term)
pokemon=(response.json())

print(f'''Name: {pokemon['name']}
{pokemon['id']} 
Height: {pokemon['height']}
Weight: {pokemon['weight']}''')