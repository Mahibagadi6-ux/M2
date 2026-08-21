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

# ANOTHER EXAMPLE FOR POLYMORPHISM








