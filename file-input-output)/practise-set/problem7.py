with open("log.txt", "r") as f:
    lines = f.readlines()   # ✅ read all lines into a list

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Word is present at Line no: {lineno}")
        break
    lineno += 1
else:
    print("The word is not present")

##################################################################################
with open("log.txt", "r") as f:
    lines = f.readlines()   # ✅ read all lines into a list

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Word is present at Line no: {lineno}")
        break
    lineno += 1
else:
    print("The word is not present")
