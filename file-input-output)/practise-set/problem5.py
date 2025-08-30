words = ["Donkey", "as","gadha","bad"]

with open("file-name.txt", "r") as f:
    content = f.read()


for word in words:
    content = content.replace(word, "#" * len(word))


with open("file-name.txt", "w") as f:
    f.write(content)