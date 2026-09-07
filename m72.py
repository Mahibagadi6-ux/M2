class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the parent class's __init__ method
        self.breed = breed

    def sound(self):
        super().sound()  # Calling the parent class's sound method
        print(f"{self.name} barks")

# Usage
dog = Dog("Buddy", "Labrador")
dog.sound()