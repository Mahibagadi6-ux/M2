class database:
    def __init__(self):
        self.__storage = {}
    def write(self,key,value):
        self.__storage[key] = value
    def read(self,key):
        if key in self.__storage:
            print(self.__storage[key])
        else:
            print("invalid key")
db = database()
db.write("mahesh","10LPA")
db.read("mahesh")

