'''
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.
'''

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
prompt = input("Whats your message?\n ").lower()
shift = int(input("Enter the amount of rotation:\n"))
output = ""
# Allow the user to input the amount of rotation used in the encryption.
shift = shift % 26
if direction == "decode":
    shift *= -1

for char in prompt:
    if char in ALPHABET:
        position = ALPHABET.index(char)
        new_position = position + shift
        output += ALPHABET[new_position]


print(f"Your {direction}d phrase is now:\n{output}")
    


