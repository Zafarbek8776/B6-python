class A:
    pass

class B(A):
    pass


print(issubclass(A, object))  
print(issubclass(B, object))  

print(A.__mro__)
print(B.__mro__)
