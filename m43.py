class Tempreture:
    def __init__(self):
        self.Tempreture = 0
    def set_Tempreture(self, Tempreture):
        if Tempreture >= -273.15:
            self.Tempreture = Tempreture
    def get_Tempreture(self):
        return self.Tempreture
t = Tempreture()
t.set_Tempreture(28)
print(t.get_Tempreture())