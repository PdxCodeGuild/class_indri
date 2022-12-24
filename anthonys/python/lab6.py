import requests
import string
response = requests.get('https://www.gutenberg.org/cache/epub/69289/pg69289.txt')
response.encoding = 'utf-8' # set encoding to utf-8
book_response=response.text

book=book_response.replace('”', '')
book=book_response.replace('  ', ' ')

for character in string.punctuation:
    book_response = book.replace(character,'')

book_list=book_response.split(' ')

word_count={}
for word in book_list:
    word=word.lower()
    if word in word_count:
        word_count[word]+=1

    else:
        word_count[word]=1


# word_dict is a dictionary where the key is the word and the value is the count

words = list(word_count.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
 