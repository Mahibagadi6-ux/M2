def menu():
    print("------- WELLCOME TO OUR BANK --------")
    print("1.check balance\n 2. deposite \n 3. withdrow \n 4.Quite ")
balance = 0
while True:
    menu()
    choice = 1
    if choice in {1,2,3,4}:
        choice = int(input("Enter your choice:"))
    if choice == 1:
        print("Your balance is: ", balance)
    elif choice == 2:
        amount = int(input("Enter your amount: "))
        balance += amount
        print("Your balance is: ", balance)
    elif choice == 3:
        amount = int(input("Enter your amount: "))
        balance -= amount
        print("Your balance is: ", balance)
        break
    elif choice == 4:
        print("Quite")
    else:
        print("Invalid choice")


