from random import randint

class Die():
    """Uma classe que representa um unico dadp."""

    def __init__(self, num_sides=6):
        """Supõe que seja uma dado de seis lados."""
        self._num_sides = num_sides

    def roll(self):
        """Devolve um valor aleatório entre 1 e o número de lados."""
        return randint(1, self._num_sides)

    @property
    def num_sides(self):
        return self._num_sides

