# Count Words
import requests
import os, string

'''
Take the following steps to build up our dictionary. The result should look something like {'a': 3, 'the': 4}
'''

response = requests.get('https://www.gutenberg.org/cache/epub/10234/pg10234.txt')
response.encoding = 'utf-8' # set encoding to utf-8
print(response.text)

book = open("response.txt" "r")
# 1.  Make everything lowercase, strip punctuation, split into a list of words.

def clean_text(text):
  # returns list of words that have been converted to lowercase and stripped of punctuation
    translator = str.maketrans('', '', string.punctuation)
    no_punct = text.translate(translator)
    return no_punct.lower().split()


# # 2. Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.

# split the sentence into words.
# iterate thorugh every word

word_dict = {}
for word in response.text:
# add the word into the word_dict initalize with 0
  if word not in word_dict:
    word_dict[word] = 0
# increase its count by 1   
  word_dict[word] =+ 1



# 3. Print the most frequent top 10 out with their counts. You can do that with the code below.
# word_dict is a dictionary where the key is the word and the value is the count
# word_dict = {'apples': 2, 'bananas': 1, 'pears': 1, 'kiwi': 7}
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])