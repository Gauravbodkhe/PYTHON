# 2. Count vowels in a string
string = "Hello World"
vowels = 'aeiouAEIOU'
count = 0
for char in string:
    if char in vowels:
        count += 1
print("\nNumber of vowels:", count)