# f=open("ok.txt","r")
# print(f.read())

f= open("ok.txt","w")
f.write("Do Not use is Anywhere")

f= open("ok.txt",'a')
f.write("Hello World")
f.close()