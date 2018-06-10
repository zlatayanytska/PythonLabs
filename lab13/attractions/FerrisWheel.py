from attractions.Attraction import *


class FerrisWheel(Attraction):
    def __init__(self, attraction, price, duration, age, height):
        self.attraction = attraction
        self.price = price
        self.duration = duration
        self.age = age
        self.height = height

    def __str__(self):
        return "Attraction type: " + self.attraction + "  Age: " + str(self.age) + " height: " + str(self.height)
