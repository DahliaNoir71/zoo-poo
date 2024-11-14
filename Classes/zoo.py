from Classes.cage import Cage


class Zoo:
    cages = []

    def __init__(self):
        self.cages = []

    def get_nb_cages(self):
        return len(self.cages)
    
    def add_cage(self, cage):
        self.cages.append(cage)

    def add_cages(self, cages):
        self.cages.extend(cages)

    def add_nb_cages(self, nb_cages):
        for _ in range(nb_cages):
            self.add_cage(Cage())