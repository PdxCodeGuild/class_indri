import requests
from os import system
import time
import json
from API_quote_token import quotetoken

#===========================================================================================#

#VERSION 1: Get a Random Quote
base_url = f"https://favqs.com/api/qotd"
response = requests.get(base_url, headers = quotetoken)

#parse the JSON in the response into a python dictionary
results = response.json()
results = results.get('quote') 
x = results['author'] 
y = results['body']

#Adding delayed response and clear terminal for good user view
print('Fetching quote.........')
time.sleep(1)
system('clear')

# show the quote and the author.
print(f'Quote: {y}. By author: {x}')
