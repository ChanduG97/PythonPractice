### 1. Write a function that takes the lengths of the two shorter sides of a right triangle as its parameters. Return the hypotenuse of the triangle, computed using Pythagorean theorem, as the function’s result.
import math 
def hypot(a,b):
    c= math.sqrt(a**2+b**2)
    return c
a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
print('The hypotenuse of a triangle is:',hypot(a,b))