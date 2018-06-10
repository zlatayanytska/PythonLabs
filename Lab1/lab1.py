class Stadium:
    totalNumberOfSeats = 0

    def __init__(self, name="arena lviv", type="football", number_of_seats=1000, field_area=55.5, covering="grass"):

        self.name = name
        self.type = type
        self.number_of_seats = number_of_seats
        self.field_area = field_area
        self.covering = covering

        Stadium.totalNumberOfSeats += number_of_seats

    def to_string(self):
            print("Name: " + self.name + " Type:", self.type,
                  " Number of seats:", self.number_of_seats, " Field Area:", self.field_area, " Covering:", self.covering)

    def print_sum(self):
            print("Current number of seats", self.number_of_seats, "at the stadium " + self.name)

    @staticmethod
    def print_static_sum():
            print("Total number of seats: ", Stadium.totalNumberOfSeats)


if __name__ == '__main__':
    ukraine = Stadium("Ukraine", "football", 28051, 7140)
    arena_lviv = Stadium()
    shanghai = Stadium("Shanghai Stadium", "universal", 80000, 12000, "sand")

    print("\n")
    ukraine.to_string()
    arena_lviv.to_string()
    shanghai.to_string()

    print("\n")
    ukraine.print_sum()
    arena_lviv.print_sum()
    shanghai.print_sum()

    print("\n")
    Stadium.print_static_sum()
