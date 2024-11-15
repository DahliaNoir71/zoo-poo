class Cage:
    animals = []
    animal_espece = ''

    def __init__(self, animals=None):
        self.animals = []
        animal_espece = ''
        if animals:
            self.add_animals(animals)

    def add_animal(self, animal):
        if not len(self.animals):
            self.animal_espece = animal.espece  # Set the espece of the cage to the first animal added.  # TODO: Consider handling case where multiple animals have the same species.  # TODO: Consider handling case where the cage already contains animals of the same species.  # TODO: Consider handling case where the cage already contains animals of different species.  # TODO: Consider handling case where the animal list contains None values.  # TODO: Consider handling case where the animal list contains non-animal objects.  # TODO: Consider handling case where the animal list contains animals of different species.  # TODO: Consider handling case where the animal list contains animals of the same species.  # TODO: Consider handling case where the animal list contains animals of the same species.  # TODO: Consider handling case where the animal list contains animals of the same species.  # TODO: Consider handling
        if animal not in self.animals and animal.espece == self.animal_espece :
            self.animals.append(animal)

    def add_animals(self, animals):
        for animal in animals:
            self.add_animal(animal)
            
    def get_animals(self):
        return self.animals