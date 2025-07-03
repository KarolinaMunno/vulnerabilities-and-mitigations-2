import os

FILE_DOWNLOAD = "C:/Users/user1/Downloads"

def unsafe_directory(file_name, file_data):
    file_path = os.path.join(FILE_DOWNLOAD, file_name)
    with open(file_path, "w") as f:
        f.write(file_data)
    
unsafe_directory("../malicious.py", "You've been hacked")
