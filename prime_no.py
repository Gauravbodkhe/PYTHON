#write a pgm to print all thr prime numbers in a given interval
a=int(input("Enter the nummber:"))

if a%2==0:
    print("It is an not prime number")
elif a%3==0:
    print("It is an not prime number")
elif a%2!=0:
    print("a is prime Nummber")
else:
    print("Given Number is Zero")
