def menu():
    print("1. wellcome to our grocery store \n 2. add item \n 3. remove item \n 4.view total price \n 5. exite")
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
        if item_name in cart:
            cart[item_name][0] += quantity
        else:
            cart[item_name] = [price, quantity]
    elif choice == 2:
        item_name = input("Enter you want remove item name:")
        if item_name in cart:
            quantity = int(input("Enter your quantity to remove:"))
            if quantity >= cart[item_name][0]:
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
