student = {}
while True:
    print("/n ====== educational system =====\n 1,add system ,\ndisplay student \n 3,exite")
    choice = input("Enter your choice >>> ")
    if choice == "1":
        roll_no = input("Enter your roll no>>>")
        name = input("Enter your name>>>>")
        age = input("Enter your age>>>")
        barch = input("Enter your barch>>>")
        student [roll_no] = {
            "name" : name,
            "age" : age,
            "barch" : barch
        }
        print("Your student has been added")
    elif choice == "2":
        if not student:
            print("Your student has not been added")
        else:
            print("no student avilable")
            for roll_no,details in student.items():
                print(f"Roll no. {roll_no}")
                print(f"Name: {details['name']}")
                print(f"Age: {details['age']}")
                print(f"Barch: {details['barch']}")
                print("  ==========   ")

    elif choice =="3":
        print("thank you")
        break

    else:
        print("invalid choice ,try again")