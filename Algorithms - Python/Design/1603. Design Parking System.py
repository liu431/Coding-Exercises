class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.slots = {1: big, 2:medium, 3:small }

    def addCar(self, carType: int) -> bool:
        available_slot = self.slots[carType]
        if available_slot >= 1:
            self.slots[carType] -= 1
            return True
        else:
            return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
