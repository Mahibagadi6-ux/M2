

class bank_account:
    def __init__(self,balance ):
        self.balance = balance
    def get_balance(self):
        return self.balance
    def set_balance(self,updated_balance):
        if updated_balance < 0:
            print("balance cannot be negative")
        else:
            self.balance = updated_balance

b = bank_account(1000)
print(b.get_balance())
b.set_balance(100)
print(b.get_balance())


class calculater:
    def mult1(self,a,b):
        print(a*b)
    def mult(self,a,b,c = 0):
        print(a*b*c)
c = calculater()
c.mult1(100,200)
c.mult(10,20,30)

class shape:
    def drow(self):
        print("drow")
class circle(shape):
    def drow(self):
        print("drowing circle")
c = circle()
c.drow()
 # when we want to print both parent class input and also child class can print useing super() funtion :
class shape:
    def drow(self):
        print("drow")
class circle(shape):
    def drow(self):
        super().drow()
        print("drowing circle")
c = circle()
c.drow()


from abc import ABC,abstractmethod
class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class manager(employee):
    @abstractmethod
    def calculate_salary(self):
        print("manager salary is calculated ")







