import requests
from os import system
import time
import json
from API_quote_token import quotetoken

#===========================================================================================#
# Version 2: List Quotes by Keyword

def quote_api(keyword, page):
        #parse the quotes you get in response
        base_url = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
        response = requests.get(base_url, headers = quotetoken)

        #parse the JSON in the response into a python dictionary
        results = response.json()
        # print(results)

        # Defines what page is displayed
        quotes = results.get('quotes')
        last_page = results.get('last_page') 
        result_page = results.get('page')

      
        
        for word in range(len(quotes)):
            if last_page == False and quotes[word]['body'] == 'No quotes found':
                print('No quotes found.') 
            elif last_page == False or last_page == True:
                print(word+1, quotes[word]['body'], "By:", quotes[word]['author'])
                print()
            
            


# prompt the user to either show the next page or enter a new keyword

keyword = input('Enter keyword to search or done to exit: ').lower()
if keyword == 'done':
    exit()
page = input("enter page number, or 'done': ")
if page == 'done':
    exit()
else:
    page = int(page)
quote_api(keyword, page)
print()

#Navigating page

navigate_page = input('Enter next page, previous page, or done to exit: ')
while navigate_page != 'done':
    if navigate_page == 'next page':
        page += 1
    if navigate_page == 'previous page':
        page -= 1
    quote_api(keyword, page)
    print()
    navigate_page = input('Enter next page, previous page, or done to exit: ')  

print('Exiting quote....')
time.sleep(1)
system('clear')