class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving on the road")

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing on the water")

car1 = Car()
boat1 = Boat()

car1.move()
boat1.move()
