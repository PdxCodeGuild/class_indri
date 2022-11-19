"""
Quotes Api Lab
By Noah Wallis

"""
import requests
import json
import time

def quote_retriever(page, keyword):
    base_url = f"https://favqs.com/api/quotes?page={page}&filter={keyword}"

    response = requests.get(base_url, headers= {
        'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
    })
    response = response.text
    response = json.loads(response)
    return response

keyword = input("Enter a keyword to search for in quotes!: ")


def quote_printer(response):
    quote_counter = 1

    while quote_counter <25:
        print(response["quotes"][quote_counter]["body"])
        print("--------------------------------------------")
        quote_counter += 1
        time.sleep(1)



next = "y"
new_keyword = "y"
page = 1

while True:
    

    if next == "y" and new_keyword == "y":
        print(f"Retrieving quotes with the keyword {keyword}...")
        time.sleep(2)
        response = quote_retriever(page, keyword)
        quote_printer(response)
        

    elif next == "y" and new_keyword == "n":
        page = page + 1
        print(f"Showing page {page} of these quotes...")
        time.sleep(2)
        response = quote_retriever(page, keyword)
        quote_printer(response)

    elif next == "n" and new_keyword == "y":
        keyword = input("What would you like your new keyword to be?: ")
        page = 1
        print(f"Showing quotes with the new keyword {keyword}...")
        time.sleep(2)
        response = quote_retriever(page, keyword)
        quote_printer(response)

    else:
        print("That is all hope you enjoyed!")
        break

    next = input("Would you like to display the next page? y/n: ")
    new_keyword = input("Would you like to use a new keyword? y/n: ")

