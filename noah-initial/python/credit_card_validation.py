# Convert the input string into a list of ints
from ctypes import c_double


card_number = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5]
print(card_number)
# Slice off the last digit. That is the check digit.
check_digit = card_number[-1]
del card_number[-1]
print(card_number)
# Reverse the digits.
card_number.reverse()
print(card_number)
# Double every other element in the reversed list.
doubled = [i * 2 for i in card_number[0:15:2]]
print (doubled)
# Subtract nine from numbers over nine.
doubled_new = [n - 9 for n in doubled if n >= 9 ]
print(doubled_new)
    
# Sum all values.
total = [sum(doubled_new + card_number[1:15:2])]
print(total)

# Take the second digit of that sum.
second_of_sum = ""
# If that matches the check digit, the whole card number is valid.
if second_of_sum == check_digit:
    print("Your card number is valid!")
else:
    print("Your card number is not valid!")