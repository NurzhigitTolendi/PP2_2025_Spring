print(len([1, 2, 3])) # 3
print(max(10, 20, 30)) # 30

max = 100 # Now max is var, but not a function
# print(max(10, 20)) # Error! max is not function no more 

del max # We delete var max, return access to the function max()
print(max(10, 20)) # 20 