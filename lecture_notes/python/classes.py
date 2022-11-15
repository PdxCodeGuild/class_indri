
class Car:

    def __init__(self, color, engine_type=4, num_of_doors=4):
        self.color = color
        self.engine_type = engine_type
        self.num_of_doors = num_of_doors

    def vroom(self):
        if(self.engine_type != 0):
            print("VRROOOM")

    def __str__(self):
        return f"Color: {self.color} \t Engine Type: {self.engine_type}"

    def __gt__(self, other_car):
        return self.engine_type > other_car.engine_type

    def __lt__(self, other_car):
        return "You cant compare these cars..."


my_car = Car("blue")

steves_car = Car("red", 0, 2)

print(steves_car < my_car)