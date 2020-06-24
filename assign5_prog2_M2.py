from math import tan,pi
GRAVITY = 9.8
length  = float(input("Enter the length of each side of Polygon (in meters): "))
number  = int(input("Enter the number of sides: "))
area = (number * length ** 2)/(4 * tan(pi/number))
print("The area of Polygon is ",area)