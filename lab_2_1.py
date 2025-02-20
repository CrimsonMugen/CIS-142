##
# @author Johnathan Florio
# lab 2.1 perform simple geometry with user inputs
import math

recLength = int(input("Please enter the length of the rectangle: "))
recWidth = int(input("Please enter the Width of the rectangle: "))
recArea = recLength * recWidth
recPerimeter = (recLength * 2) + (recWidth * 2)
print()
print(f'Area: {recArea} sq units')
print(f'Perimeter: {recPerimeter} sq units\n')

cirRadius = float(input("Please enter the radius of the circle: "))
sphereRadius = float(input("Please enter the radius of the sphere: "))
cirArea = math.pi *(cirRadius ** 2)
sphereCircumference = 2 * math.pi * sphereRadius 
sphereVol = 4 / 3 * (math.pi * sphereRadius ** 3)
print()
print(f'Area: {cirArea:.2f} sq units')
print(f'Circumference: {sphereCircumference:.2f} units')
print(f'Volume: {sphereVol:.2f} cubic units')