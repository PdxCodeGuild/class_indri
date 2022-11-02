'''Write a program that prompts the user for a string, and encodes it with ROT13. 
For each character, find the corresponding character, add it to an output string. 
Notice that there are 26 letters in the English language, so encryption is the same as decryption.'''
import string

lower_case = list(string.ascii_lowercase) #support for lowercase characters
upper_case = list(string.ascii_uppercase) #support for uppercase characters

# take in a character & if a letter, return a rotated letter according to the chosen step.
def rot_cipher(character, step):
    # check for letter case & if the letter is supported,     
    if character in lower_case:     
        # take the index position of the letter,
        letter_index = lower_case.index(character)    
        # apply the step
        rotation = lower_case[(letter_index+int(step)) % len(lower_case)] # store value at index position for (letter index plus step) divided by list length.
        # return the value at the stepped index position
        return rotation
    #samesies but for upper case
    if character in upper_case:
        letter_index = upper_case.index(character)
        rotation = upper_case[(letter_index + int(step)) % len(upper_case)]
        return rotation
    # numbers and special characters can be put directly into the output
    else:
        return character

# print(rot_cipher("l"))

user_phrase = input("Enter a word or phrase: ")
user_step = input("Input the amount of rotation: ")

# list of rotated letters
cipher_list = []

# run every position in the input string through the rot_cipher function & add the result to our list of rotated letters
for i in user_phrase:
        cipher_list.append(rot_cipher(i, user_step))

# join the list into a string
output = "".join(cipher_list)

#return the encrypted string
print(output)


