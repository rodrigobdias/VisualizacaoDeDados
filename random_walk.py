from random import choice

class RandomWalk():
    """Uma classe para gerar passeios aleatorios."""

    def __init__(self, num_points = 5000):
        """Inicializa os atributos de um passeio."""
        self.num_points = num_points

        # Todos os passeios começam em (0,0)
        self.x_values = [0]
        self.y_values = [0]

        