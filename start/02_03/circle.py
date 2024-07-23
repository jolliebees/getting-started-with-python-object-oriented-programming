"""
A class for representing a circle
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display_circumference(self):
        print(f"The circle circumference: {2 * 3.14 * self.radius} units")

    def display_area(self):
        print(f"The area of the circle: {3.14 * self.radius ** 2} square units")

# Create an instance of circle
circle1 = Circle(7)

# Display its circiference and area
circle1.display_circumference()
circle1.display_area()