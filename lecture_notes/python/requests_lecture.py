import requests

search_term = input("Enter a pokemon name: ")
base_url = "https://pokeapi.co/api/v2/pokemon/"

headers = {
    'accept': 'application/json',
}

response = requests.get(base_url + search_term, headers=headers)


if response.status_code == 200:
    pokemon = response.json()

    print(f"""Name: {pokemon['name']}
    No: {pokemon['id']}
    Height: {pokemon['height']}
    Weight: {pokemon['weight']}""")
    
elif response.status_code == 404:
    print(f"{search_term} was not found.")