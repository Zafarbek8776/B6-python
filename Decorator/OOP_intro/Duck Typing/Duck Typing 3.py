class Car:
    def run(self):
        print("Car is running.")

class Rock:
    def sit(self):
        print("Rock just sits still.")

        
def start(obj):
    if hasattr(obj, "run"):       
        obj.run()
    else:
        print("Error: This object cannot run!")


car1 = Car()
rock1 = Rock()


start(car1)   
start(rock1)  
