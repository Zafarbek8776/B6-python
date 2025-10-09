def outer():
    print("Outer start")
    
    def inner():
        print("Inner call")

outer()
