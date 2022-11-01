'''
Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.
'''

# Create a variable for testing code

user_input = int(input("Enter a number from 0-999: "))


# Create three dictionary: single digits, double digits and 10s

single_digits = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

tens_digits = {
    0: "",
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen"
}

double_digits = {
    0: "",
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

# finding the indvidual digits

ten_digit = user_input // 10
single_digit = user_input % 10
hundred_digit = user_input // 100

# print(ten_digit)
# print(single_digit)
# # print(f'{double_digits[ten_digit]}-{single_digits[single_digit]}')



if user_input < 100:
    if ten_digit == 1:
        print(f'{tens_digits[single_digit]}')
    elif user_input < 10:
        print(f'{single_digits[single_digit]}')
    elif single_digit == 0:
        print(f'{double_digits[ten_digit]}')
    else:
        print(f'{double_digits[ten_digit]}-{single_digits[single_digit]}')


# Handling numbers from 100-999
else:
    ten_digit = user_input // 10 % 10
    if ten_digit == 1:
        print(f'{single_digits[hundred_digit]} hundred {tens_digits[single_digit]}')
    elif user_input < 10:
        print(f'{single_digits[hundred_digit]} hundred {single_digits[single_digit]}')
    elif single_digit == 0:
        print(f'{single_digits[hundred_digit]} hundred {double_digits[ten_digit]}')
    else:
        print(f'{single_digits[hundred_digit]} hundred {double_digits[ten_digit]}{single_digits[single_digit]}')



