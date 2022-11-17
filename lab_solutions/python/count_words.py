import requests
import string
import re
import time

url = "https://www.gutenberg.org/cache/epub/120/pg120.txt"
response = requests.get(url)
response.encoding = 'utf-8' # set encoding to utf-8
start = time.time()
book = response.text.lower()


# Make everything lowercase, strip punctuation, split into a list of words.
pattern = r"\b([a-z’-]+)\b"
word_list = re.findall(pattern, book)


# book = book.replace("\n", " ")
# for i in book:
#     if i not in string.ascii_letters and i != " ":
#         book = book.replace(i, "")

# word_list = book.split(" ")


# Your dictionary will have words as keys and counts as values.
word_counts = {}
for word in word_list:
    # If a word isn't in your dictionary yet, add it with a count of 1.
    if word not in word_counts:
        word_counts[word] = 1
    # If it is, increment its count.
    else:
        word_counts[word] += 1


# Print the most frequent top 10 out with their counts.
words = list(word_counts.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

end = time.time()
print("Code took:", end - start)