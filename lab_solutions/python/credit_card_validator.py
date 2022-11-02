
# card_number = input("Enter your credit card number(not a scam): ")
card_number = "4556737586899855"

def make_number_list(number_string: str):
    number_list = []
    for digit in number_string:
        list_item = int(digit)
        number_list.append(list_item)

    return number_list

# Convert the input string into a list of ints
try:
    card_number = make_number_list(card_number)
except ValueError:
    print("Invalid card number")
    exit()

# Slice off the last digit. That is the check digit.
check_digit = card_number.pop()

# Reverse the digits.
card_number = card_number[::-1]

# Double every other element in the reversed list.
for i in range(len(card_number)):
    if i % 2 == 0:
        card_number[i] = card_number[i] * 2
        # Subtract nine from numbers over nine.
        if card_number[i] > 9:
            card_number[i] = card_number[i] - 9

# Sum all values.
total = str(sum(card_number))

# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
if int(total[1]) == check_digit:
    print("Valid")
else:
    print("Invalid")


### Map demo
# card_number = "123456789"

# card_number = list(map(int, card_number))

# def transform(num):
#     num *= 2
#     if(num > 9):
#         num -= 9
#     return num

# print(list(map(transform, card_number)))



# a = [1, 2, 3, 4, 5]
# b = a[::2]

# print(a)
# print(b)