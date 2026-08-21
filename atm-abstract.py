"""abs abtaction is the main role in building any atm account its hides the unnecessary implemenation details and
and showing  only essential information to user like atm machine in built in machine these programs
 when using atm card ask the insert card, and enter the pin  and choose withdrow , enter the amount  and recive money
in this type we want creat the abstarct method """
from abc import ABC,abstractmethod # abc means python provides the abc module for implimant the abstarct method
# ABC is class provided by python
# abstractmethod is a decorater means this method implimented by child class
class ATM(ABC):# ATM class will define the basic rules and ATM is inherit from the ABC
    @abstractmethod
    def withdrow(self,amount):
        pass

    @abstractmethod
    def deposite(self,amount):
        pass
    @abstractmethod
    def check_balanance(self):
        pass
class MyATM(ATM):
    def __init__(self):
        self.balance = 10000
        self.pin = 1234
    def check_balanance(self):
        print("Your balance is rupe ", self.balance)

    def deposite(self,amount):
        if amount <= 0:
            print("Enter valid deposite ammount")
        else:
            self.balance = self.balance + amount
            print("succesfully deposited ",amount)
            print("updated balance ripe ",self.balance)

    def withdrow(self,ammount):
        if amount <= 0:
            print("enter the valid ammount ")
        elif amount > self.balance:
            print("insufficient balance")
        else:
            self.balance = self.balance - amount
            print("collect your cash",amount)
            print("Remaining balance",self.balance)
atm = MyATM()
enter_pin = int(input("Enter the pin : .>>"))
if enter_pin == atm.pin:
    while True:
        print("\n ===== ATM MENU =====")
        print("1)check balance")
        print("2)withdrow")
        print("3)depositing amount  ")
        print("4)exit")

        choice = int(input("Enter your choice >>"))
        if choice == 1:
            atm.check_balanance()
        elif choice == 2:
            amount  = int(input("Enter the amount >>"))
            atm.withdrow(amount)
        elif choice == 3:
            amount = int(input("Enter the amount >>"))
            atm.deposite(amount)
        elif choice == 4:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")
else:
    print("wrong pin")
