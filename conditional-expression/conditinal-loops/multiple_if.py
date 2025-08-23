 # if elif else ladder
# age = int(input("Enter You age: "))

# if (age % 2 == 0):
#     print("age is even ") # we can run multiple 'if' in the program  

# else:
#     print("your age is odd ") # but we caan not run the 'else' alone and 'elif' also can be alone 

# if age >=18:
#     print("Your age is above the consent")
#     print("Your eligible for the vote")
# elif (age <0):
#     print("you are enterig and invalid age")
# elif (age ==0):
#     print("you are enterig 0 which is invalid ")
# else:
#     print("Your age is below age of consent ")

# print("so your age is", age)


# Take a number from the user and check if it is positive, negative, or zero.


# num = int(input("Enter the Number :"))


# if num > 0:
#     print("Enterd number is :",num)
# elif (num<=0):
#     print("number is invlid you enter and negative number:", num)
# elif (num ==0):
#     print("the number you enterd is 0")
# else:
#     print("numer is :",num)


# Take a number and check if it is even or odd.

# num = int(input("Enter the Number :"))

# if (num %2 ==0):
#     print("number is even",num)
# else:
#     print("Number is odd",num)


# Take an age and check if the person is eligible to vote (>=18).


# age = int(input("Enter You age: "))



# if (age >= 18):
#     print("Your age is 18+ \n")
#     print("Congrtualtion your eligible for vote")

# else:
#     print("Your under age of consent: ")


# Take a number and check if it is a multiple of 5.

# num = int(input("Enter the Number :"))

# if (num % 5==0):
#     print("the number is divisible by 5")
# else:
#     print("number is not divisible by 5")

# Take two numbers and print the greater one.
 

# num1 = int(input("Enter the Number 1 :"))
# num2 = int(input("Enter the Number  2:"))


# if num1 > num2:
#     print("Number 1 is greter than the Number 2")

# else:
#     print("Number 2 is greste than number 1")


# Take marks (0–100) and print the grade:

# >=90 → A, >=75 → B, >=50 → C, else Fail.



marks = int(input("Enter your marks (0–100): "))

if 0 <= marks <= 100:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")
else:
    print("Invalid marks. Please enter a number between 0 and 100.")



#  Take a year and check if it is a leap year (divisible by 4 but not 100, or divisible by 400).


# 2000 → divisible by 400 → Leap ✅

# 1900 → divisible by 100 but not 400 → Not Leap ❌

# 2024 → divisible by 4 but not 100 → Leap ✅

# 2023 → not divisible by 4 → Not Leap ❌
# 2000 → divisible by 400 → Leap ✅

# 1900 → divisible by 100 but not 400 → Not Leap ❌

# 2024 → divisible by 4 but not 100 → Leap ✅

# 2023 → not divisible by 4 → Not Leap ❌


#using nested if 

# year = int(input("Enter the Year: "))

# if year % 4 == 0:                     # divisible by 4
#     if year % 100 == 0:               # divisible by 100
#         if year % 400 == 0:           # divisible by 400
#             print("Leap year ")
#         else:
#             print("Not a leap year ")
#     else:
#         print("Leap year ")
# else:
#     print("Not a leap year ")


# # useing elif 


# year = int(input("Enter the Year: "))

# if year % 400 == 0:
#     print("Leap Year ")
# elif year % 100 == 0:
#     print("Not a Leap Year ")
# elif year % 4 == 0:
#     print("Leap Year ")
# else:
#     print("Not a Leap Year ")


# Take 3 numbers and print the largest number.


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print("A is the greatest")
elif b > c:
    print("B is the greatest")
else:
    print("C is the greatest")


# useing the nested if

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >= b:
    if a >= c:
        print("A is the greatest")
    else:
        print("C is the greatest")
else:
    if b >= c:
        print("B is the greatest")
    else:
        print("C is the greatest")



# Take a character and check if it is a vowel or consonant.

char = input("Enter a single alphabet character: ")

# Check if the input is a single alphabet character
if len(char) == 1 and char.isalpha():
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("It is a vowel.")
    else:
        print("It is a consonant.")
else:
    print("Invalid input. Please enter a single alphabet letter.")



# A shop gives a discount:

# >=5000 → 20% off,

# >=2000 → 10% off,

# else → No discount.


amount = float(input("Enter the total purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
    final_amount = amount - discount
    print(f"20% discount applied: ₹{discount:.2f}")
    print(f"Amount to pay: ₹{final_amount:.2f}")
elif amount >= 2000:
    discount = amount * 0.10
    final_amount = amount - discount
    print(f"10% discount applied: ₹{discount:.2f}")
    print(f"Amount to pay: ₹{final_amount:.2f}")
else:
    print("No discount applied.")
    print(f"Amount to pay: ₹{amount:.2f}")




# Take a number and check if it is prime or not (using if/else, no loops yet → check divisibility by 2,3,5,7 for now).
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
elif num in (2, 3, 5, 7):
    print("Prime number")
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print("Not a prime number")
else:
    print("Prime number (based on limited checks)")


#  1. Temperature Check (°C)
temp = float(input("Enter the temperature in °C: "))

if temp < 0:
    print("Freezing")
elif temp <= 20:
    print("Cold")
elif temp <= 35:
    print("Warm")
else:
    print("Hot")


# Login System (Username & Password Check)
correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username != correct_username:
    print("Invalid user")
elif password != correct_password:
    print("Wrong password")
else:
    print("Login successful")


# Ternary Operator: Positive or Negative
num = int(input("Enter a number: "))

print("Positive" if num >= 0 else "Negative")


#  Character Type Check: Digit, Uppercase, Lowercase, or Special Symbol

char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter only one character.")
elif char.isdigit():
    print("It is a Digit")
elif char.isupper():
    print("It is an Uppercase letter")
elif char.islower():
    print("It is a Lowercase letter")
elif not char.isalnum():
    print("It is a Special symbol")
else:
    print("Unrecognized character type")

