# Tuples 

ourtuple = ("Say my name", "I am the one who knocks", 2008, "Better call Saul", "Welcome to Los Pollos Hermanos family")

Heisenberg, Walter, year, Saul, Gus = ourtuple

print(Heisenberg)
print(Walter)
print(year)
print(Saul)
print(Gus)

# tuples slicing 
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4]) # (1, 2, 3)
print(numbers[:3]) # (0, 1, 2)
print(numbers[::2])

# tuples are immutable 
my_tuples = (1, 2, 3)
my_tuples[0] = 5 # Error: 'tuple' object does not support item assignment 

# tuples are faster than lists