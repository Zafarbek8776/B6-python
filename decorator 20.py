def reverse_strings(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            if isinstance(arg, str):
                new_args.append(arg[::-1])  
            else:
                new_args.append(arg)
        return func(*new_args, **kwargs)
    return wrapper


def greet(name):
    print(f"Hello, {name}!")


def show_words(word1, word2):
    print("Word 1:", word1)
    print("Word 2:", word2)


greet("Zafar")
show_words("Python", "Decorator")
