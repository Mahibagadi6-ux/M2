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

