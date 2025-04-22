# 30. Check if file exists
import os
filename = "newfile.txt"
if os.path.exists(filename):
    print("File exists")
else:
    print("File does not exist")