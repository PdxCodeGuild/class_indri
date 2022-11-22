"""

Credi Card Validation Lab
By Noah Wallis

"""
#taking input for card number
card_number = input("Enter your credit card number: ")
# Convert the input string into a list of ints
def make_number_list(number_string: str):
    number_list = []
    for number in number_string:
        list_item = int(number)
        number_list.append(list_item)

    return number_list 

card_number = make_number_list(card_number)

# Slice off the last digit. That is the check digit.
check_digit = card_number[-1]
del card_number[-1]

# Reverse the digits.
card_number.reverse()

# Double every other element in the reversed list.
card_number[0::2] = [i * 2 for i in card_number[0::2]]

# Subtract nine from numbers over nine.
for i in range(len(card_number)):
    if card_number[i] > 9:
        card_number[i] = card_number[i] -9

# Sum all values.
total = [sum(card_number)]
total = str(total)

# Take the second digit of that sum.
test_check_digit = int(total[2])
# If that matches the check digit, the whole card number is valid.
if test_check_digit == check_digit:
    print("Your card number is valid!")
else:
    print("Your card number is not valid!")