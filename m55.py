def add_ithems(self,name,price):
    pass
def get_ithems(self):
    pass
def remove_ithems(self,name):
    pass
def change_ithems(self,name,price):
    pass
def total_price(self):
    pass
def display_ithems(self):
    print("   =======simple cart =====")
    print("1.add ithem\n2.remove ithems\n3.display ithems\n4.change ithems\n5.total price\n6.Exite")
class cart:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._ithems = {}

    def add_ithems(self,product,price):
        self._ithems[product] = price

    def remove_ithems(self):
        self._ithems.remove(self.name)

    def change_ithems(self,product,price):
        self._ithems[product] = price
    def total_price(self):
        total = 0
        for i in self._ithems:
            total += self._ithems[i]
    def display_ithems(self):
        print("   =======simple cart =====")
        print("1.add_ithmes\n2.remove ithems\n3.display ithems\n4.change ithems\n5.total price\n6.Exite")

cart1 =cart("apple",100)
cart2 =cart("banana",200)
cart3 =cart("orange",300)
cart4 =cart("mango",400)
cart5 =cart("grape",500)
cart6 =cart("pear",600)
cart1.add_ithems("apple",100)
cart1.change_ithems("apple",100)
cart1.total_price()









