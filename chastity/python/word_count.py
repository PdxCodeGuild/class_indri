'''

Count Words Lab 06 - Python 
Chastity Boykin 
PDX Code Guild Class Indri

'''
import requests
import string
# send a request to get book 

'''
Author 	Leinster, Murray, 1896-1975
Title 	Men into space 
'''
url = "https://www.gutenberg.org/cache/epub/69299/pg69299.txt"
response = requests.get(url)
response.encoding = 'utf-8' # set encoding to utf-8
book = response.text
#print(book)

# 1.  Make everything lowercase, strip punctuation, split into a list of words.

translator = str.maketrans('', '', string.punctuation)
no_punct = book.translate(translator)
book_list = no_punct.lower().split()

# print(book_list)
# returns list of words that have been converted to lowercase and stripped of punctuation

# 2. Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
word_dict = {}
# iterate through book_list and ad 1 to each coresponding key value
for i in book_list:
    if i in word_dict:
        word_dict[i] += 1 # increase its count by 1 
    else:
        word_dict[i] = 1 # add the word into the word_dict 
    #print(word_dict)

# 3. Print the most frequent top 10 out with their counts. You can do that with the code below.

words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])