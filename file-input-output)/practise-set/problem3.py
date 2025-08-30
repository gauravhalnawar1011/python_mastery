# write an program to genrate and mutiplcation table from 1 to 20 and write it in the differnt place them into an folder called multiplciation-tables


def generatetable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2,20):
    generatetable(i)
