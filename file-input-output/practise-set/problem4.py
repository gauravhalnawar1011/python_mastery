# a file conations the multiple donkey word replace them with the #### updating the same file 


word = "Donkey"

with open("file-name.txt", "r") as f:
    content = f.read()

contentnew = content.replace(word, "#####")


with open("file-name.txt", "w") as f:
    f.write(contentnew)