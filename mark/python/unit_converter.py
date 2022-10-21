# Unit Converter

# Dictionary containing conversion for unit to meters
# support for yards and inches
convert = {
    "ft" : 0.3048,
    "mi" : 1609.34,
    "m" : 1,
    "km" : 1000,
    "yd" : 0.9144,
    "in" : 0.0254
}

while True:
    # ask the user for the number
    user_distance = input("what is the distance? ")

    # ask the user for the unit
    from_unit = input("What are the input units? ")

    # ask the user what to convert to
    to_unit = input("what are the output units? ")

    # Convert the user distance from user unit to meters
    meters = int(user_distance) * convert[from_unit]

    # Convert from meters to the desired unit
    result = meters * (1/convert[to_unit])

    #return the result
    print(f"{user_distance} {from_unit} is {result} {to_unit}")