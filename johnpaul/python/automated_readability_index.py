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




import string
import requests

# analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal.

# Find a book on Project Gutenberg: 
    # BOOK USED: The Project Gutenberg eBook of Treatment of hemorrhoids, and other
    # non-malignant rectal diseases, by William Penn Agnew

# send a request to that url using the requests library to get the text into Python


base_url = "https://www.gutenberg.org/cache/epub/69288/pg69288.txt"
response = requests.get(base_url) 
response.encoding = 'utf-8-sig' # set encoding to utf-8 

# Print response to verify that website is responding. Response [200] implies that means that your request was successful

if response.status_code == 200:
    book_text = response.text 
    book = book_text.lower() # convert all text to lower case
    # print(book)

#Total number of words
word_count = 0
for word in book:
    if word == " ":
        word_count +=1
#print(word_count)
    


# Splits the text into sentences
sentence_count = 0
for sentence in book:
    if sentence.endswith(". ") or sentence.endswith("? ") or sentence.endswith("! "):
        sentence_count = 1
    else:
        sentence_count += 1
#print(sentence_count)

# Count the total number of characters

list_characters = list(book)
x = list(string.ascii_lowercase)

count_character = 0
for letters in list_characters:
    if letters in x:
        count_character += 1
#print(count_character)


characters = count_character
words = word_count
sentences = sentence_count


ari_formular = ((4.71 * (characters/words)) + (0.5 * (words/sentences))) - 21.43
rounded_ari_formular = round(ari_formular)
# print(round(ari_formular))
    
grade_level_difficulty = (ari_scale[rounded_ari_formular]['grade_level'])
# print(grade_level_difficulty)

average_person = (ari_scale[rounded_ari_formular]['ages'])
# print(average_person)

print(f"""
--------------------------------------------------------
The ARI for gettysburg-address.txt is {rounded_ari_formular}
This corresponds to a {grade_level_difficulty} level of difficulty
that is suitable for an average person {average_person} years old.
--------------------------------------------------------""")
