# aggregation concept , which discribes the how to connect the differnt clas
class person:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    def print_info(self):
        print(f"name: {self.name}, gender: {self.gender}, address: {self.address.city},{self.address.state},{self.address.taluk}")
class address:
    def __init__(self,city,state,taluk):
        self.city = city
        self.state = state
        self.taluk = taluk
adds = address("yadagir","karnataka","shorapur")
per = person("mahesh","male",adds)
per.print_info()

