class Student:
    def __init__(self, roll_no, name, age):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average_mark(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average_mark():.2f}")


students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Add Mark")
    print("3. Display All Students")
    print("4. Search Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = int(input("Enter roll number: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        students.append(Student(roll_no, name, age))
        print("Student added successfully.")

    elif choice == "2":
        roll_no = int(input("Enter roll number: "))
        found = False
        for student in students:
            if student.roll_no == roll_no:
                mark = float(input("Enter mark: "))
                student.add_mark(mark)
                print("Mark added successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "3":
        if not students:
            print("No students available.")
        else:
            for student in students:
                print("\n-----------------")
                student.display()

    elif choice == "4":
        roll_no = int(input("Enter roll number to search: "))
        found = False
        for student in students:
            if student.roll_no == roll_no:
                print("\nStudent Found:")
                student.display()
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
