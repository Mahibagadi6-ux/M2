class ATM:
    def __init__(self, holder_name,bank_balance):
        self.holder_name = holder_name
        self.bank_balance = bank_balance
    def deposite(self,amount):
        self.bank_balance += amount
        print(self.bank_balance)
    def withdraw(self,amount):
        if self.bank_balance >= amount:
            self.bank_balance -= amount
        else:
            print("Not enough money")
    def display(self):
        print(self.bank_balance)
atm = ATM("mahesh",10000)
print(atm.holder_name)
atm.deposite(100)
atm.display()
atm.withdraw(1000)
atm.display()