import requests
from os import system
import time

# base_url = f"https://favqs.com/api/qotd"

# #get a random quote
# response = requests.get(base_url, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

# #parse the JSON in the response into a python dictionary
# results = response.json()
# results = results.get('quote') 
# for item in range(len(results)):
#     x = results['author'] 
#     y = results['body']

# # show the quote and the author.
# print(f'\nQuote: {y}. By author: {x}')

#===========================================================================================#
# Version 2: List Quotes by Keyword

#Prompt the user for a keyword
key_word = input('Enter keyword to search: ')
prompt = input("enter 'page number' or 'done': ")

if prompt == 'done'.lower():
    exit()
else:

    #list the quotes you get in response
    base_url = f"https://favqs.com/api/quotes?page={prompt}&filter={key_word}"

    response = requests.get(base_url, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

    #parse the JSON in the response into a python dictionary
    results = response.json()
    last_page = results.get('last_page')
    quotes = results.get('quotes')


    while last_page == False:
        for word in range(len(quotes)): 
            print(word+1, quotes[word]['body'], "By:", quotes[word]['author'])
            print()
        break
      






#prompt the user to either show the next page or enter a new keyword










