name = "Hello Devops is really  Good  Filead"

# Find the first occurrence of double space
print(name.find("  "))   # gives the index (position) of first "  "

# Replace all double spaces with single space
print(name.replace("  "," "))

# Strings are immutable in Python
# ✅ Immutable means: you cannot change them directly,
#    you can only create a new string from an old one.

name = "hello"

# ❌ This will cause an error because strings can't be modified in place
# name[0] = "H"

# ✅ Instead, you recreate a new string using slicing + concatenation
new_name = "H" + name[1:]
print(new_name)   # Output: Hello

# ✅ Or using string methods (creates a new string in memory)
upper_name = name.upper()
print(upper_name) # Output: HELLO

# Proof: memory addresses (id) change
print("Original id:", id(name))
print("New id:", id(new_name))
print("Upper id:", id(upper_name))
