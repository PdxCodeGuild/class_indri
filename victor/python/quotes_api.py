import requests

'''
The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.
'''
page = 1
answer = input("Would you like to receive a list of quotes?:\n").lower()
keyword = input("Enter a Keyword:\n")
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

while True:
    
    response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers=headers)
    quote = response.json()

    if answer == 'yes':
        for i in range(len(quote['quotes'])):
            print(f'''*==============================================*
{quote['quotes'][i]['body']}''')

        page_answer = input("\nWould you like to check the next page?:\n").lower()

        if page_answer == 'no':

            answer = input("Would you like to receive a different list of quotes?:\n").lower()           
            if answer == 'no':
                print('Have a nice day!')
                break
            keyword = input("Enter a Keyword:\n")

        page += 1

    else:
        break
    



'''
The Favqs Quote API also supports getting a list of quotes associated with a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword. You can use string concatenation to build the URL.
'''
