class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def login(self):
        print(f"{self.username} logged in")
class admin(User):
    def delate_user(self):
        print(f"{self.username} deleted")
abd = admin("abd","234567")
abd.login()
abd.delate_user()


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

