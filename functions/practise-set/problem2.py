# write an program to coverts the Celsius to fahrenheit

# fromula = C/5 = (f-32)/9

def f_to_c(f):
    return 5* (f-32)/9

f = int(input("Enter Temperature in F: "))

c = f_to_c(f)
print(f"{round(c,2)} C")