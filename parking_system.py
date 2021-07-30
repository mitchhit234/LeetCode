#Implement a ParkingSystem Class

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cars = [big,medium,small]

    def addCar(self, carType: int) -> bool:
        if self.cars[carType-1] > 0:
          self.cars[carType-1] -= 1
          return True
        return False




obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))