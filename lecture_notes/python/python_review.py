
# strings

'This is another string'

"That is Mike's house"

'"water is wet" - some guy'

# integer
from multiprocessing.sharedctypes import Value


12

# floats
2.7

# function
# print(message) # another comment


multi_line_message = '''
This is a
multiline comment
'''

# print(multi_line_message)

"""
This is also
a multiline
comment
"""

# users_fav_color = input("Enter your favorite color: ")
# print(users_fav_color, "That is also my favorite color", 5, 3.2)
# print("This is a separate line")
# print(f"The color {users_fav_color} is awesome!")

# print(3 + 2.4)  # 5.4
# print(5 - 2)    # 3
# print(10 / 2)   # 5.0
# print(11 // 2)  # 5
# print(2 * 3)    # 6
# print(3  ** 2)  # 9

# print(20 * "=")

# print(10 % 3)   # 1
# print(10 % 2)   # 0

# Booleans
True
False

message = "Hello World"

# if (some condition):
# if message != "hello world":
#     print("This statement was true")
# elif message == "Hello World":
#     print("HELLOOOOO")
# else:
#     print("The statement was NOT true")

'''
while True:
    temperature = input("Enter the current temperature (as a whole number): ")
    try:
        temperature = int(temperature)
        break
    except ValueError:
        print(f"'{temperature}' is not a valid number")


if temperature >= 80:
    print("It is hot outside!")
elif temperature <= 79 and temperature > 60:
    print("It is a nice day.")
else:
    print("It is a bit chilly")
'''
'''
# try / except
try:
    dict = {}
    dict["potato"]
except KeyError:
    print("that key does not exist")
except TypeError:
    print("uh oh")
'''

'''
# dictionaries
foods = {
    "apple": 1,
    "orange": 1.5,
    "banana": 1,
    "spinach": 2
}

foods["tomato"] = 3

foods["banana"] = .75

del foods["spinach"]


while True:
    new_food = input("Enter a food to add or 'done' to quit: ")
    if new_food == "done":
        break
    price_of_food = float(input(f"Enter the price of {new_food}: "))

    foods[new_food] = price_of_food


print(foods)


food_lookup = input("Enter a food name to get price: ")
try:
    reply = foods[food_lookup]
except KeyError:
    print(f"{food_lookup} does not exist")
else:
    print(f"The price of {food_lookup} is ${reply}")
'''



foods = ["potato", "tomato", "grape", "kiwi"]

foods.append("pineapple")

foods[0] = "apple"

removed_item = foods.pop(1)
foods.remove("grape")

# print(foods)
# print(removed_item)

if "potato" in foods:
    print("Hey! Potato is not a fruit!")
else:
    print("Only fruits here :)")


# print(foods[0])
# print(foods[1])
# print(foods[2])

# for food in foods:
#     print(food)

# for i in range(len(foods)):
#     print(foods[i])

# ["apple", "kiwi", "pineapple"]
print(foods[1:2:1])   # [start:stop:step]
