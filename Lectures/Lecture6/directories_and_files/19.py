file_name = 'new.txt' # relative path - the file should exist
# at the current working directory
# check os.getcwd() and os.listdir(path)

with open(file_name, 'x') as file: # create mode
    pass
# in create mode, if a file exists, we get an error