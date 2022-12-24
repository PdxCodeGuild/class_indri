"""
Dad Joke Api Lab
By Noah Wallis

"""
import requests
import json

#uses search term to find category of jokes
search_term = input("Choose a category to search for dad jokes in!: ")

#base url used to find jokes
base_url = "https://icanhazdadjoke.com/search?term="

# grabs the base url as well as the search term to find a json text of jokes
response = requests.get(base_url + search_term, headers={
    'accept': 'application/json'
})

#turns response into text
response = response.text

#turns text into python data
response = json.loads(response)

#shows how many jokes are available
available_jokes = len(response['results']) - 1

#variable for while loop to allow for viewing of multiple jokes
keep_going = "y"

#while loop using above variable to loop
while keep_going == "y":

    #uses user input to display desired joke number
    joke_number = int(input(f"There are {available_jokes} jokes available. Pick a number 0 - {available_jokes} to show that joke: "))

    #prints the joke at user designated joke number
    print(response['results'][joke_number]['joke'])

    #used to determine if you would like to keep viewing jokes
    keep_going = input("Would you like to keep going? y/n: ")

#end of code goodbye
print("Hope you enjoyed the jokes! :)")