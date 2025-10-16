def sort_arguments(func):
    def wrapper(*args, **kwargs):
        sorted_args = []
        for arg in args:
            if isinstance(arg, (list, tuple)):
                sorted_args.append(sorted(arg))
            else:
                sorted_args.append(arg)
        return func(*sorted_args, **kwargs)
    return wrapper

@sort_arguments
def show_numbers(numbers):
    print("Sorted numbers:", numbers)

@sort_arguments
def combine(a, b):
    print("A:", a)
    print("B:", b)

# Test
show_numbers([5, 2, 8, 1])
combine((3, 1, 2), [9, 7, 8])
