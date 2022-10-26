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

# convert input_unit to unit value
meter_per = distance_units[input_unit]

# calcutalte the total in meters
input_unit_meter = quantity * meter_per

#print(f'{quantity} is {round(input_unit_meter, 4)} m.') # round to the 4 decimal 

distance_output = distance_units[output_unit] #converting out put unit value

total = input_unit_meter / int(distance_output) # dividing meter by output unit

print (f'{quantity} {input_unit} is {round(total, 7)} {output_unit}.') # round to the 7 decimal

