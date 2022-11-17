import requests
import math

url = "https://www.gutenberg.org/cache/epub/120/pg120.txt"
response = requests.get(url)
response.encoding = 'utf-8'
book_end = response.text.find("*** END OF THE PROJECT")
book_start = response.text.find("*** START OF THE PROJECT")
book = response.text[book_start:book_end]


book = book.replace("\n", "µ").replace("  ", " ").replace("\t", "µ").replace(" ", "µ").replace("'", "µ").replace('"',"µ")

# number of characters
characters = len(book) 

# number of words
words = len(book.split("µ"))

# split string into a list of sentences based on punctuation used to end a sentence.
sentences = book.count(".") + book.count("!") + book.count("?")

# ARI formula
ARI = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
# If the result is a decimal, always round up
score = math.ceil(ARI)
print(score)

# if the result is higher than 14, it should be set to 14
if score < 1:
    score = 1
if score > 14:
    score = 14

# Scores correspond to the following ages and grad levels:
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# output
print(f"""
The ARI for {url} is {score}.
This corresponds to a {ari_scale[score]['grade_level']} level of difficulty.
That is suitable for an average person {ari_scale[score]['ages']} years old.
""")

print(characters)
print(words)
print(sentences)
