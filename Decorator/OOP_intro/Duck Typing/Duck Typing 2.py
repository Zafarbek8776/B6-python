class Car:
    def run(self):
        print("Car is running on the road.")

class Athlete:
    def run(self):
        print("Athlete is running on the track.")

class Computer:
    def run(self):
        print("Computer program is running.")


def start(obj):
    obj.run()  


car1 = Car()
athlete1 = Athlete()
computer1 = Computer()


start(car1)
start(athlete1)
start(computer1)
