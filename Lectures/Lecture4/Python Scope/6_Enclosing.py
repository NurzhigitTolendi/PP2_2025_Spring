def outer():
    x = "outer var"

    def inner():
        print(x) # Access to the var from enclosing scope 

    inner()

outer()