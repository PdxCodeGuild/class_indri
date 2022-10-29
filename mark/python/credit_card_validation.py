# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:
import random
#randomly generated card for testing
test = random.choices(range(0,9), k=16)

# Request a 16 digit credit card number, reject incorrect input
while True:
    # prompt
    user_input = input("Please enter a 16 digit credit card number:\n")

    # check for test card
    if user_input == "test":
        user_card_num = test
        break 

    try: #try to format the list, and if we can't restart the loop.
        
        f_input = "".join(user_input.split()) #delete spaces from the input string
        user_card_num = [int(i) for i in f_input] # Convert input string to a list of integers
    
        # print(user_card_num) # test
        if len(f_input) == 16: # validate length of list
                break # Great Success! move on with the program.
        else:
            print("\nThat is not a valid card number.\n")

    except: # Can't format, try again.
        print("\nThat is not a valid card number.\n")


# Slice off the last digit. That is the check digit.
check_digit = user_card_num.pop(-1)

# Reverse the digits.
user_card_num.reverse()

# Double every other element in the reversed list.
for i in range(0, len(user_card_num), 2):
    user_card_num[i] *= 2

# Subtract nine from numbers over nine.
for i in range(0, len(user_card_num)):
    if user_card_num[i] > 9:
        user_card_num[i] -= 9
    
# Sum all values.
sum = str(sum(user_card_num))
print(sum[1])

# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
if int(sum[1]) == check_digit:
    print("Valid!")
else:
    print("invalid!")



# For example, the worked out steps would be:
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!
