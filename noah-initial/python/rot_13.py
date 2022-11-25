"""
Rot 13 Cipher Lab
By Noah Wallis

"""
import string
# creating all possible inputs for a password including puncutation and digits
letters = string.ascii_letters + string.digits + string.punctuation
#asking what the password they would like to encrypt and lowering it to make it easier to code with and possible to use capitals
password = input("What password would you like to encrypt?: ")
password = password.lower()
#asking how many times they would like to rotate their password
rotate_amount = int(input("How many times would you like to rotate this password?: "))
#blank variable for holding output
output = ""
#for loop rotating letter by the desired amount using our letters variable
for letter in password:
    if letter in letters:
        position = letters.index(letter)
        new_position = (position + rotate_amount) % len(letters)
        output += letters[new_position]

    else:
        output += letter

print(f"Your new password is: {output}")
