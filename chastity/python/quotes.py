'''

Quotes API 10 - Python
Chastity Boykin 
PDX Code Guild Class Indri

'''
import requests, json

# ----------------- Version 1 ----------------------- #

# # Settting our responses with url and json
# response = requests.get("https://favqs.com/api/qotd")
# # Using json method to load our request as text
# data = json.loads(response.text)['quote']
# # Setting our quote to a variable
# print('Quote of the Day:\n')
# print(f"\n{data['body']} \n– {data['author']}")




# ----------------- Version 2 ----------------------- #

# variables for page and keyword search
page = 1
keyword = input("Enter Keyword to serach for quotes: ").lower()
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

# Function to get API information 
def pull_quotes():
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    url = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"
    # set response with headers
    response = requests.get(url, headers=headers)
    # json to load requests as text
    data = json.loads(response.text)['quotes']
    print(f'{len(data)} quotes associated with {keyword} - page {page}\n')
    # use a for loop with enumerate to print quote and number
    for index, quote in enumerate(data):
        print(index+1, quote['body'], "\n")


# Ask user for user inputs utilizing while loop to pull info
while True:
    # Call function
    pull_quotes()
    # Setting the user keyword value
    keyword_val = input("Enter 'next' to see more results, or 'new' for new keyword: ").lower()
    # Use if/else statements to filter through pages, reset, or exit
    if keyword_val == 'next':
        page += 1
        pull_quotes()
    elif keyword_val == 'new':
        page = 1
        search_term = input("Enter Keyword to serach for quotes: ").lower()
        pull_quotes()
    else:
        print("Goodbye!")
        break
    