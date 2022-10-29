#Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:


# user input credit card digits
user_input = "455673758689855"
# print(type(user_input))

#Convert the input string into a list of ints
user_input = list(user_input)
print(user_input)

# Slice off the last digit. That is the check digit.
def valid_credit_card(user_input):
    sliced_off_digit = user_input[: -1]
    return sliced_off_digit

result = valid_credit_card(user_input)
# print(result)

# Reverse the digits. 
def digit_reversed(user_input): 
    new_list = user_input[::-1]
    return new_list

new_result = digit_reversed(result)
print(new_result)



'''We can get sublists using square brackets and colons [::], this is called slicing. 
# The first number is the starting index, the second is the ending index, and the third is the increment. 
# If you leave out the first number, it's implied to be the beginning. 
# If you leave out the second number it's implied to be the end. 
# If you leave out the third number, it's implied to be 1'''

# Double every other element in the reversed list.
num = []
for x in new_result[::2]:
    x = int(x)
    x = num.append(x * 2)

print(num)

# Subtract nine from numbers over nine.

# Sum all values.

# Take the second digit of that sum.

# If that matches the check digit, the whole card number is valid.