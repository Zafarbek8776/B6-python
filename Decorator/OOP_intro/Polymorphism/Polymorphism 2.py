class Dog:
    def sound(self):
        print("Woov!")

class Cat:
    def sound(self):
        print("Meew!")

class Cow:
    def sound(self):
        print("Moo!")

def animal_sound(animal):
    animal.sound()


dog1 = Dog()
cat1 = Cat()
cow1 = Cow()

animal_sound(dog1)
animal_sound(cat1)
animal_sound(cow1)

