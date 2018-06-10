from attractions.Attraction import *


class Labyrinth(Attraction):
    def __init__(self, attraction, price, duration, age, length):
        self.attraction = attraction
        self.price = price
        self.duration = duration
        self.age = age
        self.length = length

    def __str__(self):
        return "Attraction type: " + self.attraction + "  Age: " + str(self.age) + " length: " + str(self.length)
