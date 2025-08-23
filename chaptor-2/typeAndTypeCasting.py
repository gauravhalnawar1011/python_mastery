# type() Table
# Value	Code Example	Result of type()
# String	"hello"	<class 'str'>
# Integer	42	<class 'int'>
# Float	3.14	<class 'float'>
# Boolean	True	<class 'bool'>
# List	[1, 2, 3]	<class 'list'>
# Tuple	(1, 2, 3)	<class 'tuple'>
# Dictionary	{"name": "Alice", "age": 25}	<class 'dict'>
# Set	{1, 2, 3}	<class 'set'>


a = "31"
b= int(a)


t= type(b)
print(a)
print(t)


# Examples of type() in Python

print(type("hello"))                   # str
print(type(42))                        # int
print(type(3.14))                      # float
print(type(True))                      # bool
print(type([1, 2, 3]))                  # list
print(type((1, 2, 3)))                  # tuple
print(type({"name": "Alice", "age": 25})) # dict
print(type({1, 2, 3}))                  # set
