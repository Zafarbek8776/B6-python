def multiply_by_10(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (int, float)):  
            return result * 10
        return result
    return wrapper


def add(a, b):
    return a + b


def get_number():
    return 7


print(add(3, 2))      
print(get_number())  
