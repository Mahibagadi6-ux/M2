class Animal:
    def eat(self):
        print("animal is eating ")
class dog(Animal):
        def bark(self):
            print("bark is eating ")
Dog = dog()
Dog.eat()
Dog.bark()
# child class get properties and methods of parent class
# its helps with decres the code and helps reusable less dublicates easy maintance
#usefull crating relations between class

# another example
class  father:
    def house(self):
        print("father has a  house")
class son(father):
    def bike(self):
        print("son has bike  ")
class mother(father):
    def mother(self):
        print("mother has mother  ")

s = son()
s = mother()
s.house()
s.mother()

# inehritance using consrucuter
class person():
    def __init__(self, name):
        self.name = name
    def dispaly(self):
        print("name",self.name)
class student(person):
    def study(self):
        print("student is studing  ")


s = student("mahesh")
s.dispaly()
s.study()