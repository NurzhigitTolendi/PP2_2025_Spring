# Classes and objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

person1 = Person("Mark", 8)
person2 = Person("Ramazan", 9)

print(person1.name)
print(person1.age)

print(person2.name)
print(person2.age)