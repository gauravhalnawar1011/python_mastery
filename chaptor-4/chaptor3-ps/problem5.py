# write program to find 0 in the tuple

a = (0, 12 , 33, 56, 9, 0, 6, 0)

n = a.count(0)

print(n)

# method2

a = (0, 12, 33, 56, 9, 0, 6, 0)

indexes = [i for i, val in enumerate(a) if val == 0]

print("Count:", a.count(0))
print("Indexes:", indexes)
