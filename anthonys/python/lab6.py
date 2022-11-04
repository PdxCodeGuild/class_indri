import requests
import string
response = requests.get('https://www.gutenberg.org/cache/epub/69289/pg69289.txt')
response.encoding = 'utf-8' # set encoding to utf-8
book_response=response.text

book_response.replace('\n', ' ')
book_response.replace('\r', ' ')

for character in string.punctuation:
    book_response = book_response.replace(character, ' ')


book_list=book_response.split(' ')
print(book_list)

# word_count={}
# for word in book_list:
#     word=word.lower()
#     if word in word_count:
#         word_count[word]+=1
#     else:
#         word_count[word]=1
# print(word_count)