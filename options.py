class Options:
    """Game configuration settings."""

    def __init__(self, game):
        """Initialize game settings & speeds."""
        self.rect_pnt = game.rect_pnt
        # Nave
        self.ancho_nave = self.rect_pnt.width * 0.08
        self.alto_nave = self.rect_pnt.height * 0.15
        # Bullet
        self.bala_width = self.ancho_nave * 0.75
        self.bala_height = self.alto_nave * 0.50

        # Number of balas visible on the screen.
        self.balas = 10

        # Enemyship.
        self.enemy_width = self.rect_pnt.width * 0.06
        self.enemy_height = self.rect_pnt.height * 0.11
        self.margen_enemigo = self.enemy_height * 0.5

        # Armada
        self.armada_left_speed = 10.5
        self.armada_direction = 1

        self.vidas = 2
        self.speed_boost = 1.1
        self.increase_value = 1.5

    def set_default_speeds(self):
        """
        Sets the initial speeds for the nave, enemigos & balas, as well as
        the base value for each anemy.
        """
        self.nave_speed = 2.5
        self.bala_speed = 10.5
        self.enemy_speed = 2.0
        self.enemy_value = 50

    def increase_speeds(self):
        """
        Increases the speed of nave, enemigos & balas as well as the enemy
        value, to raise overall game difficulty & reward.
        """
        self.nave_speed *= self.speed_boost
        self.bala_speed *= self.speed_boost
        self.enemy_speed *= self.speed_boost
        self.enemy_value *= self.increase_value
