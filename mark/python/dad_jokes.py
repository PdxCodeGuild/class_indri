import requests
import time

# prompt user for search term
search_term = input("Enter a search term: ")

# support for multiple pages
page_num = 1 

# variable to control while loop 
keep_playing = True

#loop the web search
while keep_playing == True:

    # pull search results from current page & return as a dictionary
    url = f"https://icanhazdadjoke.com/search?term={search_term}&page={page_num}"
    response = requests.get(url, headers={'accept':'application/json'}).json()

    # check if the current page is in range
    if page_num > response['total_pages']: 
        print("End of results! Goodbye.")
        break
    # prepare to check the next page on the next loop.
    else:
        page_num += 1

    # return joke value from each item in the result dictionary
    for i in response['results']:
        
        # dramatic effect
        print("Fetching dad joke...")
        time.sleep(1)
        
        #return joke
        print(f"\n{i['joke']}\n") 

        # check to see if we want to keep going
        next_joke = input("Would you like to get another? y/n: ").lower()

        # end parent While loop to quit playing
        if next_joke != "y":
            keep_playing = False
            print("Goodbye!")
            break