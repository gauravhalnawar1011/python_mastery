# New line
print("Hello\nWorld")  
# Output:
# Hello
# World


# Tab (like pressing Tab key)
print("Hello\tWorld")  
# Output: Hello    World


# Single quote inside single-quoted string
print('It\'s a sunny day')  
# Output: It's a sunny day


# Double quote inside double-quoted string
print("She said: \"Python is fun!\"")  
# Output: She said: "Python is fun!"


# Backslash itself
print("C:\\Users\\Admin")  
# Output: C:\Users\Admin


# Backspace (removes the previous character)
print("Helloo\b World")  
# Output: Hello World


# Carriage return (\r) → moves cursor to beginning of line
print("Hello\rWorld")  
# Output: World   (because "Hello" is overwritten)


# Form feed (\f) → moves cursor to new line (page break in printing context)
print("Hello\fWorld")  
# Output:
# Hello
#      World   (depends on terminal)


# Vertical tab (\v) → moves down but in same column
print("Hello\vWorld")  
# Output:
# Hello
#      World


# Unicode character (using \u or \U)
print("\u03A9")   # Greek Omega symbol Ω
print("\U0001F600") # 😀 (Unicode emoji)


# Octal value (\ooo) → character represented by octal number
print("\101")  # A (octal 101 = decimal 65 = 'A')


# Hex value (\xhh) → character represented by hex number
print("\x41")  # A (hex 41 = decimal 65 = 'A')
