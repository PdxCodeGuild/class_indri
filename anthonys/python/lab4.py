# Let's write a function which returns whether a string containing a credit card number is valid as a boolean.
#  The steps are as follows:

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
# For example, the worked out steps would be:

#Function that loops through a string and makes it into a int and turns to a list
def make_num_list(num_string):
    num_list=[]
    for digit in num_string:
        list_item=int(digit)
        num_list.append(list_item)
    return num_list
    
#Function that checks if the card number is valid
def check_card(user_input):

    # Convert the input string into a list of ints
    card_num=make_num_list(user_input)

    # Slice off the last digit. That is the check digit.
    check_digit=card_num[-1]
    sliced_list=card_num[:-1]

    # Reverse the digits.
    sliced_list.reverse()

    #Double every other element in the reversed list.
    for sec_number in range(0,len(sliced_list), 2):
        doubled_number=sliced_list[sec_number]*2
        #Subtract nine from numbers over nine. 
        if(doubled_number>9):
            doubled_number-=9
        sliced_list[sec_number]=doubled_number


    # Sum all values.
    total=0  
    for num in range(len(sliced_list)):
        total+= sliced_list[num]

    # Take the second digit of that sum.
    list_new=str(total)
    list_two=make_num_list(list_new)

    final_num=list_two[-1]
    return final_num==check_digit

#Ask the User for their card number
user_card=input('What is your card number?')
verdict=check_card(user_card)
#Final output that tells the user if their card is valid
if verdict==True:
    print('Your credit card is Valid!')
else:
    print('Your card is not valid!')
    



# 5
# Valid!