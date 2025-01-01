import math

# Define the Circle class with radius as a parameter
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Define the get_area method
    def get_area(self):
        return round(math.pi * self.radius ** 2, 2)


    # Define the get_circumference method
    def get_circumference(self):
        return round(math.pi * self.radius * 2, 2)

# Get the radius from the user
radius = float(input())

# Create an instance of the Circle class with the given radius
circle = Circle(radius)

# Call the get_area method and print the result rounded to 2 decimal places
print(circle.get_area())

# Call the get_circumference method and print the result rounded to 2 decimal places
print(circle.get_circumference())
