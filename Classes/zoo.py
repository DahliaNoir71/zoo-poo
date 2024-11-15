from matplotlib import pyplot as plt
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
        self.plot()
        return str_description

    def remove_cage(self, cage):
        print(f"Suppression de la cage {cage.animal_espece}")
        if cage in self.cages:
            if len(cage.animals) > 0:
                print("Cette cage n'est pas vide. Suppression annulée.\n")
            else:
                self.cages.remove(cage)
                print(f"Cage {cage.animal_espece} vide retirée du zoo.\n")

    def get_empty_cages(self):
        empty_cages =  [cage for cage in self.cages if len(cage.animals) == 0]
        return empty_cages

    def print_empty_cages_descrption(self):
        empty_cages = self.get_empty_cages()
        if len(empty_cages) == 0:
            print("Aucune cage vide dans le zoo.\n")
        else:
            print(f"Cages vides dans le zoo:\n")
            for cage in empty_cages:
                print(f"- {cage}\n")

    def remove_empty_cages(self):
        empty_cages = self.get_empty_cages()
        for cage in empty_cages:
            self.remove_cage(cage)

    def plot(self):
        """
        Create a bar chart showing the number of animals in each cage.

        Parameters:
        None

        Returns:
        None
        """
        # Get the number of animals in each cage
        animal_counts = [len(cage.animals) for cage in self.cages]

        # Create a bar chart
        plt.bar(range(len(self.cages)), animal_counts)

        # Set the labels and title
        plt.xticks(range(len(self.cages)), [cage.animal_espece for cage in self.cages], rotation=45)
        plt.xlabel("Cage")
        plt.ylabel("Nombre d'animaux")
        plt.title(f"Nombre d'animaux par cage dans le zoo {self.nom}")

        # Display the plot
        plt.show()



        