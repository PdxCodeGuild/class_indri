# Unit Converter

# Dictionary containing conversion of unit to meters, with support for yards and inches
convert = {
    "ft" : 0.3048,
    "mi" : 1609.34,
    "m" : 1,
    "km" : 1000,
    "yd" : 0.9144,
    "in" : 0.0254
}

# ask the user for the number
user_distance = input("what is the distance in feet? ")

# ask the user for the unit
user_unit = input("What are the units? ")

#Convert the user distance from user unit to meters
result = int(user_distance) * convert[user_unit]

#return the result
print(result)

