# enscapsulation means that old s the data in class means variable and funtion togehter in a class
#why enscapulation 1, protect data ,contole the access and improve security
#keeps code reconized
class bankAccount:
    def __init__(self,bankbalance):
        self.bankbalance = bankbalance
    def deposit(self,amount):
        self.bankbalance += amount
    def withdraw(self,amount):
        if amount <= self.bankbalance:
            self.bankbalance -= amount
    def get_balance(self):
        return self.bankbalance
account1 = bankAccount(200000)
account2 = bankAccount(5000)
print(account1.get_balance() - account2.get_balance())








