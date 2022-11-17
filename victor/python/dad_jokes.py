import requests
'''
Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.
'''
header = {
    "accept": "application/json"
}


while True:
    response = requests.get('https://icanhazdadjoke.com/', headers=header)
    joke = response.json()
    answer = input("Would you like to hear a joke? Type 'yes' or 'no':\n")
    if answer == 'yes':
        print(f"{joke['joke']}")
    elif answer == 'exit':
        break
    else:
        print("Too bad!")
        print(f"{joke['joke']}")
'''
Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search term and go through jokes one at a time. You can also add support for multiple pages.
'''