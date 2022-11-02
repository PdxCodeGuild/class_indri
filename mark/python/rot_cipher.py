'''Rot Cipher
Write a program that prompts the user for a string, and encodes it with ROT13. 

For each character, find the corresponding character, add it to an output string. 

Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m



Version 2

Allow the user to input the amount of rotation used in the encryption. (ROTN)

Version 3 (optional)

Add support for capital letters, numbers, and special characters. These can be handled in two different ways:

Capital letters can be rotated as well, numbers and special characters can be put directly into the output (e.g. "hello world!" becomes "uryyb jbeyq!").

Instead of using an alphabet of just letters, include numbers, spaces, and special characters as well.'''
import string

miniscule = list(string.ascii_lowercase)
capitalized = list(string.ascii_uppercase)
# print(alphabet)

#take in a letter, return a letter 13 places to the right]
def rot_cipher(letter):
    
    if letter in miniscule:
        letter_index = miniscule.index(letter)
        try:
            rotation = miniscule[letter_index + 13]
        except IndexError:
            rotation = miniscule[(letter_index+13) % len(miniscule)]
        return rotation

    if letter in capitalized:
        letter_index = capitalized.index(letter)
        try:
            rotation = capitalized[letter_index + 13]
        except IndexError:
            rotation = capitalized[(letter_index+13) % len(capitalized)]
        return rotation

    else:
        return letter

# print(rot_cipher("l"))

user_input = input("Enter a word or phrase: ")

cipher_list = []

for i in user_input:
        cipher_list.append(rot_cipher(i))

output = "".join(cipher_list)

print(output)


