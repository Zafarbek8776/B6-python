class Dog:
    def sound(self):
        print("Woof!")

class Cat:
    def sound(self):
        print("Meow!")

class Cow:
    def sound(self):
        print("Moo!")


dog1 = Dog()
cat1 = Cat()
cow1 = Cow()


animals = [dog1, cat1, cow1]


for animal in animals:
    animal.sound()
