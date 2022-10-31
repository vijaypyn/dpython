#Write a Python program to multiply two integers without using the * operator in python
n1=int(input("enter a number for n1: ")) 
n2=int(input("enter a number for n2: ")) 
product=0
for i in range(1, n2+1):
    product=product+n1
print("multiplication of number: ", product )