import requests

search_term = input("Enter a search term: ")
page_num = 1 
keep_playing = True
while keep_playing == True:
    url = f"https://icanhazdadjoke.com/search?term={search_term}&page={page_num}"
    response = requests.get(url, headers={'accept':'application/json'}).json()

    #support for multiple pages
    if page_num > response['total_pages']: 
        print("End of the line! Goodbye.")
        break
    else:
        page_num += 1

    # return joke from each result one at a time
    for i in response['results']:
        print(f"\n{i['joke']}\n")
        # check to see if we want to keep going
        next_joke = input("Would you like to get another? y/n: ").lower()

        # end parent While loop to quit playing
        if next_joke != "y":
            keep_playing = False
            break