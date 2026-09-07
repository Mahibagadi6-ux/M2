
class family:
    def __init__(self,surname):
        self.surname = surname
class child(family):
    def __init__(self,surname,name):
        super().__init__(surname)
        self.name = name
fam = family("bagadi")
child = child("badadi","mahesh")
print(f"{child.surname},{child.name}")


class aakla:
    def __init__(self,name,ate):
        self.name = name
        self.ate = ate
    def aakla(self):
        print(f"{self.name},{self.ate}")
class kara(aakla):
    def kara(self):
        print(f"{self.name},{self.ate}")
class sann_kara(aakla):
    def sann_kara(self):
        print(f"{self.name},{self.ate}")
kara = kara("gowri","mevu")
sanna = sann_kara("laxmi","ullu")

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()
d.bark()


class Person:
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender



    def show(self):
        print(self.name,self.age,self.gender)

class Student(Person):
    pass
class Teacher(Person):
    pass

s = Student("Mahi",22,"male")
s1 = Teacher("bhagya_madam",45,"female")
s.show()
s1.show()



class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def show(self):
        print(self.firstname,self.lastname)
class Student(Person):
    def welcome(self):
        print("Welcome", self.firstname, self.lastname)
class teacher(Person):
    def welcome(self):
        print("wecome",self.firstname,self.lastname)

x = Student("John", "Doe")
x.show()
x.welcome()
x1 = teacher("bhagyashree","shree")
x1.show()
x1.welcome()

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")
class Truck(Vehicle):
    def wheels(self):
        print("Truck has 4 wheels")


c = Car()
c1 = Truck()
c1.move()
c1.wheels()
c.move()
c.wheels()



class Shape:
    def area(self):
        print("This is a shape")

class Circle(Shape):
    def area(self):
        print("Area of circle")

c = Circle()
c.area()


class Parent:
    def hello(self):
        print("Hello from parent")

class Child(Parent):
    def goodbye(self):
        print("Goodbye from child")

c = Child()
c.hello()
c.goodbye()


class Employee:
    def work(self):
        print("Employee works")

class Manager(Employee):
    def manage(self):
        print("Manager manages team")

m = Manager()
m.work()
m.manage()



class Bird:
    def fly(self):
        print("Bird can fly")

class Sparrow(Bird):
    def chirp(self):
        print("Sparrow chirps")

s = Sparrow()
s.fly()
s.chirp()
