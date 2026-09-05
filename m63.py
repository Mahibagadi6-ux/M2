class ATMmachineSBI:
    def __init__(self):
        self.pin = ""
        self.balance = 0
    def menu(self):
        user_input = input("tell me how can i help you\n 1,press to creat the pin\n 2,change pin \n 3, withdrow the amount\n 3,Exite ")
        if user_input == "1":
            self.creat_pin()
            pass
        elif user_input == "2":
            self.change_pin()
            pass
        elif user_input == "3":
            self.check_balance()
            pass
        elif user_input == "4":
            self.withdrow_balance()
            pass
        else:
            print("you choose the invalid option")
    def creat_pin(self):
        creat_pin = input("enter the your pin: >>")
        self.pin =  creat_pin
        user_balance = int("Enter your balance: >>>")
        self.balance = user_balance
        print("your pin is created successfully")
        self.menu()
    def change_pin(self):
        old_pin = input("enter the new pin to change: >>")
        if old_pin == self.pin:
            new_pin = input("enter the new pin to change: >>")
            self.pin = new_pin
            print(f"your pin is changed successfully and your pin is {new_pin}")
        else:
            print(f"your entered old pin is {old_pin} and new pin is")
            self.menu()
    def check_balance(self):
        user_pin = input("Enter your pin to check the balance: >>")
        if user_pin == self.pin:
            print(f"your balance is {self.balance}")
            self.menu()
    def withdrow_balance(self):
        user_pin = input("Enetr your pin to withdrow the balance: >>")
        if user_pin == self.pin:
            amount = input("enter the amount to withdrow the balance: >>")
            if amount <= self.balance:
                self.balance -= amount
                print(f"your withdrow amount{self.amount}  and your balance is {self.balance}")
            else:
                print("your accont in in sufficient amount ")
                self.menu()
sbi = ATMmachineSBI()







