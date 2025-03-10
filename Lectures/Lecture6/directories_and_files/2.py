import os

path = r'C:\Users\chris\OneDrive\Документы\PP2_2025_Spring\Lectures\Lecture6\directories_and_files' # absolute path
# .. - shorthand for previous directory
# .  - shorthand for current directory

contents = os.listdir(path)

for element in contents:
    print(element)