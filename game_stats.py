class GameStats:
    """"""

    def __init__(self, game):
        """initialize"""
        self.options = game.options
        self.record = 0
        self.initial_values()

    def initial_values(self):
        """"""
        self.vidas = self.options.vidas
        self.score = 0
        self.level = 1
