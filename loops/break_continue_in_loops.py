for i in range(101):
    if i == 34: # this loop only run till the 34 it will not print remaining numbers (exit the loop right now)
    
        break
    print(i)


for i in range(101):
    if i == 34: # skip the 34 number from the loop and print 0 to 100 except 34
        continue
    print(i)



n = int(input("Enter the table number which you want to generate: "))
for i in range(1,11):
    print(f"{n} X {i} = {n * i}")

n = int(input("Enter the table number which you want to generate: "))
i = 1
while i<10:
    print(f"{n} x {i}= {n*i}")
    i += 1
