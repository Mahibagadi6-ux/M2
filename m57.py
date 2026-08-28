class item:
    def __init__(self,name:str,price:float):
        self.name = name
        self.price = price
class shoppingcart:
    def __init__(self):
        self.cart = {}
    def add_item(self,item,quantity):
        if quantity <= 0:
            print("quantity must be greater than one ")
            return
        if item.name in self.cart:
            self.cart[item.name]["quantity"] += quantity
        else:
            self.cart[item.name] = {f"price":item.price,"quantity":quantity}
        print(f"added {quantity}x{item.name} to  your cart")
    def remove_item(self,item,quantity):
        """reduse the ithmes in the cart """
        if item.name not in self.cart:
            print("item not in cart")
            return
        if quantity <= 0:
            print("quantity must be greater than one ")
            return
        currentqty = self.cart[item.name]["quantity"]
        if quantity >= currentqty:
            del self.cart[item.name]
            print(f"removed all {item.name} from your cart")
    def calculate_total(self):
        return sum(details["price"]* details["quantity"] for details in self.cart.values())
    def view_cart(self):
        if not self:
            print("\n your cart is completaly empty")
        print("   ==   current cart   ==    ")
        for name ,details in self.cart.items():
            print(f"{name} -- quantity: {details['quantity']} , price: {details['price']}")
        print(f"total price: {self.calculate_total()}")
        print("------------------")
class Grocerystore:
    def __init__(self):
        self.inventory = {
            "1":item("apple",100),
            "2":item("orange",50),
            "3":item("banana",40),
            "4":item("mango",30),
            "5":item("cofee",8.99),
            "6":item("eggs",15),
            "7":item("bread",10)
        }
        self.cart = shoppingcart()
    def display_inventory(self):
        print(f"\n ====inventory groceries ===:")
        for key,item in self.inventory.items():
            print(f"{key}: {item.name} - price: {item.price}")
        print(" -------------------")
    def run(self):
        print("\n ====  welcome shopping cart ==== ===:")

        while True:
            print("\n  view menu  ")
            print("  1. add item  ")
            print("  2. remove item  ")
            print("  3. view item and total  ")
            print("  4. exite  ")
            choice  = input("Enter your choice: ").strip()
            if choice == "1":
                self.display_inventory()
                item_choice = input("Enter your choice: ")
                if item_choice.lower() == "b":
                    continue
                if item_choice in self.inventory:
                    try:
                        qty = int(input("Enter quantity: "))
                        self.cart.add_item(self.inventory[item_choice],qty)
                    except ValueError:
                        print("invalid input")
                else:
                     print("invalid inventory selection ")
            elif choice == "2":
                if not self.cart.cart:
                    print("nothing is removed your cart alreday empty")
                    continue
                self.cart.view_cart()
                name_to_remove = input("Enter the exact name of the  item to remove: ")
                try:
                    qty_to_remove = int(input("Enter quantity: ")).strip()
                    self.cart.remove_item(name_to_remove,qty_to_remove)
                except ValueError:
                    print("input quantity is invalid")
            elif choice == "3":
                self.cart.view_cart()
            elif choice == "4":
                print(f"final total  amount : {self.cart.calculate_total()}")
                print("tq for visiting our shopping cart")
                break
            else:
                print("invalid position selection ")



if __name__ == "__main__":
    store = Grocerystore()
    store.run()








