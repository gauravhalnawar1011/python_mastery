# 🔹 What is a While Loop?

# A while loop repeats a block of code as long as a condition is true.
# Unlike the for loop (which is used when you know how many times to loop), the while loop is mainly used when you don’t know beforehand how many times you’ll need to run the loop.


# while condition:
    # code block
# condition → a Boolean expression (True/False)

# If condition is True → loop continues

# If condition is False → loop stops

# ⚠️ Be careful! If the condition never becomes False, you’ll create an infinite loop.


# Example 1: Basic Counter

i = 1
while i <= 5:
    print(i)
    i += 1


# Example 2: Infinite Loop (⚠️ Dangerous!)

# while True:
#     print("This will run forever")


# Example 3: Using break

i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1



# Example 4: Using continue

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


# 🔹 Example 5: Guessing Game

secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))

print("🎉 Correct! The number was", secret)


# Example 6: While-Else

# Just like for, a while loop can also have an else block.
# The else runs only if the loop condition becomes false (not if the loop ends by break).


i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished normally")


# 🔹 Real-World Uses of while Loop

# ✅ Waiting for user input until correct
# ✅ Running a program until the user exits
# ✅ Reading files line by line
# ✅ Games (loops until game over)
# ✅ Network/server programs that run continuously





# Nested while loops (while inside while)

i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1


# Using while True with break as a menu system (common in real-world apps)

while True:
    print("\n1. Say Hello\n2. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        print("Hello 👋")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

# While loop with multiple conditions

x = 0
y = 5
while x < 5 and y > 0:
    print(f"x={x}, y={y}")
    x += 1
    y -= 1


# Simulating do-while loop (Python doesn’t have it directly)
# Many languages (like C, Java) have do-while (runs at least once). In Python, you can mimic it:


while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        break
    print("Try again!")




# Using while with input validation
# Example: forcing a user to enter valid data until correct.


age = -1
while age < 0:
    age = int(input("Enter a valid age (>=0): "))
print("Your age is:", age)



# File reading with while loop
# Instead of reading all at once, you can read line by line:
f = open("data.txt", "r")
line = f.readline()
while line:
    print(line.strip())
    line = f.readline()
f.close()


# Using counters / accumulators inside while
# Example: summing numbers until user quits.


total = 0
while True:
    num = input("Enter number (or 'q' to quit): ")
    if num == 'q':
        break
    total += int(num)
print("Total:", total)


# Performance / safety

# Always make sure your while loop changes something inside (otherwise → infinite loop).

# Example of bad loop:

i = 1
while i < 5:
    print(i)   # i never changes


