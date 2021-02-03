class City:
    def __init__(self, name, population):
        self.population = population
        self.name = name

    def __gt__(self, other):
        return self.population > other.population
