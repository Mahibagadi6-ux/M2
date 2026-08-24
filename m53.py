items =  {
    "apple":10,
    "banana":20,
    "orange":30,
    "mango":40,
    "pineapple":50,
    "grape":60,
}
cart = {}
while True:
    print("=======  GROCERY STORE ====== ")
    print("1.add item")
    print("2.remove item")
    print("3.view items")
    print("4.view cart")
    print("5.exit")
    choice = input("Enter your choice:")
    if choice == "1":
        print("avilable items")
        for item, price in items.items():
            print(f"{item}: {price}")
        item = input("Enter the item name :").lower()
        if item in items:
            quanitity = int(input("Enter quantity of items to add:"))
            cart[item] = cart.get(item, 0) + quanitity
            print(f"{quanitity}: {cart[item]} added to cart")
        else:
            print("Item is not avilable")
    elif choice == "2":
        item = input("Enter the item name :").lower()
        if item in cart:
            del cart[item]
            print(f"{item}: removed from cart")
        else:
            print("Item is not in cart")
    elif choice == "3":
        total = 0
        for item, quantity in cart.items():
            total += items[item]*quantity
            print(f"total price: {total}")
    elif choice == "4":
        if not cart:
            print("cart is empty")
        else:
            print("====== YOur cart ======")
            for item, quantity in cart.items():
                price = items[item] * quantity
                print(f"{item} x {quantity}: {price}")
    elif choice == "5":
        print("thanku for visiting our mart")
        break
    else:
        print("invalid choice ,try again")




