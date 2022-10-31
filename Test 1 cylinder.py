#Write a Python program to calculate surface volume and area of a cylinder.
#surface area = 2pirh + 2pirr
#volume = pirrh'''
pi=22/7
radius=float(input("Enter radious of cyclinder "))
height=float(input("Enter height of cyclinder "))
surfacearea= ((2*pi*radius)*height) + (2*(pi*radius*radius))
voulume= pi*radius*radius*height
print("surface of cyclinder: ", surfacearea)
print("volume of cyclinder: ", voulume)                 