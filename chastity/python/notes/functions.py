# Functions

def say_hello(name: str, color): # def defins the function will recall later anytime used
    print("Hello", name)
    print(f"Nice {color} shirt yout have.")

    return "Hello"

def say_hello2(name: str, color): # def defins the function will recall later anytime used
    '''
    Takes in a name and a color and prints out a message
    :param name: str prints out users name
    :param name: str color used for their shirt
    '''
    # give more detail on the function
    
    print("Hello", name)
    print(f"Nice {color} shirt yout have.")

    return "Hello"


    # say_hello("Mario", "red") 
    # print("=================")
    # say_hello("Luigi")

# name = input("What is your name: ")
# color = input("What is your favorite color: ")

# result = say_hello(name, color)








import random
# # Ask the user for thier grade
# user_grade = int(input("What was your grade: "))

# # figure out their letter grade
# user_letter_grade = ""
# if user_grade >= 90:
#     user_letter_grade = "A"
# elif user_grade >= 80:
#     user_letter_grade = "B"
# elif user_grade >= 70:
#     user_letter_grade = "C"
# elif user_grade >= 60:
#     user_letter_grade = "D"
# else:
#     user_letter_grade = "F"

# # Get a randome number grade your rival
# rival_grade = random.randint(0, 101)

# # Figure out rivals letter grade
# rival_letter_grade = ""
# if rival_grade >= 90:
#     rival_letter_grade = "A"
# elif rival_grade >= 80:
#     rival_letter_grade = "B"
# elif rival_grade >= 70:
#     rival_letter_grade = "C"
# elif rival_grade >= 60:
#     rival_letter_grade = "D"
# else:
#     rival_letter_grade = "F"
# # Output both the user and rivals letter grades as well as who won
# print(f"""
# Your grade was {user_letter_grade}
# Your rivals grade was {rival_letter_grade}
# """)

# if user_grade > rival_grade:
#     print("You had the higher grade")
# elif user_grade < rival_grade:
#     print("Your rival beat you this time")


def calculate_letter_grade(number_grade: int):
    """
    Calculates a letter grade from an integer
    """
    letter_grade = ""
    if number_grade >= 90:
        letter_grade = "A"
    elif number_grade >= 80:
        letter_grade = "B"
    elif number_grade >= 70:
        letter_grade = "C"
    elif number_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade


# Ask the user for thier grade
user_grade = int(input("What was your grade: "))

# figure out their letter grade
user_letter_grade = calculate_letter_grade(user_grade)

# Get a randome number grade your rival
rival_grade = random.randint(0, 101)

# Figure out rivals letter grade
rival_letter_grade = calculate_letter_grade(user_grade)

# Output both the user and rivals letter grades as well as who won
print(f"""
Your grade was {user_letter_grade}
Your rivals grade was {rival_letter_grade}
""")

if user_grade > rival_grade:
    print("You had the higher grade")
elif user_grade < rival_grade:
    print("Your rival beat you this time")