# Program: Detect spaces in a string

name = "Hello Devops is really  Good  Filead"

# Find double space
double_space_index = name.find("  ")

if double_space_index != -1:
    print(f"Double space found at index {double_space_index}")
else:
    print("No double space found")
