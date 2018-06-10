from attractions.Attraction import *


class ChildrenTrain(Attraction):
    def __init__(self, attraction, price, duration, age, driverName):
        self.attraction = attraction
        self.price = price
        self.duration = duration
        self.age = age
        self.driverName = driverName

    def __str__(self):
        return "Attraction type: " + self.attraction + "  Age: " + str(self.age) + " driverName: " + self.driverName
