class Dog:
    def action(self):
        print("Dog is barking!")

class Car:
    def action(self):
        print("Car is driving!")

class Robot:
    def action(self):
        print("Robot is working!")


dog1 = Dog()
car1 = Car()
robot1 = Robot()


objects = [dog1, car1, robot1]


for obj in objects:
    obj.action()
