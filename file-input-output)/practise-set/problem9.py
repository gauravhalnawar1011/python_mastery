# write an program to find out wheteher a file is identical & matches the content of thee another file 
with open("this.txt") as f:
    content1 = f.read()

with open("this_copy.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("Content matches")
else:
    print("content is differnet ")