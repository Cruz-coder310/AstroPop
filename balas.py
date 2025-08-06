import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    """Manage the bullets of the game."""

    def __init__(self, astropop):
        """initialize atribbutes of the class"""
        super().__init__()

        self.pantalla = astropop.pantalla
        self.options = astropop.options
        self.nave = astropop.nave

        self.image_1 = pygame.image.load("./images/proto.png")
        self.image_scale = pygame.transform.scale(
            self.image_1, (self.options.bala_widht, self.options.bala_height)
        )
        self.image = self.image_scale.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.midright = self.nave.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Mmovement of the bullet realted to the ship"""
        self.x += self.options.bala_speed
        self.rect.x = self.x
