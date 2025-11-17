class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14 * self.radius


# Test
c = Circle(5)
print("Diện tích:", c.area())
print("Chu vi:", c.circumference())
