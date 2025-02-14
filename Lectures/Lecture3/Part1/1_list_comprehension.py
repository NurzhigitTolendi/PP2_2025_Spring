"""
Plan for the lecture:
- List Comprehension
- Tuples, Sets, Dictionaries - briefly
- Functions
- Lambda Functions
- Classes and Objects
- Inheritance
"""

# List comprehension

ourlist = []

for i in range(1, 6):
    ourlist.append(i)

print(ourlist)

ourlist.clear()

# filling a list with list comprehension
ourlist = [x for x in range(1, 6)]
# syntax: new_list = [expression for item in some_iterable if condition]

print(ourlist)

anotherlist = [x * 2 for x in range(1, 6) if x % 2 != 0]

print(anotherlist)

# removing spaces from string 
words = ["apple ", " banana ", " cherry"]
clealed_words = [word.strip() for word in words]
print(clealed_words)

