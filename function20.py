def outer():
    def add_one(x):
        return x + 1

    def add_two(x):
        return x + 2

    
    return add_one, add_two

f1, f2 = outer()


print(f1(12))  
print(f2(10)) 
