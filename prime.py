#write a program to print all the prime numbers in a given interval.
n = int(input("Enter the number: "))
for n in range(2, n):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)