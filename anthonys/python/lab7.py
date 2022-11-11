import requests
import string
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
URL='https://www.gutenberg.org/cache/epub/69289/pg69289.txt'
response = requests.get(URL)
response.encoding = 'utf-8' # set encoding to utf-8
book=response.text
book_words=response.text.lower()
sentence_book=response.text.lower()
end_characters=list('"!.;?')
#-----------Sentence Find-------------------
for end_character in end_characters:
    sentence_book=sentence_book.replace(end_character, '@')

sentence_list=sentence_book.split('@')

sentence_count=0
for sentence in sentence_list:
    sentence_count+=1

#--------Word Find-------------

book_words=book_words.replace('”', '')
book_words=book_words.replace('  ', ' ')

for character in string.punctuation:
    book_words = book_words.replace(character,'')

book_list=book_words.split(' ')

word_count=0
for word in book_list:
    word_count+=1

#------Find Character----------
characters_amount=len(book_words)

#---------Formula------------

#Here I use the ARI formula and then round that number to the nearest whole number
ARI=round(((4.71*(characters_amount/word_count))+(.5*(word_count/sentence_count))-21.43))

#Here I print the output for the user to see
print(f'''The ARI for {URL} is {ARI} This corresponds to a {ari_scale[ARI]['grade_level']} 
level of difficulty that is suitable for an average person {ari_scale[ARI]['ages']} years old.''')


# --------------------------------------------------------
# The ARI for gettysburg-address.txt is 12
# This corresponds to a 11th Grade level of difficulty
# that is suitable for an average person 16-17 years old.
# --------------------------------------------------------