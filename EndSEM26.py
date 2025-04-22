# 26. Read file line by line
with open("newfile.txt", "r") as f:
    for line in f:
        print(line.strip())