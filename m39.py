# oops ( object orienetd program )
# object ofuntions rineted p is prgram that approch the were we organize the prgarm using class and object
# object may consist data and funtions > data means attiributes and funtion means methods
class Car:
    def start(self):
        print("car started")
    def stop(self):
        print("car stopped")
car1 = Car()
car1.start()
car1.stop()


# what is class
# class means class is  bluprint or template for creating objects

class student:
    name = "mahesh"
    age = 20
student1 = student()
print(student1.name)
print(student1.age)

# object : object is an instant of class. or an object is an instance of the class an dthat has have own sate and behaviour

# student is class ans student  is object



# what tis construter means that automatically calls funtion itself  when an object is created  commnly used _init_()
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("mahesh", 20)
print(student1.name)
print(student1.age)









