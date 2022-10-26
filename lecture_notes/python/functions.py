def say_hello(name, color = "Yellow"):
    print("Hello", name)
    print(f"Nice {color} shirt you have.")

    return "Hello"

def say_hello2(name: str, color = "Yellow"):
    """
    Takes in a name and a color and prints out a message
    :param name: str prints out users name
    :param color: str color used for their shirt
    """
    print("Hello", name)
    print(f"Nice {color} shirt you have.")

    return "Hello"




# say_hello("happy", "Mario", "red")
# print("===============")
# say_hello("moody", color="gray", name="John")

# name = input("What is your name: ")
# color = input("What is your favorite color: ")

# result = say_hello(name)
# result = say_hello2(4)









import random

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


# Ask the user for their grade
user_grade = int(input("What was your grade: "))

# Figure out their letter grade
user_letter_grade = calculate_letter_grade(user_grade)

# Get a random number grade your rival
rival_grade = random.randint(0, 101)

# Figure out rivals letter grade
rival_letter_grade = calculate_letter_grade(rival_grade)

# Output both the users and rivals letter grades as well as who won
output = f"""
Your grade was {user_letter_grade}
Your rivals grade was {rival_letter_grade}
"""

if user_grade > rival_grade:
    output += "You had the higher grade"
elif user_grade < rival_grade:
    output += "Your rival beat you this time"
else:
    output += "You had the same grade. Hope your not cheating...."

print(output)