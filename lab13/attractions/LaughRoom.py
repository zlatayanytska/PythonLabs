from attractions.Attraction import *


class LaughRoom(Attraction):
    def __init__(self, attraction, price, duration, age, clownsCount):
        self.attraction = attraction
        self.price = price
        self.duration = duration
        self.age = age
        self.clownsCount = clownsCount

    def __str__(self):
        return "Attraction type:" + self.attraction + " Age:" + str(self.age) + " clownsCount: " + str(self.clownsCount)
