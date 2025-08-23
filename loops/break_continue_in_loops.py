for i in range(101):
    if i == 34: # this loop only run till the 34 it will not print remaining numbers (exit the loop right now)
    
        break
    print(i)


for i in range(101):
    if i == 34: # skip the 34 number from the loop and print 0 to 100 except 34
        continue
    print(i)