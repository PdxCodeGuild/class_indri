
measure = {
    'm': 1,
    "ft": .3048,
    'mi' : 1609.34,
    'km' : 1000,
    'inch': .0254,
    'yard': .9144

}
# Ask the user amount of distance
user_input= float(input('What is the distance?'))
#Ask the user what input units
user_units=input('What are the units? (mi, km, ft, m, inch, yard)')
#Here I convert the user input to a key in the directory and assign it to a varable 
value_dict=measure[user_units]
#Here I do the math to find the meters
meters=round(value_dict*user_input, 2)
#Ask the user what units they want outputed
output_units= input('What are the output units?')
#Here I am doing the math with meters found to user desired unit output
desired_measured=meters/measure[output_units]
#Here I print out the results
print(f'{user_input} {user_units} is {desired_measured} {output_units}')

#--------Outcome----------
#  what is the distance? 100
# > what are the input units? ft
# > what are the output units? mi
# 100 ft is 0.0189394 mi