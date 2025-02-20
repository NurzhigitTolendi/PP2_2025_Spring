def outer():
    x = 5

    def inner():
        x = 10 # this is local var, not changed var x
        print("Inside inner: ", x) 

    inner()
    print("Inside outer: ", x) # 5 (outer x did not change)

outer()