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
#print('''
#you can print
#a multi line statment
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
"""
temperature = input("what is the current temperature outside?(using a whole number) ")
temperature = int(temp)
#print(type(temp))
#print(temp)
if temperature >= 80:
    print("its a hot day out today")
elif temperature <= 79 and temp >= 60:
    print("its a nice day today")
elif temperature < 60:
    print("its cold today")
"""
#error handling
'''
"""
temperature = input("what temperature is it outside? ")
try:
    temperature = int(temperature)
except:
    print("something wrong...")
    exit()
if temperature >= 80:
    print("its a hot day out today")
elif temperature <= 79 and temp >= 60:
    print("its a nice day today")
elif temperature < 60:
    print("its cold today")
"""
#not a good way to handle error just kicks you out if you do something wrong
'''
while True:
    temperature = input("what is the temperature outside? ")
    try:
        temperature = int(temperature)
        break
    except:
        print("invalid input enter just the digits of the temp.")
if temperature >= 80:
    print("its a hot day out today")
elif temperature <= 79 and temperature >= 60:
    print("its a nice day today")
elif temperature < 60 and temperature > 40:
    print("its cold today")
else:
    print("its freezing outside")
'''
# not good because the except will trigger on any error and not just the text error
#if you know something will cause an error but dont know what kind run it and then add the type error

# try / except
'''
try:
    dict = {}
    dict["potato"]
except KeyError:
    print("this key does not exist.")
'''
# dictionaries {}

#keys on left value on right 
example = {}# makes  a dictionarie
'''
foods = {
    "apple": 1,
    "orange": 1.5,
    "banana":1,
    "spinach":2
}

foods["tomato"] = 3#you can add to your dict anywhere below you can also update values this way
print(foods)#prints whole food dict
print(foods["orange"])#prints the value of orange
foods["banana"] = 2
print(foods["tomato"])#useing something you dont have causes a key error
del foods["spinach"]# deletes key and value
print(foods)
#adding food to the dict in the program
'''
'''
new_food = input("enter a food to add or 'done' to exit: ")
food_price = input(f"enter the price of {new_food}: ")
food_price = float(food_price)
foods[new_food] = food_price
'''
'''
print(foods)

while True:
    new_food = input("enter a food to add or 'done' to exit: ")
    if new_food == "done":
        break
    food_price = float(input(f"enter the price of {new_food}: "))

    foods[new_food] = food_price
    print(foods)

food_lookup = input("enter a food name to get the price.")
try:
    reply = foods[food_lookup]
except KeyError:
    print(f"{food_lookup} does not exist")
else:
    print(f"the price of {food_lookup} does not exist")

'''
#lists []
foods =["potato","tomato","grape","kiwi"]
print(foods[1])
#first thing in a list is at index 0
#negative values start at the bottom of the list
#putting in a index that doesnt exist causes a IndexError
foods.append("pineapple")#adds pineapple to end of the list
#foods[0] = "apple" # overwrites whatever was in the specifed index 


#removed_item = foods.pop(1)#save removed items for use later
#foods.remove("grape")#removes item and returns nothing

if "potato" in foods:
    print("hey! Potato isnt a fruit!")
else:
    print("only fruits here :)")

#print(foods[0])
#print(foods[1])
#print(foods[2])
#print(foods[3])

#for food in foods:#^does the same thing 
#    print(food)


#for i in range(len(foods)):#^same thing prints items in the range of the length of the foods list
#    print(foods[i])

#print(foods[1:2])#get all the foods from index 1 and up to but not including index 2 
#print(foods[0:3:2])#3rd number is the step and its how many indexes you move at a time
#print(foods[::-1])#prints list backwords if left blank it does entire list
#[start:stop:step]