import math  
pi = 3.14159 
def area_of_segment(radius, angle):  
    area_of_sector = pi*(radius*radius)*(angle / 360) 
    area_of_triangle = 1/2*(radius*radius)*math.sin((angle*pi)/180)   
    return area_of_sector - area_of_triangle; 
radius = float(input("enter radius"))
angle = float(input("enter angle"))
print("Area of minor segment =", 
       area_of_segment(radius, angle)) 
print("Area of major segment =", 
      area_of_segment(radius, (360 - angle))) 