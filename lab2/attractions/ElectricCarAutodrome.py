from attractions.Attraction import *


class ElectricCarAutodrome(Attraction):
    def __init__(self, attraction, price, duration, age, number):
        self.attraction = attraction
        self.price = price
        self.duration = duration
        self.age = age
        self.number = number

    def __str__(self):
        return "Attraction type: " + self.attraction + "  Age: " + str(self.age) + " Number: " + str(self.number)
