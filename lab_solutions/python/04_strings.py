

# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

def loud_text(text):
    uppercase = text.upper()        # convert to uppercase
    split_text = list(uppercase)    # split sting into list
    output = "-".join(split_text)   # join list together with dashes '-'
    return output

def test_loud_test():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'



# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    output = ""
    for letter in word:
        output += letter * 2

    return output

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

# Count Letter
# Count the number of letter occurances in a string

def count_letter(letter, word):
    
    letter_count = 0
    for char in word:
        if char == letter:
            letter_count += 1

    return letter_count

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2


# Latest Letter
# Return the letter that appears the latest in the english alphabet.

from string import ascii_lowercase
def latest_letter(word):
    letters = ascii_lowercase
    # letters = "abcdefgh"

    highest_index = 0

    for char in word:
        current_index = letters.find(char)
        if current_index > highest_index:
            highest_index = current_index

    return letters[highest_index]

def test_latest_letter():
    assert latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'
    assert latest_letter('abcd') == 'd'
    assert latest_letter('zyx') == 'z'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text: str):
#   return text.count("hi")
    count = 0
    for i in range(len(text) - 1):
        if text[i] + text[i+1] == "hi":
            count += 1

    return count

count_hi("hello")

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi from llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

from string import punctuation
def snake_case(text):
    text = text.lower()
    for punct in punctuation:
        text = text.replace(punct, "")
    text = text.replace(" ", "_")

    return text

def test_snake_case():
    assert snake_case('Hello World!') ==  'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

def camel_case(text):
    text = snake_case(text)
    words = text.split("_")

    for i in range(1, len(words)):
        words[i] = words[i].title()

    return "".join(words)

camel_case('This is another example.')

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

## Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text):
    text = list(text)
    for i in range(0, len(text), 2):
        text[i] = text[i].upper()

    return "".join(text)

alternating_case("hi there")

def test_alternating_case():
    assert alternating_case('Hello World!') ==  'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'


# type conversion
dict()
tuple()
int()
float()
str()
list()