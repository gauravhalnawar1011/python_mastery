f = open("poem.txt")
content = f.read()
if ("twinkle" in content):
    print("Present")
else:
    print("The content is not present in our file")
f.close()