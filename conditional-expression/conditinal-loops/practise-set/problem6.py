name = "python"

if name == "java" or "html":
    print("Login Done")
else:
    print("Not Valid")


x = {}
x[1] = 'one'
x[True]= 'true'
x[1.0]='float'

print(x)


x = 1
if x >8:
    print("Big")
else:
    print("small")

n = 20
if n ==15:
    print("hello")
else:
    print("world")

print(sum([1,2,3],10))
print(min("hello"))


print('-'.join(['2025','08','11']))

a = [1,2,3]
b = a
b.append(4)
print(a)


print(pow(4,4))

print(5 == 4 +1)

a = float(3)
print(a)

x = "10"
x += "5"  

result = int(x) // 3 # int(x) converts the string '105' to int 105 105//3 = 35

print(result)


print([x for x in range(10) if x % 2 == 0])

x = 5
x **=3
print(x)



x = [10,20,30]

y = x
y[1] = 99
print(x)


x = bool(0)
print(x)


#print(1 /0)  # zero division error 


a = (10,20,20)
x,y,z = a

print(y)


thistuple = ("naz","somu", "krishna")

y = ("anjali",)
thistuple += y

print(thistuple)