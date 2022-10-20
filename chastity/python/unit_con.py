# Unit Converter

# dictonary listing out convertions for meters
distance_units = {
    'foot': 0.3048,
    'mile': 1609.34,
    'meter': 1,
    'km': 1000,
    'yard': 0.9144,
    'inch': 0.0254
}

# ask the user the distance and unit they would like to convert

quantity = int(input('What is the distance? '))
input_unit = input("What are the input units? ")
output_unit = input("What are the output units? ")

# convert input_unit to meters 
meter_per = distance_units[input_unit]

# calcutalte the total in meters
total_input_unit = quantity * meter_per

distance_per = distance_units[output_unit]

total = int(distance_per) / total_input_unit

print (f'{quantity} {input_unit} is {round(total, 4)} {output_unit}.') # round to the 4 decimal

