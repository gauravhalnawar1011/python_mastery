import os

# specify the dir you want to list

directory_path = '/home'
# list all the files and dir in specified path
contents =os.listdir(directory_path)

# print each fiile and dir name
for item in contents:
    print(item)