class GameStats:
    """Track & manage statistical data related to the game session."""

    def __init__(self, game):
        """
        Initialize game statistics using settings from the provided game
        instance.
        """
        self.options = game.options
        self.record = 0
        self.initial_values()

    def initial_values(self):
        """Initialize core gameplay statistics from configuration settings."""
        self.vidas = self.options.vidas
        self.score = 0
        self.level = 1
