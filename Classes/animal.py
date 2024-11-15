class Animal:
    nom = ''
    espece = ''


    def __init__(self, name, species):
        self.nom = name
        self.espece = species
        self.proies = []

    def __str__(self):
        return f"Nom : {self.nom}, Espèce : {self.espece}"


class Lion(Animal):
    espece = "Lion"

    def __init__(self, name):
        super().__init__(name, self.species)


class Gazelle(Animal):
    espece = "Gazelle"

    def __init__(self, name):
        super().__init__(name, self.species)
