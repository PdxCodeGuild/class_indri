import requests
import string

response = requests.get('https://www.gutenberg.org/cache/epub/120/pg120.txt')
response.encoding = 'utf-8' # set encoding to utf-8
book = (response.text).lower()

# Take the following steps to build up our dictionary. The result should look something like {'a': 3, 'the': 4}

# Make everything lowercase, strip punctuation, split into a list of words.
punct = string.punctuation + '' + '//' 
book = book.translate(str.maketrans('', '', punct))
book_list = book.split(" ")

# Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
word_dict = {}


word_pair_list = [book_list[i:i+2] for i in range(0, len(book_list), 2)]

for word_pair in word_pair_list:
    word_pair = tuple(word_pair)
    if word_pair not in word_dict:
        word_dict[word_pair] = 1
    else:
        word_dict[word_pair] += 1

# Print the most frequent top 10 out with their counts. You can do that with the code below.

# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
    

# Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.