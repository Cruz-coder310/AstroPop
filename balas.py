import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    """Manage the bullets of the game."""

    def __init__(self, astropop):
        """initialize atribbutes of the class"""
        super().__init__()
        self.pantalla = astropop.pantalla
        self.nave = astropop.nave
        self.medidas_nave = self.nave.ship_rect

        self.casco = pygame.image.load("./images/proto.png")
        self.rect = self.casco.get_rect()
        self.rect.midbottom = self.medidas_nave.midtop

    def materialize(self):
        """draw the vala in the screan"""
        self.pantalla.blit(self.casco, self.rect)
