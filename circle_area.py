import math

def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

# Prompt the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
circle_area = calculate_circle_area(radius)

# Display the result
print(f"The area of the circle with radius {radius} is: {circle_area}")
