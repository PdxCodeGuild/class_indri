import string
user_string=input('Input a statement:').lower()
user_shifts=int(input("How much do you want it to shift?"))


def encryted_message(user_statement, user_shift):
    letters=string.ascii_lowercase
    shifted = letters[user_shift:] + letters[:user_shift]
    letter_map=str.maketrans(letters, shifted)
    encryted_output=user_statement.translate(letter_map)
    return encryted_output

output=encryted_message(user_string, user_shifts)
print(output)














#Notes
# def make_list():
#     alphbait=[]
#     letters=string.ascii_lowercase
#     for letter in letters:
#         alphbait.append(letter)
#     return alphbait
# letters=make_list()
# print(letters)

