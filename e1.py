age = int(input("Please enter your age: "))


if age < 13:
    stage = "You Are Child"
elif 13 <= age <= 19:
    stage = "You Are Teenager"
elif 20 <= age <= 64:
    stage = " You Are Adult"

else:
    stage = "You Are Senior"

print(stage)