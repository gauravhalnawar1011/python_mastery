# Write an Program to rename the file to "renamed_python.txt"

with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt","w") as f :
    f.write(content)