# 27. Count lines in file
with open("newfile.txt", "r") as f:
    print("Number of lines:", len(f.readlines()))