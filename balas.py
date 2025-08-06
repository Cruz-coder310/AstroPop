import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    """Manage the bullets of the game."""

    def __init__(self, astropop):
        """initialize atribbutes of the class"""
        super().__init__()

        self.pantalla = astropop.pantalla
        self.nave = astropop.nave

        self.image = pygame.image.load("./images/proto.png")
        self.rect = self.image.get_rect()

        self.rect.midtop = self.nave.rect.midtop

        self.x = float(self.rect.x)

        # self.s_flag = False

    def update(self):
        """Mmovement of the bullet realted to the ship"""
        # if self.s_flag:
        self.x += 2
        self.rect.x = self.x
