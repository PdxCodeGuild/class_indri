distances = {
    "meters":0.3048,
    "feet":1,
    "miles": 1609.34,
    "kilometers":1000,
    "yards": 0.9144,
    "inches": 0.0254
}


unit_measured_one = input("What unit would you like to measure?: ")
unit_measured_two = input(f"What unit would you like to convert {unit_measured_one} to?: ")
amount_measured = float(input(f"How many {unit_measured_one} would you like to convert to {unit_measured_two}?: "))

unit_measured_one_in_meters = distances[unit_measured_one] * amount_measured
unit_measured_two_in_meters = distances[unit_measured_two] * distances["meters"]

answer = unit_measured_one_in_meters / unit_measured_two_in_meters
print(f"{amount_measured} {unit_measured_one} converted to {unit_measured_two} is {answer}!")
