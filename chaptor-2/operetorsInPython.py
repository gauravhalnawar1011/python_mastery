# Arithmetic Operators
a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a % b)   # Modulus (remainder): 1
print(a ** b)  # Exponentiation: 1000
print(a // b)  # Floor Division: 3

# Comparison Operators
print(a == b)  # Equal to: False
print(a != b)  # Not equal to: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater than or equal to: True
print(a <= b)  # Less than or equal to: False

# Assignment Operators
x = 5
x += 2  # x = x + 2 → 7
x -= 1  # x = x - 1 → 6
x *= 3  # x = x * 3 → 18
x /= 2  # x = x / 2 → 9.0
x %= 4  # x = x % 4 → 1.0

# Logical Operators
a = True
b = False

print(a and b)  # Logical AND: False
print(a or b)   # Logical OR: True
print(not a)    # Logical NOT: False

# Bitwise Operators
x = 5  # 0101 in binary
y = 3  # 0011 in binary

print(x & y)  # AND: 1 (0001)
print(x | y)  # OR: 7 (0111)
print(x ^ y)  # XOR: 6 (0110)
print(~x)     # NOT: -6 (inverts all bits)
print(x << 1) # Left shift: 10 (1010)
print(x >> 1) # Right shift: 2 (0010)

# Membership Operators
my_list = [1, 2, 3]

print(2 in my_list)     # True
print(4 not in my_list) # True

# Identity Operators
a = [1, 2]
b = [1, 2]
c = a

print(a is c)     # True (same object)
print(a is b)     # False (same content, different objects)
print(a == b)     # True (same content)
