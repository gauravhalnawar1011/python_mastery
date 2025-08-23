 # if elif else ladder
age = int(input("Enter You age: "))



if age >=18:
    print("Your age is above the consent")
    print("Your eligible for the vote")
elif (age <0):
    print("you are enterig and invalid age")
elif (age ==0):
    print("you are enterig 0 which is invalid ")
else:
    print("Your age is below age of consent ")

print("so your age is", age)
