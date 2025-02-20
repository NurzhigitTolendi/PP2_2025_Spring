# iterators and generators

"""
iterator
An iterator is an object which contains countable number of values 
and it is used to iterate over iterable objects 
like lists, tuples, sets, etc.

"""

# https://docs.python.org/3/tutorial/classes.html#iterators

our_list = [1, 2, 3] # iterable 

our_list_iter = iter(our_list) # iterator 

print(next(our_list_iter)) # 1
print(next(our_list_iter)) # 2
print(next(our_list_iter)) # 3

print(next(our_list_iter)) # StopIteration