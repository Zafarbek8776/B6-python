def execute_twice(func):
    func()
    func()

def say_hello():
    print("Hello!")

execute_twice(say_hello)
