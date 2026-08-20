
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