def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen)) # 1 
print(next(gen)) # 2
print(next(gen)) # 3 

# print(next(gen)) # StopIteration 

for num in my_generator():
    print(num)

def example():
    yield "Hello"
    yield "World"

gen = example()
print(next(gen)) # Hello
print(next(gen)) # World 
 
print(next(gen)) # StopIteration 