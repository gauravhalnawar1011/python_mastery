# Python Logical Operators
# Logical operators are used to combine conditional statements:

# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	




### **Truth Table**

# | A     | B     | A and B | A or B | not A |
# | ----- | ----- | ------- | ------ | ----- |
# | True  | True  | True    | True   | False |
# | True  | False | False   | True   | False |
# | False | True  | False   | True   | True  |
# | False | False | False   | False  | True  |



# "and" operator
print("True and True   is:", True and True)
print("True and False  is:", True and False)
print("False and True  is:", False and True)
print("False and False is:", False and False)
print("=============================================================")

# "or" operator
print("True or True    is:", True or True)
print("True or False   is:", True or False)
print("False or True   is:", False or True)
print("False or False  is:", False or False)
print("=============================================================")

# "not" operator
print("not True  is:", not True)
print("not False is:", not False)
print("================================================================")


### **Python Script**

# Logical Operators Truth Table Example

# Possible boolean values
values = [True, False]


print("A\tB\tA and B\tA or B\tnot A")
print("-" * 40)

# Loop through all combinations of True/False for A and B
for A in values:
    for B in values:
        and_result = A and B
        or_result = A or B
        not_result = not A
        print(f"{A}\t{B}\t{and_result}\t{or_result}\t{not_result}")

print("\n--- EXAMPLES ---")

x = 7
print(f"x = {x}")
print(f"(x > 5) and (x < 10) → {(x > 5) and (x < 10)}  # Both conditions true")
print(f"(x > 5) and (x > 10) → {(x > 5) and (x > 10)}  # One false, so result false")
print(f"(x < 5) or (x > 10)  → {(x < 5) or (x > 10)}   # At least one true → true")
print(f"not(x > 5 and x < 10) → {not (x > 5 and x < 10)} # Reverses the truth")


### **How It Works**

# 1. **Truth Table Part**

#    * Loops through all combinations of `True` and `False`.
#    * Shows what `and`, `or`, and `not` produce.
# 2. **Example Part**

#    * Uses a real number (`x = 7`) so you can see logical operators in real conditions.



