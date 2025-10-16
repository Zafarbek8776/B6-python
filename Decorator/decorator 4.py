def to_uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper


def greet():
    return "hello, world!"


def name():
    return "zafar"


print(greet())
print(name())
