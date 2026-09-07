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
# aggregation concept , which discribes the how to connect the differnt clas
# check the in the aggregation method cannot allow the private attiribute for example below ,
"""class person:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    def print_info(self):
        print(f"name: {self.name}, gender: {self.gender}, address: {self.address.city},{self.address.state},{self.address.taluk}")
class address:
    def __init__(self,city,state,taluk):
        self.__city = city
        self.state = state
        self.taluk = taluk
    def get_city(self):
        return self.__city
adds = address("yadagir","karnataka","shorapur")
per = person("mahesh","male",adds)
per.print_info()
# occures Error
# aggregation concept , which discribes the how to connect the differnt clas"""
class person:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    def print_info(self):
        print(f"name: {self.name}, gender: {self.gender}, address: {self.address.get_city()},{self.address.state},{self.address.taluk}")
class address:
    def __init__(self,city,state,taluk):
        self.__city = city
        self.state = state
        self.taluk = taluk
    def get_city(self):
        return self.__city

adds = address("yadagir","karnataka","shorapur")
per = person("mahesh","male",adds)
per.print_info()


# aggregation concept , which discribes the how to connect the differnt clas
class person:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    def print_info(self):
        print(f"name: {self.name}, gender: {self.gender}, address: {self.address._address__city},{self.address.state},{self.address.taluk}")
class address:
    def __init__(self,city,state,taluk):
        self.__city = city
        self.state = state
        self.taluk = taluk

adds = address("yadagir","karnataka","shorapur")
per = person("mahesh","male",adds)
per.print_info()
 # but above program is not good approach
 # try the middle one
 # in nover days the agreeratuon is not working insted of this using inheritance



