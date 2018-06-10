from attractions.Attraction import *


class Catapult(Attraction):
    def __init__(self, attraction, price, duration, age, speed):
        self.attraction = attraction
        self.price = price
        self.duration = duration
        self.age = age
        self.speed = speed

    def __str__(self):
        return "Attraction type: " + self.attraction + "  Age: " + str(self.age) + " Speed: " + str(self.speed)
