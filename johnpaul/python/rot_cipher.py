import string

# get string from user
user_phrase = input("Enter a word or phrase to encrypt: ")

# rotate string by 13 characters
user_phrase = user_phrase.lower()
letters = string.ascii_letters + string.digits + string.punctuation    # "abcdefghijklmnopqrstuvwxyz"
shift = int(input("Enter the amount to rotate: "))
output = ""
for char in user_phrase:
    if char in letters:
        position = letters.index(char) # d => 3
        new_position = (position + shift) % len(letters) # 3 + 13 => 16
        output += letters[new_position] # letters[16] => q
    else:
        output += char

# output the rotated string
print(output)