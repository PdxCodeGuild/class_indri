
# strings


message = "Hello World" # variable 
'This is another string' 

"That is Mike's house"

'"water os wet" - some guy'

# integer
12 

# floats
2.7 

# function
# print(message) # print function with take input and output it 

"""
This is a
Multi line 
comment
"""

'''This is a
Multi line 
comment''' # string that you can print


#user_fav_color = input("What is your favorite Color: ") # assign variable to input
#print(user_fav_color, "Is a cool color!")
#print("This is a separate line")

#print(f"The color{user_fav_color} is awesome!")

# print(3 + 2.4) # 5.4
# print(5 -2 )   # 3
# print(10 / 2) # 5.0
# print(11 // 2) # 5
# print(2 * 3)  #6
# print(3 ** 2) #9

# print(20 * "=") 

# print(10 % 3) # 1
# print(10 % 2) # 0

# Booleans
True
False

message = "Hello World"

# if (some condition):
# if message != "hello world": # != not true
#     print("This statment was true")
# if message == "Hello World": #elif only the 1st with run if true
#     print("HELLOOOOO")
# else:
#     print("This statment was NOT true")

'''
# try and accept block

while True:
    temperature = input("Enter the current temperature (as a whole number): ")
    try:
        temperature = int(temperature)
        break
    except:
        print(f"'{temperature}' is not a valid number")

    
if temperature >= 80:
    print("It's hot outside!")
elif temperature <= 79 and temperature > 60:
    print("It is a nice day.")
else:
    print("It is a bit chilly")


# try /except
try:
    dict = {}
    dict["potato"]
except KeyError:
    print("that key does not exist")
'''


'''
# dictonaries
foods = {
    "apple": 1,
    "orange": 1.5,
    "banana": 1,
    "spinach": 2
}

# print(foods) # entire dic

# print(foods["apple"]) # one item price

# foods["tomato"] = 3
# print(foods["tomato"]) # add new food

# foods["banana"] = .75
# print(foods["banana"]) # update value

# del foods["tomato"]
# print(foods["tomato"]) #remove a Key value

# add new food to dictonary
while True:
    new_food = input("Enter a food to add or 'done' to quit: ")
    if new_food == "done"
        break
    price_of_food = float(input(f"Enter the price of {new_food}: "))

    foods[new_food] = price_of_food

print(foods)

#look up price of food
food_lookup = input("Enter a food name to get price")
try:
    reply = [food_lookup]
except KeyError:
    print(f"{food_lookup} does not exist")
else:
    print(f"The price of {food_lookup} is ${reply}")
'''

# Lists
'''
foods = ["potato", "tomato", "grape", "kiwi"]

# print(foods) # print list

foods.apend("pineapple") # add new food
removed_item = foods.pop(1)

# print(foods [0]) # one item use index 0,1,2,3

foods.pop(1) #remove items

'''