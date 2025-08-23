# write an program 


marks1 = int(input("Enter the Marks 1: "))
marks2 = int(input("Enter the Marks 2: "))
marks3 = int(input("Enter the Marks 3: "))


# check for the total percentage 

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage >= 40 and marks1 >=33 and marks2 >= 33 and marks3 >= 33):
    print("You are Pass",total_percentage)
else:
    print("you failed,try again next year",total_percentage)


