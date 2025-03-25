import os

path = './' # relative path
# .. - shorthand for previous directory
# .  - shorthand for current directory

contents = os.listdir(path)

print(contents)

for element in contents:
    print(element)