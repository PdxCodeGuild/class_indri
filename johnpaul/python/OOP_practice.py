class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


model = Vehicle(240, 18)
print(model.max_speed)

Modelv = Vehicle(200, 60)
print(Modelv.mileage)