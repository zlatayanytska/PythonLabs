from attractions.Catapult import *
from attractions.ChildrenTrain import *
from attractions.ElectricCarAutodrome import *
from attractions.FerrisWheel import *
from attractions.Labyrinth import *
from attractions.LaughRoom import *
from Manager import *

if __name__ == '__main__':
    manager = Manager()

    catapult = Catapult("Catapult", 18, 9, 8, 10.0)
    children_train = ChildrenTrain("ChildrenTrain", 5, 8, 78, "Anna")
    electric_car_autodrome = ElectricCarAutodrome("ElectricCarAutodrome", 5, 7, 8,  12)
    ferris_wheel = FerrisWheel("FerrisWheel", 4, 8, 9, 100)
    labyrinth = Labyrinth("Labyrinth", 8, 78, 7, 50)
    laugh_room = LaughRoom("LaughRoom", 4, 89, 78, 10)

    manager.attractions = [catapult, children_train, electric_car_autodrome, ferris_wheel, labyrinth, laugh_room]
    print("Initial list:")
    manager.print_list()

    manager.sort_by_price()
    print("Sorted list")
    manager.print_list()

    manager.attractions = manager.find_by_age(18)
    print("Found list:")
    manager.print_list()

    pass
