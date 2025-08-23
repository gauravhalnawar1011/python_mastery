# this section will explore about the tuples methods 
names = ("krushna", "Arjuna", "karna", "dhritrstra", "kaurav", 100, "pandav", 23.89, True, "False")

# 1. count(x) → returns number of times x appears in tuple
print(names.count(100))   # 1
print(names.count("karna"))  # 1

# 2. index(x) → returns the index of first occurrence of x
print(names.index("karna"))  # 2
print(names.index("krushna"))  # 0


# Length of tuple
print(len(names))   # 10

# Membership test in
print("Arjuna" in names)   # True
print("Bheem" in names)    # False

# Concatenation
new_tuple = names + ("bheem", "nakul")
print(new_tuple)

# Repetition
repeated = ("test",) * 3
print(repeated)  # ('test', 'test', 'test')

# Slicing
print(names[0:3])  # ('krushna', 'Arjuna', 'karna')'


# unpackging
names = ("krushna", "Arjuna", "karna", "dhritrstra", "kaurav", "pandav", "bheem", "nakul")

# unpackging
a, b, c, d, e, f, g, h = names  

print(a, b, c, d, e, f, g, h)




