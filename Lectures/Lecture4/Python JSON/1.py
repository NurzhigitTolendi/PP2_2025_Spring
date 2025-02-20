# JSON - JavaScript Object Notation 
import json 

{
    "name": "Alice", 
    "age": 25, 
    "city": "New York", 
    "skills": ["Python", "JavaScript"]
}

data = {
    "name": "Alice", 
    "age": 25, 
    "city": "New York", 
    "skills": ["Python", "JavaScript"]
}

# python object to JSON
data = {"name": "Alice", "age":25, "city": "New York"}

json_data = json.dumps(data)
print(json_data) # {"name": "Alice", "age": 25, "city": "New York"}
print(type(json_data)) # <class 'str'>

# JSON to python object 
json_string = '{"name": "Alice", "age": 25, "city": "New York"}' 

data = json.loads(json_string)
print(data) # {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(type(data)) # <class 'dict'>
