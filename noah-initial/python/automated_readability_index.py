"""
Automated Readability Index Lab
By Noah Wallis
Class Indri

"""
import requests
import string
punctuation = [".","!","?"]
character_punctuation = list(string.punctuation)
character_punctuation.append(" ")


book_name = "Mobby Dick"
response = requests.get("https://www.gutenberg.org/files/2701/2701-0.txt")
response.encoding = 'utf-8'

response = response.text
response = response.lower()

#To find the number sentences

response_sentences = response
for character in punctuation:
    response_sentences = response_sentences.replace(character, "-")

sentence_counter = 0
sentences = response_sentences.split("-")
for sentence in sentences:
    sentence_counter += 1

#To find the number words

word_counter = 0
words = response.split(" ")

for word in words:
    word_counter += 1

#To find the number of characters

response_characters = response
for character in character_punctuation:
    response_characters = response_characters.replace(character, "")


character_counter = 0
for character in response_characters:
    character_counter += 1

#Calculating ARI with the variables we have created

ari = 4.71 * (character_counter/word_counter) + .5 * (word_counter/sentence_counter) - 21.43
ari = round(ari)
#Dictionary for ARI designation

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

#The final print statement telling you the information gathered from the program
print(f"The ARI for {book_name} is {ari}\nThis corresponds to a {ari_scale[ari].get('grade_level')} level of difficulty\nThat is suitable for an average person {ari_scale[ari].get('ages')} years old!")