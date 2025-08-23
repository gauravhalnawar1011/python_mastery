# write an program to calculate factorial of the given number  useing for loop 


# 5! = 1x2x3x4x5 

n = int(input("Enter An Number: "))
product = 1


for i in range(1,n+1):
    product = product * i
print(f"The factorial of {n}  is the : {product}")

