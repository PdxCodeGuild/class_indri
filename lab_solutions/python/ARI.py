import requests

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

# response = requests.get("https://www.gutenberg.org/cache/epub/120/pg120.txt")
# response.encoding = "utf-8"

with open("book.txt") as file:
    response = file.read()

license_start = response.find("*** END OF THE PROJECT GUTENBERG EBOOK")

book = response[0:license_start].lower()

characters = len(book.replace("\n", "").replace("\t", ""))
sentences = 0

for char in book:
    if char == "." or char == "?" or char == "!" or char == "'" or char == '"':
        sentences += 1

word_count = 0

# Chose ∆ as common character to split by
book = book.replace("\n", "∆").replace("  ", " ").replace(" ", "∆").replace("\t", "∆")
words = book.split("∆")


# print(characters)
# print(len(words))
# print(sentences)

ARI = 4.17 * (characters / len(words)) + .5 * (len(words) / sentences) - 21.43

score = min(round(ARI), 14)


print(f"""
--------------------------------------------------------
The ARI for Treasure Island is {score}
This corresponds to a {ari_scale[score].get('grade_level')} level of difficulty
that is suitable for an average person {ari_scale[score].get('ages')} years old.
--------------------------------------------------------
""")