import requests
import time


# base_url = "https://icanhazdadjoke.com/"

# response = requests.get(base_url, headers={'accept': "application/json"})

# # Print response to verify that website is responding. Response [200] implies that means that your request was successful
# if response.status_code == 200:
#     dad_joke = response.json()
# else:
#     print("Unsuccessful request")

# for key, value in dad_joke.items():
#     if key == 'joke':
#         print(key,':', value)


#VERSION 2
#Create a REPL (Read, Evaluate, Print, Loop) that allows one to enter a search term and go through jokes one at a time.#

search_joke = input('would you like to search for a joke? (y/n): ')
if search_joke == 'y'.lower():
    search_term = input('Enter a term(default: list all jokes): ')
    base_url = f"https://icanhazdadjoke.com/search?term={search_term}"
    response = requests.get(base_url, headers={'accept': "application/json"})
    dad_joke = response.json()
    result = dad_joke["results"]
    new_result = {}
    for items in result:
        new_result.update(items)
        for key, value in new_result.items():
            if key == 'joke':
                print(key,':', value)
else:
    print("That's a joke! Bye")




