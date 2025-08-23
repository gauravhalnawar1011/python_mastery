s = {34,45,29,19,13,"devops"} 
print(s,type(s))   # {34, 13, 19, 'devops', 29, 45} <class 'set'>

# if you want to add new element in the sets we use the method called add

# s.add(788)

print(s,type(s))    # {34, 13, 19, 29, 788, 45, 'devops'} <class 'set'>

# properties of sets

# sets are unorderd doesnt maintain an order 
# set are  unindexed can not acees element by index 
# there is no way to chnage items in sets
# sets can not conatin an duplicate values 

print(len(s))  # to print  the len of string 

s.remove("devops") # {34, 13, 19, 29, 45}  removed the devops from the string 


print(s)

s.pop()  # remove an random element from set {13, 19, 29, 45}

print(s)

# ✅ Quick Reference for Set Methods in Python

s = {1, 2, 3}

# --- Adding & Removing ---
s.add(4)            # Add a single element
s.update([5, 6])    # Add multiple elements (list/tuple/set)
s.remove(2)         # Remove element (Error if not found)
s.discard(10)       # Remove element (No error if not found)
x = s.pop()         # Remove and return a random element
s.clear()           # Remove all elements

# --- Set Operations ---
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1, 2} (elements in a but not in b)
print(b.difference(a))   # {4, 5}
print(a.symmetric_difference(b)) # {1, 2, 4, 5}

# --- Update Variants (in-place) ---
a.intersection_update(b)   # Keep only common elements
a.difference_update(b)     # Remove elements also in b
a.symmetric_difference_update(b) # Keep only non-common

# --- Membership & Relations ---
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))   # True
print(b.issuperset(a)) # True
print(a.isdisjoint({4, 5})) # True (no common elements)

# --- Copy ---
c = b.copy()
# ```

# ---

# ✅ **Summary of Set Methods**

# * **Adding/removing** → `add`, `update`, `remove`, `discard`, `pop`, `clear`
# * **Set ops** → `union`, `intersection`, `difference`, `symmetric_difference`
# * **In-place ops** → `intersection_update`, `difference_update`, `symmetric_difference_update`
# * **Relations** → `issubset`, `issuperset`, `isdisjoint`
# * **Copy** → `copy`

# ---

# ⚡ Best Practice:

# * Use `discard` instead of `remove` if you don’t want errors when an element isn’t present.
# * Use set operations (`union`, `intersection`, etc.) instead of loops for cleaner code.



