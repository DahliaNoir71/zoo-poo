class Cage:
    animals = []
    animal_espece = ''

    def __init__(self, animals=None):
        """
        Initialize a new Cage instance.

        Parameters:
        - animals (list, optional): A list of animals to add to the cage. Defaults to None.

        The cage's animals list and animal_espece attribute are initialized as empty.
        If animals are provided, they are added to the cage using the add_animals method.
        """
        self.animals = []
        animal_espece = ''
        if animals:
            self.add_animals(animals)

    def add_animal(self, animal):
        """
        Add an animal to the cage.

        Parameters:
        - animal (Animal): The animal to add to the cage.

        If the cage is empty, the animal's species is set as the cage's species.
        If the animal is not already in the cage and its species matches the cage's species,
        the animal is added to the cage.
        """
        if not len(self.animals):
            self.animal_espece = animal.espece  # Set the espece of the cage to the first animal added.  # TODO: Consider handling case where multiple animals have the same species.  # TODO: Consider handling case where the cage already contains animals of the same species.  # TODO: Consider handling case where the cage already contains animals of different species.  # TODO: Consider handling case where the animal list contains None values.  # TODO: Consider handling case where the animal list contains non-animal objects.  # TODO: Consider handling case where the animal list contains animals of different species.  # TODO: Consider handling case where the animal list contains animals of the same species.  # TODO: Consider handling case where the animal list contains animals of the same species.  # TODO: Consider handling case where the animal list contains animals of the same species.  # TODO: Consider handling
        if animal not in self.animals and animal.espece == self.animal_espece :
            print(f"{animal.espece} {animal.nom} ajouté à la cage.\n")
            self.animals.append(animal)
        elif animal.espece != self.animal_espece:
            msg_alert = f"Vous ne pouvez ajouter l'espèce {animal.espece} dans une cage {self.animal_espece}.\n"
            print(msg_alert)
        elif animal in self.animals:
            msg_alert = f"{animal.nom} est déjà dans la cage.\n"
            print(msg_alert)

    def add_animals(self, animals):
        """
        Add multiple animals to the cage.

        Parameters:
        - animals (list): A list of animals to add to the cage.

        Each animal in the list is added to the cage using the add_animal method.
        """
        for animal in animals:
            self.add_animal(animal)
            
    def get_animals(self):
        """
        Return the list of animals in the cage.

        Returns:
        - list: The list of animals in the cage.
        """
        return self.animals
    
    def get_animal_espece(self):
        """
        Return the species of animals in the cage.

        Returns:
        - str: The species of animals in the cage.
        """
        return self.animal_espece
    
    def remove_animal(self, animal):
        """
        Remove an animal from the cage.

        Parameters:
        - animal (Animal): The animal to remove from the cage.

        If the animal is in the cage, it is removed from the cage.
        """
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.espece} {animal.nom} retiré de la cage.\n")

    def empty_cage(self):
        """
        Remove all animals from the cage.
        """
        self.animals = []
        print(f"La cage a été vidé.\n")
            
    def __str__(self):
        """
        Return a string representation of the cage.

        Returns:
        - str: A string representation of the cage, including the species of animals and the list of animals.
        """
        if not len(self.animals):
            return 'Cage vide.'
        else:
            str_description = f'Cage pour {self.animal_espece}\n'
            str_description += f'Nb animaux : {len(self.animals)}'
            for animal in self.animals:
                str_description += f'\n- {animal}'
            return str_description
