# enscapslation another example
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def check_password(self, password):
        return password == self.password
user1 = User("mahesh", "12346")
