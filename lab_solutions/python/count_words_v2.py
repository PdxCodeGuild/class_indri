import requests
import string
import re
import time

def print_top_ten(counts):
    # Print the most frequent top 10 out with their counts.
    words = list(counts.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])




url = "https://www.gutenberg.org/cache/epub/120/pg120.txt"
response = requests.get(url)
response.encoding = 'utf-8' # set encoding to utf-8
start = time.time()
book = response.text.lower()


# Make everything lowercase, strip punctuation, split into a list of words.
pattern = r"\b([a-z’-]+)\b"
word_list = re.findall(pattern, book)


# Your dictionary will have words as keys and counts as values.
word_counts = {}
for word in word_list:
    # If a word isn't in your dictionary yet, add it with a count of 1.
    if word not in word_counts:
        word_counts[word] = 1
    # If it is, increment its count.
    else:
        word_counts[word] += 1

word_pair_counts = {}
for i in range(len(word_list) - 1):
    pair = word_list[i] + " " + word_list[i + 1]
    if pair not in word_pair_counts:
        word_pair_counts[pair] = 1
    else:
        word_pair_counts[pair] += 1


print_top_ten(word_counts)
print("=============")
print_top_ten(word_pair_counts)
end = time.time()
print("Code took:", end - start)