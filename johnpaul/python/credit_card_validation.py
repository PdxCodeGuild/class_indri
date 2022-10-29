#Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:


# user input credit card digits
user_input = input("Enter your credit cared number: ")
# print(type(user_input))

#Convert the input string into a list of ints
user_input = list(map(int, user_input))
print(user_input)



# Slice off the last digit. That is the check digit.

popped_digit = user_input.pop()
print(user_input)

# Reverse the digits. 
def digit_reversed(user_input): 
    new_list = user_input[::-1]
    return new_list

new_result = digit_reversed(user_input)
print(new_result)

# Double every other element in the reversed list.
for i in range(len(new_result)):
    if i % 2 == 0:
        new_result[i] = new_result[i]*2
        # print(new_result)
      
print(new_result)       
# Subtract nine from numbers over nine.
for x in range(len(new_result)):
    if new_result[x] > 9:
        new_result[x] = new_result[x] - 9
#        print(sum(new_result)) # Sum all values.

print(new_result)
print(sum(new_result))
# Take the second digit of that sum.
net = (sum(new_result)) % 10
print(net)

# If that matches the check digit, the whole card number is valid.
final_check = net - popped_digit
if final_check == 0:
    print("Valid!")
else:
    print("Invalid")
