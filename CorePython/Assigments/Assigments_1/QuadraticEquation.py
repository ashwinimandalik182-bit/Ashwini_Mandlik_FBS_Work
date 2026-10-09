# 7. Program to Find the Roots of a Quadratic Equation

import math
a = int (input ("Enter a: "))
b = int (input ("Enter b: "))
c = int (input ("Enter c: "))

d = b**2 - 4 * a * c

root1 = (-b + math.sqrt(d))/(2*a)

root2 = (-b - math.sqrt(d))/(2*a)

print(f"Root 1 = {root1} \nRoot 2 = {root2}")