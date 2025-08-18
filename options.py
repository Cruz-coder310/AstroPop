class Options:
    """Game configuration settings."""

    def __init__(self):
        """Initialize game settings & speeds."""
        # Nave
        self.ancho_nave = 100
        self.alto_nave = 100

        # Bullet
        self.bala_width = 80
        self.bala_height = 55

        # Number of balas visible on the screen.
        self.balas = 10

        # Enemyship.
        self.margen_enemigo = 30
        self.enemy_width = 80
        self.enemy_height = 80

        # Armada
        self.armada_left_speed = 10.5
        self.armada_direction = 1

        self.vidas = 0
        self.speed_boost = 1.1

    def set_default_speeds(self):
        """Sets the initial speeds for the nave, enemigos & balas."""
        self.nave_speed = 2.5
        self.bala_speed = 3.5
        self.enemy_speed = 2.0

    def increase_speeds(self):
        """
        Increases the speed of nave, enemigos & balas to raise game difficulty.
        """
        self.nave_speed *= self.speed_boost
        self.bala_speed *= self.speed_boost
        self.enemy_speed *= self.speed_boost
