# write an program to mine log file and and find whethere python is present from que 6 

with open("log.txt", "r") as f:
    content = f.read()
if("python" in content):
    print("Word is present ")
else:
    print("the word is not present")