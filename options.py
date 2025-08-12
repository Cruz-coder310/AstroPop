class Options:
    """Game configuration settings."""

    def __init__(self):
        """Initialize game settings & speeds."""
        # Nave
        self.nave_speed = 6.5
        self.ancho_nave = 100
        self.alto_nave = 100

        # Bullet
        self.bala_width = 80
        self.bala_height = 55
        self.bala_speed = 5.5

        # Number of balas visible on the screen.
        self.balas = 10
        # Enemyship.
        self.margen_enemigo = 30
        self.enemy_width = 80
        self.enemy_height = 80
        self.enemy_speed = 1.5

        # Armada
        self.armada_left_speed = 1.5
        self.armada_direction = 1
