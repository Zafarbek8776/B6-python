class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age 
p1 = Person("Ali", 24)


print("Name:", p1.name)
print("Age:", p1.age)


p1.name = "Zafar"
p1.age = 25


print("Updated Name:", p1.name)
print("Updated Age:", p1.age)

