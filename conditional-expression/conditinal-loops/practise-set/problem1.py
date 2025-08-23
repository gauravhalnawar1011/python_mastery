# write an program to find the greatest four number enterd by user 
# Program to find the greatest among four numbers
a = int(input("Enter the First number: "))
b = int(input("Enter the Second number: "))
c = int(input("Enter the Third number: "))
d = int(input("Enter the Fourth number: "))

if a >= b and a >= c and a >= d:
    print("A is the greatest")
elif b >= a and b >= c and b >= d:
    print("B is the greatest")
elif c >= a and c >= b and c >= d:
    print("C is the greatest")
else:
    print("D is the greatest")


