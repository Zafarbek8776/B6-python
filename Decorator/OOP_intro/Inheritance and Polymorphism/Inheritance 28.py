class A:
    def show(self):
        print("This is from class A")

class B(A):
    def show(self):
        print("This is from class B")

class C(A):
    def show(self):
        print("This is from class C")

class D(B, C):  
    pass

d1 = D()

d1.show()              
print(D.__mro__)       
