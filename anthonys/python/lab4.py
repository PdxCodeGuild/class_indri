# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
# For example, the worked out steps would be:


card_num=[]

user_input='4556737586899855'
for numbers in user_input:
    num_list=int(numbers)
    card_num.append(num_list)

# Slice off the last digit. That is the check digit.
check_digit=card_num[-1]
# print(check_digit)
one_less_card_num=card_num[:-1]
# Reverse the digits.
one_less_card_num.reverse()
#card_num.pop()

#Double every other element in the reversed list.
for sec_number in range(0,len(one_less_card_num), 2):
    one_less_card_num[sec_number]=one_less_card_num[sec_number]*2

#  # Subtract nine from numbers over nine. 
total=0  
for num in range(len(one_less_card_num)):
    if one_less_card_num[num]>9:
       one_less_card_num[num]=one_less_card_num[num]-9
    total=total + one_less_card_num[num]

list_two=[]
list_new=str(total)
for numb in list_new:
    list_two.append(list_new)

print(list_two)



# 5
# Valid!