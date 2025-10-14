def add(a, b):
    return a + b

def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(5, 3, add)
print(result)
