class Animal:
    """
    A class representing an animal.

    Attributes
    ----------
    nom : str
        The name of the animal.
    espece : str
        The species of the animal.
    regime_alimentaire : str
        The dietary habits of the animal.

    Methods
    -------
    __init__(name: str, species: str)
        Initializes an Animal object with the given name and species.
    __str__() -> str
        Returns a string representation of the Animal object.
    """

    nom = ''
    espece = ''
    regime_alimentaire = ''

    def __init__(self, name, species):
        """
        Initializes an Animal object with the given name and species.

        Parameters
        ----------
        name : str
            The name of the animal.
        species : str
            The species of the animal.

        Returns
        -------
        None
        """
        self.nom = name
        self.espece = species
        self.proies = []
        self.regime_alimentaire = ""

    def __str__(self):
        """
        Returns a string representation of the Animal object.

        Returns
        -------
        str
            A string in the format "Nom : {self.nom}, Espèce : {self.espece}, Régime alimentaire : {self.regime_alimentaire}"
        """
        return f"Nom : {self.nom}, Espèce : {self.espece}, Régime alimentaire : {self.regime_alimentaire}"


class Lion(Animal):
    """
    A class representing a Lion, a subclass of Animal.

    Attributes
    ----------
    espece : str
        The species of the Lion, which is "Lion".
    regime_alimentaire : str
        The dietary habits of the Lion, which is "Carnivore".

    Methods
    -------
    __init__(name: str)
        Initializes a Lion object with the given name and species.

    Parameters
    ----------
    name : str
        The name of the Lion.

    Returns
    -------
    None
    """

    espece = "Lion"
    regime_alimentaire = "Carnivore"

    def __init__(self, name):
        """
        Initializes a Lion object with the given name and species.

        Parameters
        ----------
        name : str
            The name of the Lion.

        Returns
        -------
        None
        """
        super().__init__(name, self.espece)


class Gazelle(Animal):
    """
    A class representing a Gazelle, a subclass of Animal.

    Attributes
    ----------
    espece : str
        The species of the Gazelle, which is "Gazelle".
    regime_alimentaire : str
        The dietary habits of the Gazelle, which is "Herbivore".

    Methods
    -------
    __init__(name: str)
        Initializes a Gazelle object with the given name and species.
    """

    espece = "Gazelle"
    regime_alimentaire = "Herbivore"

    def __init__(self, name):
        """
        Initializes a Gazelle object with the given name and species.

        Parameters
        ----------
        name : str
            The name of the Gazelle.

        Returns
        -------
        None
        """
        super().__init__(name, self.espece)
