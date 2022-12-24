'''

Automated Readability Index Lab 07 - Python
Chastity Boykin 
PDX Code Guild Class Indri

'''

import requests, re, math

file_name = "Men into Space"
url = "https://www.gutenberg.org/cache/epub/69299/pg69299.txt"
response = requests.get(url)
response.encoding = 'utf-8'  # set encoding to utf-8
book = response.text


# Change all end punc to periods
new_book = re.sub("\?", ".", book) + re.sub("\!", ".", book) + re.sub('\"', ".", book)

# get sentence count
sentences = 0
sentences = book.count(".")

# get word count 
 
words = book.lower().split(' ')  # all words lower case & split in list of words
num_words = len(words)  # count all words

# get character count
characters = book.replace(" ", "") # remove empty char
num_characters = len(characters) # count all characters

# Calculate ARI score

ari = 4.71 * (num_characters/num_words) + 0.5 * (num_words/sentences) -21.43
ari = math.ceil(ari)  # rounds a number upward to its nearest interger
if ari > 14:
        ari = 14

# look up age range and grade level

ari_scale = {
    1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages': '6-7', 'grade_level': '1st Grade'},
    3: {'ages': '7-8', 'grade_level': '2nd Grade'},
    4: {'ages': '8-9', 'grade_level': '3rd Grade'},
    5: {'ages': '9-10', 'grade_level': '4th Grade'},
    6: {'ages': '10-11', 'grade_level': '5th Grade'},
    7: {'ages': '11-12', 'grade_level': '6th Grade'},
    8: {'ages': '12-13', 'grade_level': '7th Grade'},
    9: {'ages': '13-14', 'grade_level': '8th Grade'},
    10: {'ages': '14-15', 'grade_level': '9th Grade'},
    11: {'ages': '15-16', 'grade_level': '10th Grade'},
    12: {'ages': '16-17', 'grade_level': '11th Grade'},
    13: {'ages': '17-18', 'grade_level': '12th Grade'},
    14: {'ages': '18-22', 'grade_level': 'College'}
}

grade_level = ari_scale[ari]

# Output

output = '-'*60+ '\n'
output += "The ARI for " + file_name + " is " + str(ari) + '\n'
output += "This corresponds to a " + grade_level['grade_level'] + " Grade level of difficulty\n"
output += "That is suitable for an average person " + grade_level['ages'] + " years old.\n"
output += '-'*60

print(output)