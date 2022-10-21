
from hashlib import new


print('''
Unit Options:
1. feet
2. miles
3. meters
4. kilometers
''')

#Version 1 
## Ask the user for the number of feet, and print out the equivalent distance in meters
# one_feet = 0.3048
# number_of_distance = float(input("What is the number of distance?: "))
# result = round(number_of_distance * one_feet, 3)
#print(f"{number_of_distance} ft is {result} m")


#=====================================================================================================#

#Version 2
## Allow the user to also enter the units. Then depending on the units, convert the distance into meters.
metrics = {
    "feet": 0.3048, 
    "miles": 1609.34, 
    "meters": 1, 
    "kilometers": 1000,
    "ft": 0.3048, 
    "mi": 1609.34, 
    "m": 1, 
    "km": 1000
}

# user_input_unit = input("What are the units?: ").lower()

# if user_input_unit in metrics:
#     print(f'{int(number_of_distance)} {user_input_unit} is {int(number_of_distance * metrics[user_input_unit])} m ')
# else:
#     print("Input error! please try again")

#=====================================================================================================#
# Version 3
## Add support for yards, and inches.

metrics["yard"] = 0.9144
metrics["inch"] = 0.0254

# user_input_unit = input("What are the input units?: ").lower()

# # if user_input_unit in metrics:
# #     print(f'{int(number_of_distance)} {user_input_unit} is {int(number_of_distance * metrics[user_input_unit])} m ')
# # else:
# #     print("Input error! please try again")


# #=====================================================================================================#

#Version 4
## ask the user for the distance, the starting units, and the units to convert to.



while True:
    try:
       number_of_distance = float(input("What is the number of distance?: "))
    except:
        print ("Input error! please input number only")
        continue
    user_input_unit = input("What are the input units?: ").lower()
    user_output_unit = input("What are the output units?: ").lower()
    if user_input_unit in metrics and user_output_unit in metrics:
        new_value = round(number_of_distance * metrics[user_input_unit]/ metrics[user_output_unit], 5)
        print(f'{number_of_distance} {user_input_unit} is {new_value} {user_output_unit}')
        break
    else:
        print("Input Error! Please try again")

   