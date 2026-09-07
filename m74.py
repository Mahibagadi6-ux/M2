class bankaccount:
    def __init__(self,holedr_name,balance):
        self.holedr_name = holedr_name
        self.__balance = balance
    def get_balance(self):
        print(f"{self.__balance}")
    def set_balance(self,balance):
        self.__balance = balance
bnk = bankaccount("Buddy",10000)
bnk.get_balance()
bnk.set_balance(20000)
bnk.get_balance()


class calculater:
    def mult1(self,a,b):
        return a*b
    def mult(self,a,b,c=0):
        return (a*b*c)
cla = calculater()
cla.mult1(1,2)
cla.mult(3,4,5)
print(cla.mult(3,4,5))
print(cla.mult1(3,4))


class shape:
    def __init__(self,name):
        self.name = name
    def drow(self):
        print(f"{self.name} your are drowing this one ")
class circle(shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius = radius


    def drow(self):
        print(f"{self.name} is your drowing ")
shape  = circle("circle",5)
shape.drow()
