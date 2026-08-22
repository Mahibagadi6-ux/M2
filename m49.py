# getter , setter , method overloding and over hiding
# first one  getter and setter
# defination : these are method they controlled access to an objects attributes
# they help  in  validating  data and protecting data and provide controlled  access
class student:
    def __init__(self,firstname):
        self.firstname=firstname
    def get_firstname(self):
        return self.firstname
    def set_firstname(self,firstname):
        self.firstname=firstname
S = student("mahesh,22")
print(S.get_firstname())
S.set_firstname("vishwa") # immp concept in this getter and setter means getter heplls to give the value and setter change the values
print(S.firstname)

# method overloding is the ability to define multiple methods with the same  but differnr parameters
# note : in python languge is not allows the direct overloding
class calculater:
    def add (self,a,b):
        print(a+b)
    def add(self,a,b,c = 0):
        print(a+b+c)
c = calculater()
c.add(1,2)
c.add(1,2,3)

# method overriding = parent class provide the information to its child class
class animal:
    def make_sound(self):
        print("animal is making sound")
class dog(animal):
    def make_sound(self):
        print("bark")
a = dog()
a.make_sound()


# super() funtion : is used in child class to call a method from  from the parent class
# in super () funtion it class both parent class print and child class print means it prints both attributes
class animal:
    def make_sound(self):
        print("animal is making sound")
class dog(animal):
    def make_sound(self,name,age):
        super().make_sound()
        self.name = name
        self.age = age
        print("bark")
a = dog()
a.make_sound("mahesh",66)
print(a.age,a.name)





