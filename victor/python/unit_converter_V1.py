conversion = {
    "ft": .3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yard": .9144,
    "inch": .0254
}


distance = float(input("What is the distance? "))
input_units = input("What are the input units? ")
output_units = input("What are the output units? ")
distance_in_meters = round(distance * conversion[input_units], 4)
result = distance_in_meters / conversion[output_units]
print(f"{distance} {input_units} is {result} {output_units} ")