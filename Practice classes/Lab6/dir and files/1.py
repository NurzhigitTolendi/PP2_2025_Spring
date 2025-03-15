import os

def list_files_and_dirs(path):
    all_items = os.listdir(path)
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    return directories, files, all_items

path = "."  # directory
dirs, files, all_items = list_files_and_dirs(path)
print(f"Directories: {dirs}")
print(f"Files: {files}")
print(f"All items: {all_items}")
