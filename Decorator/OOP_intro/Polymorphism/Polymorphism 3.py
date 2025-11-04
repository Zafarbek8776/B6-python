class Shape:
    def area(self):
        print("This method should be overridden by subclasses.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


circle1 = Circle(7)
square1 = Square(6)


print("Circle area:", circle1.area())
print("Square area:", square1.area())
