
def say_hello(name):
    print("Hello", name)

say_hello("luigi")

#say_hello("mario","red")
#wont work because it only accepts one parameter
def say_hello2(name = "bob",color = "blue" ):#set those as the defualt if you pass nothing through 
    """
    Takes in a name and a color and prints out a messege
    :param name: prints users name
    :param color: color used for the shirt
    """
    #also turns them from positional arguments to keyword arguments
    #^doc string lets you document what your function does so when you mouse over it tells you
    #also turns them from positional arguments to keyword arguments
    print("hello", name)
    print(f"nice {color} shirt")
    
    return "hello"
#say_hello_("mario","red")
#say_hello_("luigi", "green")
#greeting = say_hello_("happy", "carl", "orange")#returns none 
#print(greeting)#prints none


name = input("what is your name? ")
color = input("whats your favorite color? ")

result = say_hello2(name, color)
#doc string isnt required and setting the defaults isnt either (helps tho)
def say_hello3(name: str,color = "Yellow" ):#setting name as a string is a suggestion and itll still take ints 
    """
    Takes in a name and a color and prints out a messege
    :param name: prints users name
    :param color: color used for the shirt
    """
    print("hello", name)
    print(f"nice {color} shirt")
    
    return "hello"

import random 
'''
#ask the user for their grade
user_grade = int(input("what was your grade"))
#figure out the letter grade
user_letter_grade = ""
user_letter_grade
if user_grade >= 90:
    user_letter_grade = "A"
elif user_grade >= 80:
    user_letter_grade = "B"
elif user_grade >= 70:
    user_letter_grade = "C"
elif user_grade >= 60:
    user_letter_grade= "D"
else:
    user_letter_grade= "F"
#get a random number for rivals letter grade
rival_grade = random.randint(0,101)#excludes top number
#figure iut rivals letter grade 
rival_letter_grade = ""
if rival_grade >= 90:
    rival_letter_grade = "A"
elif rival_grade >= 80:
    rival_letter_grade = "B"
elif rival_grade >= 70:
    rival_letter_grade = "C"
elif rival_grade >= 60:
    rival_letter_grade= "D"
else:
    rival_letter_grade= "F"
#output both letter grades and whos score is higher
output = f"""
Your grade was{user_letter_grade}
Your rivals grade was {rival_letter_grade}
"""
if user_grade > rival_grade:
    output+= ("you had the higher grade")
elif user_grade < rival_grade:
    output+= ("our rival beat you this time")
else:
    output+= ("you had the same grade")
'''
#this is messy and a bunch of repeted code there a nicer way to get this done
def calculate_letter_grade(number_grade):
    letter_grade = ""
    if number_grade >= 90:
        user_letter_grade = "A"
    elif number_grade >= 80:
        user_letter_grade = "B"
    elif number_grade >= 70:
        user_letter_grade = "C"
    elif number_grade >= 60:
        user_letter_grade= "D"
    else:
        user_letter_grade= "F"

user_grade = int(input("what grade did you get? "))
rival_grade = random.randint(0,101)

user_letter_grade = calculate_letter_grade(user_grade)#
rival_letter_grade= calculate_letter_grade(rival_grade)#figure out why these are printing as one
output = f"""
Your grade was {user_letter_grade}
Your rivals grade was {rival_letter_grade}
"""
if user_grade > rival_grade:
    output+= ("you had the higher grade")
elif user_grade < rival_grade:
    output+= ("our rival beat you this time")
else:
    output+= ("you had the same grade")
print(output)