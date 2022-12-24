from dataclasses import replace
import string

string_ascii_list = list(string.ascii_lowercase)

#print(string_ascii_list)


# 1) Prompts the user for a string

prompt = input("Enter letters: ")

prompt = prompt.replace(" ", "") # remove spaces if any

# Allow the user to input the amount of rotation used in the encryption. (ROTN)
user_rotn_input = int(input("input number of rotation: "))

prompt_list = list(prompt) # convert to list of string



# 2) Encodes it with ROT13


for char in prompt_list:
    output =[]
    output += [string_ascii_list.index(char)]
    for num in output:
        # print(num)
# 3) For each character, find the corresponding character, add it to an output string
        if num + user_rotn_input < 26:
            print(string_ascii_list[num + user_rotn_input], end="\n")
        if num + user_rotn_input > 26:
            print(string_ascii_list[num + user_rotn_input - 26], end="\n")




# Version 2: 
## 
        




