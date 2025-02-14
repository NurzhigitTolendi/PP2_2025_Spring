# Sets 

ourset = {"Batman", "Wonder Woman", "Superman"}

ourset.add("Flash")
ourset.add("Lex Luthor")
ourset.add("Robin")

print(ourset)

if "Lex Luthor" in ourset:
    print("Lex is here!")
else:
    print("Lex is not here, he is hiding")

if "Batman" in ourset:
    print("Batman found")
else:
    print("Batman not found, he's in Gotham")

if "Homelander" not in ourset:
    print("Happily, not found")
else:
    print("He's here! Run!")