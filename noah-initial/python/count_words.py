"""
Count Words Lab
By Noah Wallis

"""

import requests
import string
response = requests.get('https://www.gutenberg.org/cache/epub/69283/pg69283.txt')
response.encoding = 'utf-8'
print(response.text)
response = response.text
# dictionary holding all words in the text!
word_dict = {

}

punctuation = list(string.punctuation)


# response = "Hello, my name is Noah Wallis! How are you doing today? Hello name you today" #testing code

#This part will make it lower case and get rid of punctuation with nothing
response = response.lower()
for character in punctuation:
    response = response.replace(character, "")

# print(response)

#this part will split the str of response into a list of individual words by using a space as a seperator
response = response.split(" ")
# print(response)

#This part will add words to our dictionary or add a value if they already exist in that dictionary
for word in response:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

#Code from lab to list top 10 words! (credit to lab creator)
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])