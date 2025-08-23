# write an program to find give number is prime or not 


num = int(input("Enter a Number: "))

for i in range(2, num):
    if num % i == 0:   # check divisibility
        print("Number is Not Prime")
        break
else:
    print("Number is Prime")
