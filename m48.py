# differnt types of inheritance 1,multiple inheritance 2, single type inheritance 3, heirarcial inheritance

# imp polymorphism  : polymorphism allows object of diffrent class to be treated as
# object as common super class,but they behave diffrently depending on the object type
# poly means = many
# morm = form
# same method or  funtion name can behave diffrently depending on the object
# imp same method + differnt obeject + differnt beHAVIOR
# EXPLAINED BY THE BELOW Programs
class dog():
    def sound(self):
        print("bark")
class cat():
    def sound(self):
        print("meow")
class cow():
    def sound(self):
        print("woof")
def animal_sound(animal):
    animal.sound()
dog = dog()
cat = cat()
cow = cow()
animal_sound(dog)
animal_sound(cat)
animal_sound(cow)


# another example
class car():
    def start(self):
        print(" car start with the key")
class bike():
    def start(self):
        print(" bike start with botton")
class elecricvehical():
    def start(self):
        print(" elecric_vehical start with silent ")
vehicals  = [car(),bike(),elecricvehical()]
for vehical in vehicals:
    vehical.start()

# ER EXAMPLE FOR POLYMORPHISM

class calculater:
    def add(self,*numbers):
        return sum(numbers)
c = calculater()
print(c.add(1,2,3,4))
print(c.add(1,2,3,4,5))


class circle:
    def area(self):
        print("circle area",end = "")
class rectangle:
    def area(self):
        print("rectangle perimeter",end = "")
class square:
    def area(self):
        print("square area", end = "")
area1 = [circle(),rectangle(),square()]
for shapes  in area1:
    print(shapes .area())












