# ===============================
# 1. Opening a file
# ===============================
# Modes: 
# "r"  -> read (default, error if file doesn’t exist)
# "w"  -> write (creates new file / overwrites existing)
# "a"  -> append (adds to the end of file)
# "x"  -> create new file (error if file exists)
# "b"  -> binary mode
# "t"  -> text mode (default)

f = open("file.txt", "r")
f.close()


#===============================================
# 2. Reading from a file
#===============================================
# Read entire content
with open("file.txt", "r") as f:
    data = f.read()
    print("Read All:#n", data)

# Read only first 10 characters
with open("file.txt", "r") as f:
    data = f.read(10)
    print("First 10 chars:", data)

# Read one line at a time
with open("file.txt", "r") as f:
    line1 = f.readline()
    print("Line1:", line1)

# Read all lines as list
with open("file.txt", "r") as f:
    lines = f.readlines()
    print("Lines List:", lines)


#===============================================
# 3. Looping through file
#===============================================

# Using while loop
with open("file.txt", "r") as f:
    line = f.readline()
    while line != "":
        print(line, end="")   # end="" avoids double newlines
        line = f.readline()

# Using for loop (better way)
with open("file.txt", "r") as f:
    for line in f:
        print(line, end="")

#===============================================
# 4. Writing to a file
#===============================================

# Overwrites file (creates new if doesn’t exist)
with open("file.txt", "w") as f:
    f.write("Hello World!#n")
    f.write("This will overwrite old content.#n")


#===============================================
# 5. Appending to a file
#===============================================

# Adds new content at the end
with open("file.txt", "a") as f:
    f.write("This line is appended.#n")

#===============================================
# 6. Binary mode (images, audio, etc.)
#===============================================
# Read binary
with open("image.png", "rb") as f:
    content = f.read()
    print("Binary length:", len(content))

# Write binary
with open("copy.png", "wb") as f:
    f.write(content)


#===============================================
# 7. File pointer operations
#===============================================

with open("file.txt", "r") as f:
    print(f.read(5))        # Read first 5 chars
    f.seek(0)               # Move pointer back to start
    print(f.read(10))       # Read first 10 chars again
    print("Current position:", f.tell())  # Get pointer location


#===============================================
# 8. Check if file exists before opening
#===============================================


import os

if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File does not exist")



#==========================================================

# 1. **`f.truncate([size])`**

# → Shrinks or expands file to given size (in bytes).

#==========================================================

  
with open("file.txt", "w") as f:
    f.write("Hello World!")
    f.truncate(5)   # File now only contains "Hello"
   

   

##==========================================================

# 2. **`f.flush()`**

# → Forces writing buffered content to disk (useful before program crash).

##==========================================================

  
with open("file.txt", "w") as f:
    f.write("Temporary data")
    f.flush()  # Immediately save to disk
   

   

##==========================================================

# 3. **`f.closed` (property)**

# → Returns `True` if file is closed.

##==========================================================

  
f = open("file.txt")
print(f.closed)  # False
f.close()
print(f.closed)  # True
   

   

##==========================================================

# 4. **`f.mode` (property)**

# → Shows mode in which file was opened (`"r"`, `"w"`, `"a"`, etc.).

##==========================================================

  
f = open("file.txt", "a")
print(f.mode)  # "a"
f.close()
   

   

##==========================================================

# 5. **`f.name` (property)**

# → Shows the filename.

##==========================================================

  
f = open("file.txt")
print(f.name)  # "file.txt"
f.close()
   

   

##==========================================================

# 6. **`f.encoding` (property)**

# → Shows encoding of the file (usually `"UTF-8"`).

##==========================================================

  
with open("file.txt", "r", encoding="utf-8") as f:
    print(f.encoding)  # UTF-8
