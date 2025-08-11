# Import entire modules
import math
# Import specific functions from modules
from math import sqrt, pow, sin, cos


radius = float(input("Enter your radius: "))

# Using imported modules
circle_area = math.pi * (radius ** 2)
circle_circumference = math.pi * (radius * 2)

print()
print("Area : " + str(circle_area))
print("Circumference : " + str(circle_circumference))