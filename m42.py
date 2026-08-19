class mobile:
    def __init__(self):
        self.battery = 100
    def use_phone(self,amount):
        if amount <= self.battery:
            self.battery = self.battery - amount
        else:
            print("low baatery")
    def show_battery(self):
        print("battery",self.battery)
phone = mobile()
phone.use_phone(80)
print(phone.show_battery())
