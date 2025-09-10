# Open the file in read mode (default is 'r')
f = open("file.txt", "r")

# Read the entire content of the file
data = f.read()

# Print the content
print(data)

# Always close the file after work is done 
# (important for releasing system resources & letting other programs access it)
f.close()

# Best practice: Using 'with' automatically closes the file
with open("file.txt", "r") as f:
    data = f.read()
    print(data)
