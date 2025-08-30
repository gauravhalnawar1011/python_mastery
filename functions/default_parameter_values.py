# Default Parameter Value
# The following example shows how to use a default parameter value.

# If we call the function without argument, it uses the default value:



def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

''' factorial 
factorial(0): 1
factorial(1): 1
factorial(2): 2 X 1
factorial(3):3 X 2 X 1
factorial(4):4 X 3 X 2 X 1
factorial(5):5 x 4 X 3 X 2 X 1
factorial(n): n x n-1 X .... 3 X 2 X 1


factorial = n * factorial (n-1)


'''

def factorial(n):
  if (n == 1 or n == 0):
    return 1
  return n * factorial(n-1)

n = int(input("Enter Your Number : "))
print(f"The factorial of the number {factorial(n)} is ")