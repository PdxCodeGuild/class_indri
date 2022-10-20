from_units = input("what unit of measurment are you using? ft,mi,m,km,yd,in ")
input_dist = input("what is the distance you are converting? ")
to_units = input("what unit of measurment are you converting to? ft,mi,m,km,yd,in ")
input_dist = float(input_dist)
measurments = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1 ,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254,
    }
conversions = {
    "ft":3.280,
    "mi":0.000621371,
    "m":1,
    "km":0.001,
    "yd":1.09361,
    "in":39.3701,
      }

meters = input_dist * measurments[from_units]

converted_number = meters*conversions[to_units]
print(f'{input_dist} {from_units} is {converted_number} {to_units}')