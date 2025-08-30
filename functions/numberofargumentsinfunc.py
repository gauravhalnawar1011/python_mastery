# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments,
#  you have to call the function with 2 arguments, not more, and not less.

# Example
# This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


# Example
# This function expects 2 arguments, but gets only 1:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil") #TypeError: my_function() missing 1 required positional argument: 'lname'


