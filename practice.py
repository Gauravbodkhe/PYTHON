# file = open("ok.txt","r")
# content=file.read()
# print(content)
# file.close()

# list = [1,1,1,2,3,4,5,6,7,8]
# list.extend[11,12,13]
# print(list)

# class Car:
#     name=" "
#     speed =0

# suzuki=Car()
# mahindra= Car()
    
# suzuki.name="Swift"
# suzuki.speed=180
# print(f"Name:{suzuki.name},speed:{suzuki.speed}")

# class Car:
#     name=""
#     speed =0

# suzuki = Car()
# mahindra = Car()

# suzuki.name="ertige"
# suzuki.speed=180
# print(f"Name:{suzuki.name},Speed:{suzuki.speed}")

# mahindra.name="bolero"
# mahindra.speed=121
# print(f"Name:{mahindra.name},Speed:{mahindra.speed}")

# string = "dddgggfffjjj"
# for i in string :
#     if i=='d' or i=='f':
#         continue
#     print(i,end='')


# for i in range (1,101):
#     if i%3==0 and i%9!=0:
#         print(i)

# 

# amount=float(input("Enter a amount:"))
# if amount > 10000:
#     discount=amount*0.20
# elif amount > 5000:
#     discount=amount*0.10
# elif amount >1000 :
#     discount = amount*0.05
# else:
#     discount=0
# total_bill=amount-discount

# print("Discount=",discount)
# print("you have to pay=",total_bill)

# class Car:

#     name=""
#     speed=0

# farrari=Car()
# ford=Car()

# farrari.name="rr"
# farrari.speed=330
# print(f"Name:{farrari.name},Speed:{farrari.speed}")

# ford.name="end"
# ford.speed=270
# print(f"Name:{ford.name},Soeed:{ford.speed}")

# 

# 

# from math import sqrt,sin
# a=16
# b=3.12
# print(sqrt(a))
# print(sin(b))


# Book_auther = {
#     "A":"Z",
#     "B":"Y",
#     "C":"X"
# }

# print(Book_auther["B"])
# Book_auther ["D"]="W"
# print(Book_auther)

# name_surname = {
#  "John": "Doe",
#  "Jane": "Doe",
#  "Alice": "Smith"
# }
# name_surname ["shubham"]="sonawane"
# print(name_surname)

# tup1 = (1, 2, 3, 4, 5)
# tup2 = (6, 7, 8, 9, 10)
# print(tup1+tup2)

int(input("Enter a value for factorial:"))
factorial=1
for i in range(1,num+1):
    factorial *= i
    print(f"The factorial of {num} is {factorial}")