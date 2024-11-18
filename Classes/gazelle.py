from Classes.animal import Animal


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