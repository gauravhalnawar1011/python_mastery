# Write an python Program to print multiplication table fo the given number 


def multiplication(n):
    for i in range (1,11):
        print(f"{n} X {i} = {n * i}")

n = int(input("Enter Your number : "))
multiplication(n)




