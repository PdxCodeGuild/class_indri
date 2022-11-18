import string
import requests
# analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal.

# Find a book on Project Gutenberg: 
    # BOOK USED: The Project Gutenberg eBook of Treatment of hemorrhoids, and other
    # non-malignant rectal diseases, by William Penn Agnew

# send a request to that url using the requests library to get the text into Python


base_url = "https://www.gutenberg.org/cache/epub/69288/pg69288.txt"
response = requests.get(base_url) 
response.encoding = 'utf-8-sig' # set encoding to utf-8 

# Print response to verify that website is responding. Response [200] implies that means that your request was successful

if response.status_code == 200:
    book_text = response.text 
    book = book_text.lower() # convert all text to lower case
    book = book.translate(str.maketrans('', '', string.punctuation)) # REMOVE all punctuations
    book = book.translate(str.maketrans('', '', string.digits)) # REMOVE all numbers
    # print(book) # prints out the text from the url
else:
    print("The url connection is unsuccessful!")
    exit()

# split text into a list of words

list_book_text = book.split() # Split a string into a list where each word is a list item
# print(list_book_text)

# create a dictionary with words as keys and counts as values

dict_book_text = {}
for words in list_book_text:
    if words not in dict_book_text:
        dict_book_text[words] = 1

    else:
        dict_book_text[words] += 1
# print(dict_book_text)


# Print the most frequent top 10 out with their counts.

words = list(dict_book_text.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse= True) # sort largest to smallest, based on count
for i in range(min(10, len(words))): # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
