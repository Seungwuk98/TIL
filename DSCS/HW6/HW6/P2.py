from P1 import Country  # Do Not Modify


class Continent:
    def __init__(self, name, countries):
        # write your code below
        self.name = name
        self.countries = countries

    def total_population(self):
        # write your code below
        return sum([country.population for country in self.countries])
