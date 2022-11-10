''' Let's compute the ARI for a given book. 
The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. 
'''

import requests
import math

url = "https://www.gutenberg.org/cache/epub/46/pg46.txt"
response = requests.get(url)
response.encoding = 'utf-8'
given_text = response.text

# number of characters
characters = len(given_text) 
print(f"Total characters: ", characters)

# remove characters that may interfere with sentence detection.
items_to_remove = ["\t","\n","\r","\v","\f", ",", ":", "'", "-", "/", "*", "@", "$", "\"", ";"]
for i in items_to_remove:
    given_text = given_text.replace(i, "")

# number of words
words = len(given_text.split())
print("Total words:", words)

# split string into a list of sentences based on punctuation used to end a sentence.
punctuation = [".","!","?"]
for i in punctuation:
    given_text = given_text.replace(i, "|")
sentence = given_text.split("|")
# print(*sentence, sep="\n") # testing

sentences = len(sentence) #number of sentences
print("Total sentences:", sentences)

# ARI formula
# If the result is a decimal, always round up
score = math.ceil(4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43)

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
