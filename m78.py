"""Write a program with options to:
Add student details.
Display student details.
Exit."""
def menu():
    print("STUDENT DETAILS ")
    print("1. add student details \n 2. display student details \n 3. exit ")
student = {}
while True:
    menu()
    choice = 1
    if choice in {1,2,3}:
        choice = int(input("Enter your choice:"))
        if choice == 1:
            name = input("Enter your student name:")
            roll_no = input("Enter your roll no:")
            class_no = input("Enter your class no:")
            student[name] = [roll_no, class_no]
            print("Student added successfully.")
        elif choice == 2:
            name = input("Enter your student name:")
            if name in student:
                print(f"{student[name]} is already registered.")
            else:
                print("Student not found.")
        else:
            print("Invalid choice. Please try again.")