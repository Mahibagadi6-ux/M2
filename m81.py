class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
class cart:
    def __init__(self):
        self.items = []
    def add_product(self,product):
        self.items.append(product)
        print( product.name,"added product ")
    def show_cart(self):
        for product in self.items:
            print(product.name,"-",product.price)
    def total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price
    def Quantity(self):
        return len(self.items)
    def remove_product(self,remove_product):
         if remove_product in self.items:
             self.items.remove(remove_product)
             print(remove_product.name,"removed product ")
         else:
             print("Product not found.")
    def discount_price(self,discount_price):
        total_price = self.total_price()
        if len(self.items) >= 10:
            total_price = total_price - discount_price
            return total_price

        else:
            print("you didn't purchased the greter than 10 itmes .")




p1 = product("laptop",60000)
p2 = product("chair",50)
p3 = product("bangara",10000)
cart = cart()
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)
cart.show_cart()
cart.total_price()
cart.remove_product(p1)
cart.discount_price(10)
print(cart.total_price())
