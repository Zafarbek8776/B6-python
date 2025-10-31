class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass


print(issubclass(Mammal, Animal))  
print(issubclass(Dog, Mammal))     
print(issubclass(Dog, Animal))     
print(issubclass(Animal, Dog))     
