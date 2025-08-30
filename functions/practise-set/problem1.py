# write an program to find the greatest of 3 number using function

def greatest_number(a,b,c):
    if (a>b and a>c ):
        return a
    elif(b>a and b>c ):
        return b 
    elif (c>b and c>a):
        return c 
    
a = 1
b = 3

c = 5

print(greatest_number(a,b,c))




def greatest_number(a, b, c):
    if a >= b and a >= c:     # a is greatest
        return a
    elif b >= a and b >= c:   # b is greatest
        return b
    else:                     # otherwise c is greatest
        return c


# test values
a = 1
b = 3
c = 5

print("Greatest number is:", greatest_number(a, b, c))
