# Write an function print the n lined of the following pattern 

'''
***
**
*
'''


def pattern(n):
    if (n==0):
        return
    print("*" * n)
    pattern(n-1)
n = int(input("Enter the Number: "))
pattern((n))