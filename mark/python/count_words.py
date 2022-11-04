'''
Lab 15: Count Words
Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. 
Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg and navigate to the plain-text version. 
You can then send a request to that url using the requests library to get the text into Python. 
You can also save the file into the same folder as the .py file and open it using with.
'''
import requests
import string
# The result should look something like {'a': 3, 'the': 4}

response = requests.get("https://www.gutenberg.org/files/11/11-0.txt")
response.encoding = 'utf-8'

# Make everything lowercase
book = response.text.lower()
# strip punctuation 
book = book.translate(str.maketrans('','',string.punctuation)) # this way is faster...

# for i in book:                                                  # but this one returns more results...
#     if i not in string.ascii_letters and i != " ":
#         book = book.replace(i, "")


# #split into a list of words.
book = str.split(book, " ")

# # Your dictionary will have words as keys and counts as values. 
word_count = {}
# If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
for word in book:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

# sort the dictionary items by value from greatest to least. Returns a list of tuples
sorted_word_count = sorted(word_count.items(), key=lambda tup: tup[1], reverse = True) 

# Print the most frequent top 10 out with their counts.
for i in range(min(10, len(sorted_word_count))):
    print(sorted_word_count[i])

# Version 2 (optional)

# Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

# Version 3 (optional)

# Let the user enter a word, then show the words which most frequently follow it.