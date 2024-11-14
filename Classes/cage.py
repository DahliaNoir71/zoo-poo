class Cage:
    animals = []

    def __init__(self, animals=None):
        self.animals = []
        if animals:
            self.add_animals(animals)

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)

    def add_animals(self, animals):
        for animal in animals:
            self.add_animal(animal)
            
    def get_animals(self):
        return self.animals