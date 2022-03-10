class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big, self.medium, self.small = big, medium,small


    def addCar(self, carType: int) -> bool:
        if 1 == carType:
            if self.big != 0:
                self.big -=1
                return True
            else:
                return False
        elif 2 == carType:
            if self.medium != 0:
                self.medium -=1
                return True
            else:
                return False
        elif 3 == carType:
             if self.small != 0:
                self.small -=1
                return True
             else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# parprintam_1 = obj.addCar(carType)