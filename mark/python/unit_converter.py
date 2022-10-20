# Unit Converter

# Dictionary containing conversion of unit to meters
convert = {
    "ft" : 0.3048
}

# Ask the user for the number of feet
user_distance = input("what is the distance in feet? ")

#Convert the user distance from feet to meters
result = int(user_distance) * convert["ft"]

#return the result
print(result)

