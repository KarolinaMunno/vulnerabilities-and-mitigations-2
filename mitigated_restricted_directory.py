import os

FILE_DOWNLOAD = "C:/Users/user1/Downloads"

def safe_directory(file_name, file_data):
    safe_file = os.path.basename(file_name)
    file_path = os.path.join(FILE_DOWNLOAD, safe_file)
    with open(file_path, "w") as f:
        f.write(file_data)
    
safe_directory("../malicious.py", "You haven't been hacked")
