# super() funtion is most imp for interview because most time its  asked lot of rime
class person():
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,collage):
        super().__init__(name)
        self.collage  = collage
class developer(person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary

s = student("mahesh","abc collage")
s1 = developer("rahul",20)
print(s1.name)
print(s1.salary)
print(s.name)
print(s.collage)



# inheritance
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def dispaly(self):
        print(self.name)
        print(self.salary)
class developer(employee):
    def code(self):
        print("developer writes the  pyhton codes")
class manager(employee):
    def manage(self):
        print("manager maintains them ")
dev = developer("mahesh",50000)
mana = manager("rahul",5000)
dev.dispaly()
dev.code()
mana.manage()


# litrally super() is built in funtion used to inheritance to access the methods and constructers of the parent class

