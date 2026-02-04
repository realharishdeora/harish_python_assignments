class Vehicle:
    def move(self):
        print("This Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road.")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road.")

Vehicles = [Car(),Bicycle()]
for Vehicle in Vehicles:
    Vehicle.move()