class Animal:
    nom = ''
    espece = ''
    proies = []  # List of animals this animal preys on.


    def __init__(self, name, species):
        self.nom = name
        self.espece = species
        self.proies = []


class Lion(Animal):
    espece = "Lion"
    proies = ["Gazelle"]  # Lions are known to prey on elephants and wildebeests.


    def __init__(self, name):
        super().__init__(name, self.species)


class Gazelle(Animal):
    espece = "Gazelle"

    def __init__(self, name):
        super().__init__(name, self.species)
