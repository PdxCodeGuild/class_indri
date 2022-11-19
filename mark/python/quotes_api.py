# Quotes API

import requests
import json

# The Favqs Quote API also supports getting a list of quotes associated with a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>

page = 1
keyword = input("Enter a keyword to search for quotes: ")

while True:
    
    url = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
    response = requests.get(url, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}).json()
    
    # print(json.dumps(response, indent=0)) # inspect return data 
    for i in response['quotes']:
        print(f"\n{i['body']}\n–– {i['author']}\n")

    fork = input("Enter 'next page', 'new search' or 'done': ").lower()
    
    if fork == 'next page':
        page += 1
    elif fork == 'new search':
        keyword = input("Enter a keyword to search for quotes: ")
    else:
        print("Goodbye!")
        False
        break