import os

def check_path_access(path):
    return {
        "Exists": os.path.exists(path),
        "Readable": os.access(path, os.R_OK),
        "Writable": os.access(path, os.W_OK),
        "Executable": os.access(path, os.X_OK)
    }

path = "."  
access_info = check_path_access(path)
for key, value in access_info.items():
    print(f"{key}: {value}")
