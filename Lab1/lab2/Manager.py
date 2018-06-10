class Manager:
    attractions = []

    def __init__(self):
        pass

    def sort_by_price(self):
        self.attractions.sort(key=lambda attraction: attraction.price)

    def find_by_age(self, age):
        found_attractions = []

        for attraction in self.attractions:
            if attraction.age > age:
                found_attractions.append(attraction)

        return found_attractions

    def add_attraction(self, attraction):
        self.attractions += attraction

    def print_list(self):
        for attraction in self.attractions:
            print(attraction)
        print("\n")





dictionary = {(1, 2, 3) : 1, 2: (1, 2, 3)}