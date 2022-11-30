# Quotes API
import requests
import json

# page counter and search term
page = 1
keyword = input("Enter a keyword to search for quotes: ")

# run loop
while True:

    url = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
    response = requests.get(url, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}).json()
    
    # print(json.dumps(response, indent=0)) # inspect return data 
    # break

    # return the quotes with authors
    for i in response['quotes']:
        print(f"\n{i['body']}\n–– {i['author']}\n")

    # keep going, search again or exit
    # if on the last page, don't suggest to search the next page.
    if response['last_page'] == True:
        fork = input("Last page! Enter 'new search' or 'done': ").lower()
        page = 1 # reset page count  
    else:
        fork = input("Enter 'next page', 'new search' or 'done': ").lower()
    
    # multiple interpretations
    next_page = ['next page', 'next', 'nex', 'nxt', 'np']
    new_search = ['new search', 'new','search', 'ns']
    
    if fork in next_page and response['last_page'] == True: # loop back to the first page if the user types next page while on the last page
        continue

    if fork in next_page: # loop on the next page
        page += 1
    elif fork in new_search: # loop with a new search term
        keyword = input("Enter a keyword to search for quotes: ")
    else:                 # exit loop
        print("Goodbye!")
        False
        break