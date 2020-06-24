# 1.Write a python program to find area of a circle using math function

import math
r=float(input("Enter the radius of circle:"))
area=math.pi*r*r
print("area of circle is:",area)


# 2.Write a program to find area of regular polygon using math function

from math import tan,pi
n=int(input("Enter number of sides:"))
s=float(input("Enter the length of the side:"))
area=n*(s**2)/(4*tan(pi/n))
print("Area of regular polygon is:",area)


# 3.Write a program to find area of segment of a circle formula using math function 

import math
pi=3.14159
def area_of_segment(radius,angle):
    area_of_sector=pi*(radius*radius)*(angle/360)
    area_of_triangle=1/2*(radius*radius)*math.sin((angle*pi)/180)
    return area_of_sector-area_of_triangle;
radius=float(input("Enter radius of circle:"))
angle=float(input("Enter angle of circle:"))
print("Area of minor segment=",area_of_segment(radius,angle))
print("Area of major segment=",area_of_segment(radius,(360-angle)))


# 4.Write a python program to shuffle list l1=[100,1,2,3,30,40,"hai","hello"]

import random
l1=[100,1,2,3,30,40,"hai","hello"]
print("Before shuffling:",l1)
random.shuffle(l1)
print("After shuffling",l1)

# 5.Write a program to generate random numbers between 1,10000 and difference between each random number is 50

import random
rnum=random.sample(range(1,10000),50)
print("Random integer:",rnum)


# 6.Write a python program by using math module to find

import math
print(math.sin(math.pi/3))
print(math.cos(math.pi))
print(math.tan(math.pi/2))
print(math.sin(0.8660254037844386))
print(math.pow(5,8))
print(math.sqrt(400))
print(math.exp(5))
print(math.log2(1024))
print(math.log10(1024))
print(math.floor(23.56),math.ceil(23.56000))