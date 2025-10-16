def show_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@show_function_name
def greet():
    print("Hello, world!")

def add(a, b):
    return a + b

greet()
result = add(5, 3)
print("Result:", result)
