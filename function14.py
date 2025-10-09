def outer():
    def inner1():
        print("This is inner function 1")
    
    def inner2():
        print("This is inner function 2")
    
    inner1()
    inner2()

outer()
