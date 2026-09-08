def menu():
    print(". wellcome to our grocery store \n 1. add item \n 2. remove item \n 3.view total price \n 4. exite")
cart = {}
while True:
    menu()
    choice = 1
    if choice in {1,2,3,4,5}:
        choice = int(input("Enter your choice:"))
    if choice == 1:
        item_name= input("Enter your item name:")
        price = int(input("Enter your item price:"))
        quantity = int(input("Enter your quantity:"))
        cart[item_name] = [price, quantity]
        print("Item added.")
    elif choice == 2:
        item_name = input("Enter you want remove item name:")
        if item_name in cart:
            quantity = int(input("Enter your quantity to remove:"))
            if quantity >= cart[item_name][1]:
                del cart[item_name]
                print("Item removed successfully.")
            else:
                cart[item_name][0] -= quantity
                print("Item quantity updated.")

    elif choice == 3:
        total = 0
        for item in cart:
            qty, price = cart[item]
            total += qty * price
            print(f"Total price: {total}")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


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
                print(f"Student {name} already exist.")
            else:
                print("Student not found.")
        else:
            print("Invalid choice. Please try again.")


