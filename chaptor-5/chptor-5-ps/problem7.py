# in folwlwing progam what happens when the user enter same name twice ?

dict = {}

name = input("Enter you name: ")
lang = input(("Enter your lang: "))

dict.update({name:lang})
name = input("Enter you name: ")
lang = input(("Enter your lang"))

dict.update({name:lang})
name = input("Enter you name: ")
lang = input(("Enter your lang: " ))

dict.update({name:lang})
name = input("Enter you name: ")
lang = input(("Enter your lang: "))

dict.update({name:lang})

print(dict) 
# Enter you name: sur 
# Enter your lang: c
# Enter you name: gap 
# Enter your langjava 
# Enter you name: lorvord
# Enter your lang: python 
# Enter you name: sur 
# Enter your lang: golang
# {'sur ': 'golang', 'gap ': 'java ', 'lorvord': 'python '}


# it will print the updated new value for the user




