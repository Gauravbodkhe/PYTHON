# 28. Count words in file
with open("newfile.txt", "r") as f:
    print("Number of words:", len(f.read().split()))