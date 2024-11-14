class Animal:
    name = ''
    species = ''
    preys = []

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.preys = []


class Lion(Animal):
    species = "Lion"

    def __init__(self, name):
        super().__init__(name, self.species)


class Gazelle(Animal):
    species = "Gazelle"

    def __init__(self, name):
        super().__init__(name, self.species)
