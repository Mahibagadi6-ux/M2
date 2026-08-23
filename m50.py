# HW

class mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def display(self):
        print(f"{self.brand}cost {self.price}")
m1 = mobile("nokia",10000)
m2 = mobile("iiphone",7000)
print(m1.brand,m1.price)
print(m2.brand,m2.price)
m1.display()
m2.display()


class mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def display(self):
        print(f"{self.brand}cost {self.price}")
m1 = mobile("nokia",10000)
m2 = mobile("iiphone",7000)
print(m1.brand,m1.price)
print(m2.brand,m2.price)
m1.display()
m2.display()

class employee:
    def __init__(self,name,designation,salary = 30000):
        self.name = name
        self.designation = designation
        self.salary = salary
    def display_info(self):
        print(f"{self.name} has  {self.designation} and  his {self.salary}")
s1 = employee("sarah",'ceo',10000)
s2 = employee("edward",'clerk',15000)
s1.display_info()
s2.display_info()


class bankaccount:
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance
    def check_balance(self):
        print(self.__balance)
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if self.__balance < amount:
            print("insufficient balance")
            return
        self.__balance -= amount
        print("withdraw succesfully your reamining money",self.__balance)

a=bankaccount(11234,10000)
a.check_balance()
a.deposit(100)
a.check_balance()
a.withdraw(100)
a.check_balance()







