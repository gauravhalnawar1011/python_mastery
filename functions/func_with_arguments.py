# Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:



def myfunc(fname):
    print(fname+ 'devops ')

myfunc('email ')
myfunc("body ")
myfunc("skill ")


def test1(movies):
    print(movies + "marval")
test1("avengers ")
test1("mahi ")


def test2(heros):
    print(heros+ "my fav")
test2('john ')
test2("cena ")


def devopstolls(tools):
    print("My fav "+tools+"i love this")
devopstolls("aws ")
devopstolls("jnekins ")
devopstolls("gitlab ")


def docker(commands):
    print("My fav Docker Commands are  "+commands+"!")
docker("rm")
docker("run")
docker("start")
docker("Stop")


def my_function(fname):
  print(fname+ "devops")
my_function("hello ")