# Dictionary to store student records
students = {}

# Function to add a student record
def add_student():
    try:
        roll_number = int(input("Enter Roll Number: "))
        if roll_number in students:
            print("Error: Roll number already exists!")
            return
        
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        
        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100!")
            return
        
        students[roll_number] = {"Name": name, "Marks": marks}
        print("Student added successfully!")
    except ValueError:
        print("Error: Invalid input! Roll number must be an integer, and marks must be a number.")

# Function to view all student records
def view_students():
    if not students:
        print("No student records found!")
    else:
        print("\nStudent Records:")
        for roll_number, details in students.items():
            print(f"Roll Number: {roll_number}, Name: {details['Name']}, Marks: {details['Marks']}")

# Function to update a student record
def update_student():
    try:
        roll_number = int(input("Enter Roll Number to update: "))
        if roll_number not in students:
            print("Error: Roll number not found!")
            return
        
        name = input("Enter new Name (leave blank to keep current): ")
        marks = input("Enter new Marks (leave blank to keep current): ")
        
        if name:
            students[roll_number]["Name"] = name
        if marks:
            try:
                marks = float(marks)
                if marks < 0 or marks > 100:
                    print("Error: Marks must be between 0 and 100!")
                    return
                students[roll_number]["Marks"] = marks
            except ValueError:
                print("Error: Marks must be a number!")
                return
        
        print("Student record updated successfully!")
    except ValueError:
        print("Error: Roll number must be an integer!")

# Function to delete a student record
def delete_student():
    try:
        roll_number = int(input("Enter Roll Number to delete: "))
        if roll_number not in students:
            print("Error: Roll number not found!")
            return
        
        del students[roll_number]
        print("Student record deleted successfully!")
    except ValueError:
        print("Error: Roll number must be an integer!")

# Function to search for a student record
def search_student():
    try:
        roll_number = int(input("Enter Roll Number to search: "))
        if roll_number not in students:
            print("Error: Roll number not found!")
            return
        
        student = students[roll_number]
        print(f"\nStudent Found:")
        print(f"Roll Number: {roll_number}, Name: {student['Name']}, Marks: {student['Marks']}")
    except ValueError:
        print("Error: Roll number must be an integer!")

# Function to generate a grade report
def generate_grade_report():
    if not students:
        print("No student records found!")
    else:
        print("\nGrade Report:")
        for roll_number, details in students.items():
            marks = details["Marks"]
            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            else:
                grade = "D"
            print(f"Roll Number: {roll_number}, Name: {details['Name']}, Marks: {details['Marks']}, Grade: {grade}")

# Main menu
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Generate Grade Report")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            generate_grade_report()
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()