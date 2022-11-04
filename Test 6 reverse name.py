#Write a Python function to reverses a string if it's length is a multiple of 4.
name=input("enter a name:")

if(len(name)%4==0):
    print(name[::-1])
else:
    print("cant")                               