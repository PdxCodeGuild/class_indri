# Convert the input string into a list of ints
# test 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5

credit_card = input("Please enter your Credit Card number in this format(ex: 1 2 3 4 5 6): ")
string_list = credit_card.split(" ")
cc_list = [int(num) for num in string_list]

# Slice off the last digit. That is the check digit.

check_digit = cc_list.pop()

# Reverse the digits.

rev_cc = cc_list[::-1]

# Double every other element in the reversed list.

for i in range(0, len(rev_cc), 2):
    rev_cc[i] *= 2
    
# Subtract nine from numbers over nine.

for i in range(0, len(rev_cc)):
    if rev_cc[i] > 9:
        rev_cc[i] -= 9
        
# Sum all values.

cc_total = sum(rev_cc)

# Take the second digit of that sum.

cc_total_str = str(cc_total)
cc_second_digit = int(cc_total_str[1:])

# If that matches the check digit, the whole card number is valid.
if cc_second_digit == check_digit:
    print("Your card is valid!")
else:
    print("Not valid!")
    print(check_digit, cc_second_digit, rev_cc)
