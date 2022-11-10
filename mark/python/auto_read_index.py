''' Let's compute the ARI for a given book. 
The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. 
'''

import requests
import math

url = "https://www.gutenberg.org/files/11/11-0.txt"
response = requests.get(url)
response.encoding = 'utf-8'
given_text = response.text

# number of characters
characters = len(given_text) 
print(f"Total characters: ", characters)

# remove characters that may interfere with sentence detection.
items_to_remove = ["\n","\r",",",";","'s", "@", "&","*","(",")","#","!","%","=","+","-","_",":", '"',"'"]
for i in items_to_remove:
    given_text = given_text.replace(i, " ")

# number of words
words = len(given_text.split())
print("Total words:", words)

punctuation = [".","!","?","-"]
for i in punctuation:
    given_text = given_text.replace(i, "|")
sentence = given_text.split("|")
print("Total sentenches: ", *sentence, sep="\n")
sentences = len(sentence) #number of sentences
print("Total sentences:", sentences)



# The score is computed by multiplying the number of characters divided by the number of words by 4.71, 
# adding the number of words divided by the number of sentences 
# multiplied by 0.5, 
# and subtracting 21.43. 
# If the result is a decimal, always round up, and if the result is higher than 14, it should be set to 14

score = (4.71 * (characters / words)) + (0.5 * (words / sentences)) - 21.43

if score is float:
    score = round(score)
if score > 14:
    score = 14

print(f"your score is:", math.ceil(score))
# print(score)

#Scores correspond to the following ages and grad levels:
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

# The output should look something like the following:

'''
--------------------------------------------------------
The ARI for gettysburg-address.txt is 12
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.
--------------------------------------------------------
'''