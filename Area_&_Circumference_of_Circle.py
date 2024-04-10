'''Calculate the area and circumference of a circle given its
radius'''

def area(r):
    return 3.14*r**2

def circumference(r):
    return 2*3.14*r
    
radius=float(input("Enter the radius: "))

print('Area:',area(radius))
print('circumference:',circumference(radius)) 

'''
import math

def area(r):
    return math.pi * r**2

def circumference(r):
    return 2 * math.pi * r

radius = float(input("Enter the radius: "))

print("Area:", area(radius))
print("Circumference:", circumference(radius))
'''