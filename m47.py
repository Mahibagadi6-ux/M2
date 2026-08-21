
class parent:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class student(parent):
    def __init__(self, name, salary,collage_name,age):
        super().__init__(name, salary)
        self.collage_name = collage_name
        self.age = age
s = student("mahes",11000,12,23)
print(s.name,s.salary,s.collage_name,s.age)


class car():
    def __init__(self, name):
        self.name = name
class muruti(car):
    def __init__(self, name, model,year,rental,new_model):
        super(). __init__(name)
        self.model = model
        self.year = year
        self.rental = rental
        self.new_model = new_model

s1 = muruti("maruti_suzuki",2019,2026,2000,"yes")
print(s1.name,s1.rental,s1.new_model,s1.model,s1.year)


