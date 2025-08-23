# ================================
#  Dictionary Methods in Python
# ================================

# Sample dictionary
marks = {"shubham": 100, "ganesh": 34, "krishna": 40}

# 1. clear() → Remove all items
marks_copy = marks.copy()
marks_copy.clear()
print("clear():", marks_copy)   # {}

# 2. copy() → Shallow copy
marks_copy = marks.copy()
print("copy():", marks_copy)    # {'shubham': 100, 'ganesh': 34, 'krishna': 40}

# 3. fromkeys(seq, value) → Create dict from keys with default value
new_dict = dict.fromkeys(["a", "b", "c"], 0)
print("fromkeys():", new_dict)  # {'a': 0, 'b': 0, 'c': 0}

# 4. get(key, default) → Return value or default if key not found
print("get():", marks.get("shubham"))       # 100
print("get() with default:", marks.get("renuka", 50))  # 50

# 5. items() → Key-value pairs as tuples
print("items():", list(marks.items()))      # [('shubham', 100), ('ganesh', 34), ('krishna', 40)]

# 6. keys() → Only keys
print("keys():", list(marks.keys()))        # ['shubham', 'ganesh', 'krishna']

# 7. values() → Only values
print("values():", list(marks.values()))    # [100, 34, 40]

# 8. pop(key, default) → Remove and return item
popped_value = marks.pop("ganesh")
print("pop():", popped_value)               # 34
print("after pop:", marks)                  # {'shubham': 100, 'krishna': 40}

# 9. popitem() → Remove last inserted (key, value)
last_item = marks.popitem()
print("popitem():", last_item)              # ('krishna', 40)
print("after popitem:", marks)              # {'shubham': 100}

# 10. setdefault(key, default) → Return value if key exists, else add with default
marks.setdefault("renuka", 80)
print("setdefault():", marks)               # {'shubham': 100, 'renuka': 80}

# 11. update() → Merge with another dictionary
marks.update({"krishna": 99, "ganesh": 45})
print("update():", marks)                   # {'shubham': 100, 'renuka': 80, 'krishna': 99, 'ganesh': 45}
