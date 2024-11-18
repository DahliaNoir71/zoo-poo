from Classes.animal import Animal


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