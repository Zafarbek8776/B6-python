def math_ops(x, y):
    def add():
        print("Addition:", x + y)

    def sub():
        print("Subtraction:", x - y)

    def mul():
        print("Multiplication:", x * y)

    add()
    sub()
    mul()

math_ops(10, 8)
