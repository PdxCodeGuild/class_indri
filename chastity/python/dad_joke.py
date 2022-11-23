'''

Dad Joke 09 - Python
Chastity Boykin 
PDX Code Guild Class Indri

'''
import requests


# requests library to send an HTTP request

search_term = input("Would you like to hear a joke? Type 'yes' or 'no': ")
url = "https://icanhazdadjoke.com/"

# with the accept header as application/json.

headers = {
    'accept': 'application/json',
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    joke = response.json()

    if search_term == 'yes':
        print(f"{joke['joke']}")
    
    elif search_term == 'no':
        print("Bye!")