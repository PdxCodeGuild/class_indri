# Credit Card Validation Lab
'''
    If that matches the check digit, the whole card number is valid.
'''

# card_number = ('4556737586899855')

# 1. Convert the input string into a list of ints

card_number = list(input("Enter Credit Card Number: ").strip())
'''
passing a string to the list function the default behaviour split every character in the string into different list items. 
'''
# print(card_number)

# 2. Slice off the last digit. That is the check digit.

check_digit = card_number.pop()
'''
pop method allows to very neatly remove and store the check digit.
'''
# print(check_digit)

# 3. Reverse the digits

card_number.reverse()
'''
clean way of reversing the card number
'''

# 4. Double every other element in the reversed list

process_num = [] # to store our modified digits

for index, num in enumerate (card_number):
    '''
    enumerate adds a counter to an iterable and returns it in a form of enumerating object
    '''
    if index % 2 == 0:
        double_num = int(num) * 2 
        ''' 
        convert the num to an integer and double the value
        '''
       
#  5. Subtract nine from numbers over nine

        if int(double_num) > 9:
            double_num = int(double_num) - 9 

        process_num.append(double_num)
    else:
        process_num.append(int(num)) 
        '''
        need to convert num to an integer call append to add the integer to process_nums 
        '''
    # index = index + 1

# 6. Sum all values

total = str(sum(process_num))
'''
need to convert it back to string  after converting to int
'''

print(total)

# 7. Take the second digit of that sum.

get_second_num = (total[1])
"""
returns second digit of number
"""
# print(get_second_num)

# 8. If that matches the check digit, the whole card number is valid.

if get_second_num == check_digit:
    print("Valid!")
else:
    print("Invalid!")