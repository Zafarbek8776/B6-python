
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Muu!")

dog1 = Dog()
cat1 = Cat()

dog1.speak()
cat1.speak()
