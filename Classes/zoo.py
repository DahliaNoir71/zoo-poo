from Classes.cage import Cage


class Zoo:
    nom = ''
    cages = []

    def __init__(self, nom):
        """
        Initialize a new Zoo instance.

        Parameters:
        nom (str): The name of the zoo.

        Returns:
        None
        """
        self.nom = nom
        self.cages = []

    def get_nb_cages(self):
        """
        Get the number of cages in the zoo.

        Parameters:
        None

        Returns:
        int: The number of cages in the zoo.
        """
        return len(self.cages)
    
    def add_cage(self, cage):
        """
        Add a single cage to the zoo.

        Parameters:
        cage (Cage): The cage to be added.

        Returns:
        None
        """
        self.cages.append(cage)

    def add_cages(self, cages):
        """
        Add multiple cages to the zoo.

        Parameters:
        cages (list): A list of cages to be added.

        Returns:
        None
        """
        self.cages.extend(cages)

    def add_nb_cages(self, nb_cages):
        """
        Add a specified number of cages to the zoo.

        Parameters:
        nb_cages (int): The number of cages to be added.

        Returns:
        None
        """
        for _ in range(nb_cages):
            self.add_cage(Cage())
            
    def __str__(self):
        """
        Return a string representation of the zoo.

        Parameters:
        None

        Returns:
        str: A string representation of the zoo.
        """
        str_description = f"Zoo:  {self.nom}\n"
        str_description += f"{len(self.cages)} cages\n"
        for cage in self.cages:
            str_description += f"- {cage}\n"
        return str_description
        