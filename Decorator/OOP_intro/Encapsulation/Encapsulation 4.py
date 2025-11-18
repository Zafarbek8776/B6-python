class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def show_age(self):
        print(f"{self.name}'s age is {self.age}")

p = Person("Rustam", 20)

p.show_age()
print(p.age)