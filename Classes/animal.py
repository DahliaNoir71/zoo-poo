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


    def __str__(self):
        """
        Returns a string representation of the Animal object.

        Returns
        -------
        str
            A string in the format "Nom : {self.nom},
            Espèce : {self.espece},
            Régime alimentaire : {self.regime_alimentaire}"
        """
        return (f"Nom : {self.nom}, "
                f"Espèce : {self.espece}, "
                f"Régime alimentaire : {self.regime_alimentaire}")



