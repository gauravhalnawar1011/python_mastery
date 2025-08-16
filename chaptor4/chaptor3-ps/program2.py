# write an program to accept marks of 6 students and display them in sorted manner 


students = []

f1 = int(input("Enter the marks of students:"))
students.append(f1)
f2 = int(input("Enter the marks of students:"))
students.append(f2)

f3 = int(input("Enter the marks of students:"))
students.append(f3)

f4= int(input("Enter the marks of students:"))
students.append(f4)

f5 = int(input("Enter the marks of students:"))
students.append(f5)

f6 = int(input("Enter the marks of students:"))
students.append(f6)

f7 = int(input("Enter the marks of students:"))
students.append(f7)

students.sort()
print(students)

# method 2

# students = list(map(int, int(input("Enter the students marks separ)ated by space: ").split()))

# students.sort()

# print(students)

