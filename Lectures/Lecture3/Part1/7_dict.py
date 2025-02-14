# Dictionaries

ourdict = {
    "make": "BMW", 
    "model": "M5 E34", 
    "year": 1995, 
    "color": "Black"
}

print(ourdict)
print(type(ourdict))

ourdict["mileage"] = 100000

print(ourdict)

ourdict.update({"price" : "8 million tenge"})

print(ourdict)