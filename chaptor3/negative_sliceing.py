name = "devops"

# Indexing reference:
#   d   e   v   o   p   s
#   0   1   2   3   4   5   (positive index)
#  -6  -5  -4  -3  -2  -1   (negative index)


# Slice from index 0 up to (but not including) index 3
# → starts at 'd' (0), ends before 'o' (3)
dev = name[0:3]
print(dev)   # Output: 'dev'


# Negative indexing: slice from -6 (d) up to -3 (o, exclusive of p)
negative_slice = name[-6:-3]
print(negative_slice)  # Output: 'dev'


# [:] → full string (default: from start to end)
print(name[:])   # Output: 'devops'


# [1:] → from index 1 to end
# → skips the first character 'd'
print(name[1:])  # Output: 'evops'


# [:6] → from start (0) to index 6 (exclusive)
# → length of "devops" is 6, so this gives the whole string
print(name[:6])  # Output: 'devops'


# [0:] → from index 0 to end
# → also gives the full string
print(name[0:])  # Output: 'devops'


# --- Extra tricks with slicing ---

# [::2] → take every 2nd character (step = 2)
print(name[::2])  # Output: 'dvp'

# [::-1] → step -1 means reverse the string
print(name[::-1]) # Output: 'spoved'
