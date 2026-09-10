
class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0

    def check_balance(self):
        print(f"Your amount is {self._balance}")

    def deposite(self, amount):
        self._balance += amount
        print(f"Your amount successfully deposited: {self._balance}")
        return self._balance

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Your amount successfully withdrawn: {self._balance}")
        else:
            print("Your amount is not enough")


class Savings_Account(Account):
    def calculate_intrest(self):
        interest_rate = 0.03
        interest = self._balance * interest_rate
        print(f"Your interest is {interest}")
        return interest


class Current_Account(Account):
    def withdraw(self, amount):
        over_draft = 1000

        if self._balance + over_draft >= amount:
            self._balance -= amount
            print(f"Your amount successfully withdrawn: {self._balance}")
        else:
            print("Your amount is not enough")


class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__account = {}

    def createAccount(self, id, holder_name, type):
        if type == "savings":
            new_account = Savings_Account(id, holder_name)

        elif type == "current":
            new_account = Current_Account(id, holder_name)

        else:
            print("Invalid account type")
            return None

        # These must be outside the if/elif blocks
        self.__account[id] = new_account
        print("Account creation successful")
        return new_account

    def get_account(self, id):
        if id not in self.__account:
            print("Account does not exist")
            return None
        else:
            account = self.__account[id]
            print(f"Account {account.id} and {account.holder_name} created")
            return account


MBK = Bank("Mahesh Bank of India", "Shorapur")

s1 = MBK.createAccount(1, "Mahesh", "savings")
c1 = MBK.createAccount(2, "Mahesh", "current")

s1.deposite(100)
c1.deposite(10)

s1.withdraw(100)
c1.withdraw(1020)

s1.check_balance()
c1.check_balance()




