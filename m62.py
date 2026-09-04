from abc import ABC, abstractmethod


class Vehicle(ABC):

  def __init__(self, brand: str, model: str):
    self._brand = brand
    self._model = model

  @property
  def brand(self) -> str:
    return self._brand

  @property
  def model(self) -> str:
    return self._model

  @abstractmethod
  def start_engine(self) -> str:
    pass

  def stop_engine(self) -> str:
    return f"{self._brand} {self._model} engine stopped."


class Car(Vehicle):

  def __init__(self, brand: str, model: str, doors: int):
    super().__init__(brand, model)
    self.doors = doors

  def start_engine(self) -> str:
    return f"{self.brand} {self.model} with {self.doors} doors started."


class Motorcycle(Vehicle):

  def __init__(self, brand: str, model: str, has_carrier: bool):
    super().__init__(brand, model)
    self.has_carrier = has_carrier

  def start_engine(self) -> str:
    return f"{self.brand} {self.model} motorcycle started."


if __name__ == "__main__":
  my_car = Car("Toyota", "Camry", 4)
  my_bike = Motorcycle("Yamaha", "R15", False)

  vehicles = [my_car, my_bike]

  for v in vehicles:
    print(v.start_engine())
    print(v.stop_engine())
