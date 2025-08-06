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
        self.ship_scale = pygame.transform.scale(self.ship, (100, 100))
        self.image = self.ship_scale.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.midleft = self.pantalla_rect.midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.r_flag = False
        self.l_flag = False
        self.u_flag = False
        self.d_flag = False

    def update(self):
        """movement of the ship depends of the flags"""
        if self.r_flag and self.rect.right < self.pantalla_rect.centerx // 2:
            self.x += self.options.nave_speed
        if self.l_flag and self.rect.left > 0:
            self.x -= self.options.nave_speed
        if self.u_flag and self.rect.top > 0:
            self.y -= self.options.nave_speed
        if self.d_flag and self.rect.bottom < self.pantalla_rect.bottom:
            self.y += self.options.nave_speed

        self.rect.x = self.x
        self.rect.y = self.y
