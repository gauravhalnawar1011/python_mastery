name = "hello"
name2 = "hello devops"
name3 = "   python   "
name4 = "aaaahelloaaaa"

# 1. strip() → removes whitespace from start and end
print(name3.strip())   # 'python'

# 2. lstrip() → removes whitespace from the left
print(name3.lstrip())  # 'python   '

# 3. rstrip() → removes whitespace from the right
print(name3.rstrip())  # '   python'

# 4. replace(old, new) → replace a substring
print(name2.replace("hello", "hi"))  # 'hi devops'

# 5. find(substring) → returns first index of substring, or -1 if not found
print(name2.find("dev"))   # 6
print(name2.find("xyz"))   # -1

# 6. index(substring) → like find(), but gives error if not found
print(name2.index("dev"))  # 6
# print(name2.index("xyz"))  # ValueError if not found

# 7. count(substring) → number of times substring appears
print(name2.count("o"))  # 2

# 8. isalpha() → True if only letters (no numbers, no spaces)
print("hello".isalpha())   # True
print("hello123".isalpha()) # False

# 9. isdigit() → True if only numbers
print("123".isdigit())    # True
print("12a".isdigit())    # False

# 10. isnumeric() → True if only numeric characters (includes Unicode numbers)
print("123".isnumeric())  # True

# 11. isalnum() → True if only letters & numbers (no spaces/symbols)
print("hello123".isalnum())  # True
print("hello 123".isalnum()) # False

# 12. isspace() → True if only whitespace
print("   ".isspace())   # True
print("  a  ".isspace()) # False

# 13. swapcase() → switches upper → lower and lower → upper
print("Hello World".swapcase())  # 'hELLO wORLD'

# 14. zfill(width) → pads with zeros to the left
print("42".zfill(5))  # '00042'

# 15. center(width, fillchar) → center align with padding
print("hi".center(10, "-"))  # '----hi----'

# 16. ljust(width, fillchar) → left align with padding
print("hi".ljust(10, "*"))  # 'hi********'

# 17. rjust(width, fillchar) → right align with padding
print("hi".rjust(10, "*"))  # '********hi'

# 18. startswith() and endswith() → already covered
# but you can also give a range
print(name2.startswith("dev", 6)) # True (searches starting at index 6)

# 19. partition() → splits into 3 parts: before, separator, after
print(name2.partition("dev")) # ('hello ', 'dev', 'ops')

# 20. rpartition() → same but from right side
print(name2.rpartition("o")) # ('hello dev', 'o', 'ps')
