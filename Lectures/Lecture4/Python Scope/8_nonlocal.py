def outer():
    x = 5

    def inner():
        nonlocal x 
        x = 10 # Now we are changing x in outer scope 
        print("Inside inner: ", x) 

    inner()
    print("Inside outer: ", x) # 10

outer()