class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass


dog1 = Dog()


print(isinstance(dog1, Dog))     
print(isinstance(dog1, Mammal))  
print(isinstance(dog1, Animal))  
