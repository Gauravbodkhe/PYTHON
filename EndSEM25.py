# 25. Append user input to file
with open("newfile.txt", "a") as f:
    data = input("Enter text to append: ")
    f.write("\n" + data)