import math 
from math import sqrt, pow, sin, cos
number = float(input("Enter a number: "))
square_root = sqrt(number)
square = pow(number, 2)
cube = pow(number, 3)
sine_value = sin(number)
print()
print(f"The square root of {number} is {square_root:.2f}")
print(f"The square of {number} is {square:.2f}")
print(f"The cube of {number} is {cube:.2f}")    
print(f"The sine of {number} is {sine_value:.2f}")

# :.2f : 2 SIGNIFICANT FIGURES
# f {} : TO ADD VALUES IN BETWEEN STRINGS || [ print(f"Area :{type(sine_value)} and car : {cube}"+ str(sine_value)) ] IS POSSIBLE