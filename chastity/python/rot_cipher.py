'''

ROT13 Caesar cipher Lab 05 - Python
Chastity Boykin 
PDX Code Guild Class Indri

'''

'''

Write a program that prompts the user for a string, and encodes it with ROT13. 
For each character, find the corresponding character, add it to an output string. 

'''

import string

phrase = input("Enter a phrase to encrypt: ")
shift_rot = int(input("Enter a number to rotate: "))

def rot13(phrase): # ord() to get the Unicode of each letter in a word calculate the new value and use chr() to convert it back to letters.
    return ''.join([chr((ord(letter) - 97 +(shift_rot)) % 26 + 97) 
        if 97 <=ord(letter) <= 122
        else letter
    for letter in phrase.lower()])

print(rot13(phrase))