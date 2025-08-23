# if we have to print the 5 number we can do like 

print(1,2,3,4,5)

# but there is an another better way 

for i in range(1,5):
    print(i)


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)




# Example 3: Custom Range

for i in range(2, 10, 2):  
    print(i)


# range(start, stop, step)

# 2 = start

# 10 = stop (exclusive)

# 2 = step


# Example 4: Iterating Over a String

for char in "hello":
    print(char)
#output
# h
# e
# l
# l
# o


# 🔹 Loop Control Statements

# break → exit loop immediately

for i in range(10):
    if i == 5:
        break
    print(i)

# 👉 Output: 0 1 2 3 4


# continue → skip the current iteration and go to next
for i in range(5):
    if i == 2:
        continue
    print(i)
# 👉 Output: 0 1 3 4


# else with for loop
# The else block runs only if the loop finishes normally (not broken by break).

for i in range(3):
    print(i)
else:
    print("Loop finished successfully")

# 👉 Output:
# 0
# 1
# 2
# Loop finished successfully

# 🔹 Nested For Loops

# A loop inside another loop:

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 👉 Output:

# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1



# 🔹 Common Uses of For Loop

# ✅ Iterating over lists, tuples, strings, dictionaries
# ✅ Generating sequences of numbers
# ✅ Running code a fixed number of times
# ✅ Creating patterns (like star patterns)
# ✅ Searching/filtering items



# 🔹 1. Multiplication Table

num = 5  # Multiplication Table of 5

print(f"Multiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# 2. Sum of Numbers
n = 10
total = 0

for i in range(1, n+1):
    total += i

print("Sum of numbers from 1 to", n, "is:", total)  # Sum of numbers from 1 to 10 is: 55

# 3. Factorial of a Number

num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is:", fact)  # Factorial of 5 is: 120

# 4. Print a Pattern (Pyramid of Stars ⭐)

rows = 5
for i in range(1, rows+1):
    print(" " * (rows - i) + "*" * (2*i - 1))



# 🔹 5. Loop Through a Dictionary

student = {"name": "Alice", "age": 20, "marks": 85}

for key, value in student.items():
    print(key, ":", value)  #name : Alice age : 20 marks : 85


# 6. Find Even Numbers in a List

numbers = [10, 15, 22, 33, 40, 55]

for n in numbers:
    if n % 2 == 0:
        print(n, "is even")   # 10 is even 22 is even 40 is even


# 🔹 7. Simple Guessing Game

secret = 7
for attempt in range(3):
    guess = int(input("Enter your guess: "))
    if guess == secret:
        print("🎉 Correct! You win!")
        break
else:
    print("❌ Sorry, you lost! The number was", secret)






# Iterating with enumerate()
# Lets you loop with both index + value.

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)



# Iterating with zip() (multiple sequences at once)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(name, "scored", score)



# Iterating a dictionary properly

student = {"name": "Alice", "age": 20, "marks": 85}

for key, value in student.items():
    print(key, ":", value)



# List / Dictionary Comprehensions (short for loops)

numbers = [1, 2, 3, 4, 5]
squares = [n*n for n in numbers]
print(squares)


# 👉 Output:

# [1, 4, 9, 16, 25]


# Using range backwards

for i in range(10, 0, -1):
    print(i)


# Else in for loop with break difference

for i in range(5):
    if i == 3:
        break
else:
    print("No break used")  # won’t run here


# For loop with pass (placeholder)

for i in range(5):
    pass  # useful when you haven’t written logic yet


# Iterating over sets (unordered)

myset = {10, 20, 30}
for val in myset:
    print(val)


# Iterating with reversed()

for i in reversed(range(1, 6)):
    print(i)


# Nested comprehensions (2D data / matrix)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [num for row in matrix for num in row]
print(flat)






