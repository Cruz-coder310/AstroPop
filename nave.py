import pygame
from pygame.sprite import Sprite


class Nave(Sprite):
    """CLass to manage the nave."""

    def __init__(self, astropop):
        """INitialize the atrribiutes of the class"""
        super().__init__()
        self.pantalla = astropop.pantalla
        self.pantalla_rect = self.pantalla.get_rect()
        self.options = astropop.options

        self.ship = pygame.image.load("./images/UFO.png")
        self.image = pygame.transform.scale(self.ship, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = self.pantalla_rect.center

        self.r_flag = False
        self.l_flag = False
        self.u_flag = False
        self.d_flag = False

    def update(self):
        """movement of the ship depends of the flags"""
        if self.r_flag and self.rect.right < self.pantalla_rect.right:
            self.rect.x += self.options.speed
        if self.l_flag and self.rect.left > 0:
            self.rect.x -= self.options.speed
        if self.u_flag and self.rect.top > 0:
            self.rect.y -= self.options.speed
        if self.d_flag and self.rect.bottom < self.pantalla_rect.bottom:
            self.rect.y += self.options.speed
