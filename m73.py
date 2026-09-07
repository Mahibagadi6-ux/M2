class vehicle:
    def __init__(self, name):
        self.name = name
    def start(self):
        print(f"vehicle {self.name} is start with the sound broooom ")
class car(vehicle):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model
    def start(self):
        super().start()
        print(f"{self.name} is starting the car")
vehiccle = car("lamberginni",2017)
vehiccle.start()

