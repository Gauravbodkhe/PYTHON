# 34. Class Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle1 = Circle(7)
print("Circle Area:", circle1.area())