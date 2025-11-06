class Duck:
    def quack(self):
        print("Quack, quack!")
    def walk(self):
        print("Duck is walking.")

class Person:
    def quack(self):
        print("The person feeds the ducks.")
    def walk(self):
        print("Person is walking in the street.")

def make_it_quack(sub):
    sub.quack()
    sub.walk()


duck1 = Duck()
person1 = Person()


make_it_quack(duck1)
make_it_quack(person1)
