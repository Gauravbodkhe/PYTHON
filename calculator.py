choice = input("Choose an operation (A/B/C/D): ")
if choice in ['A', 'B', 'C', 'D']:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 'A':
        print("Result:", num1 + num2)
    elif choice == 'B':
        print("Result:", num1 - num2)
    elif choice == 'C':
        print("Result:", num1 * num2)
    elif choice == 'D':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero.")
else:
    print("Invalid choice.")

