'''
import random
print("hello world")
playerchoice = input("welcome to rock paper scissors what is your choice? ")
choices = ["rock","paper","scissors"]
computer = random.choice(choices)
if playerchoice == computer:
    print("you tied")
'''
""""
#strings
"hello world"
'hello world'
'"incoming fire has the right of way"- unkown'
#intgers
12

#float
1.22

'''
multi line
comment
'''

'''
another 
multline
comment
'''

"""
print('''
you can print
a multi line statment
''')
"""

#variabels
message = "a variable has data stored in it and is re usable"
print(message)

#inputs dont work unless saved as a variable
favcolor = input("whats your favorite color? ")
print(f"{favcolor} is my favorite color too!")
print(favcolor,12,"everything in the print statment goes to the same line")
print("this is a seperate line")
#adding strings puts them together 
print("mar"+"ley")
#adding ints adds them together
print(5+5)
#adding ints and strings doesnt work
#print(5+"blue")
#adding int and floats together works
print(5+5.5) # 10.5

print(3+2.4) # 5.4

print(5-2) # 3

print(10/2) # 5.0 division always returns a float

print(10//2) # 5 floor division will return a int but will round down

print(2*3) # 6

print(3 ** 2) #9 three to the power of 2

print(3* "hello") #prints hello 3 times

print(10 % 3) # 1 takes the remainder of division

print(10 % 2) # 0 2 goes into 10 even no remainder

print(11 % 2) # 1 if you % a odd number by 2 it will always come back 1
print(10 % 2) # 0 if you % a even number by 2 it will always come back 0

#booleans- setting conditions -always capital
True
False
#conditional statement
# if (some condition):
if True:
    print("this is a true statement")

if 10 > 2:
    print("this statement is true")

if favcolor == "blue":
    print(f"{favcolor} is my favorite to")
else:
    print(f"{favcolor} is an okay color but its not my favorite ")
#== check for equality
#!= check for inequality
word = "hello world"
if message == "hello world":
    print("this statment is true")
if word == "Hello World":
    print("helloooo")
else:
    print("this statement was true")
#elif only the first thing that is true will be executed the rest will be skipped
"""

temp = input("what is the current temperature outside?(using a whole number) ")
temp = int(temp)
print(type(temp))

if temp >= 80:
    print("its a hot day out today")
elif temp <= 79 and temp >= 60:
    print("its a nice day today")
elif temp < 60:
    print("its cold today")
