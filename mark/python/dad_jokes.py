import requests
url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers={'accept':'application/json'}).json()

joke = response["joke"]

print(joke)