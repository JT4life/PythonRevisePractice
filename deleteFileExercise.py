import os
if os.path.isfile("file.txt"):
    os.remove("file.txt")
else:
    print("File does not exists")