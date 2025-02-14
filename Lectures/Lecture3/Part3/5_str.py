# OOP - Object Oriented Programming
# 4 Principles of OOP: abstract, inheritance, polymorphism, incapsulation 

# Classes and objects 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
person1 = Person("Mark", 8)
person2 = Person("Ramazan", 9)

print(person1)
print(person2)