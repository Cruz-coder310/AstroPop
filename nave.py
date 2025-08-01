import pygame


class Nave:
    """CLass to manage the nave."""

    def __init__(self, rocket):
        """INitialize the atrribiutes of the class"""
        self.pantalla = rocket.pantalla
        self.pantalla_rect = self.pantalla.get_rect()

        self.ship = pygame.image.load("./images/UFO.png")
        self.ship_small = pygame.transform.scale(self.ship, (100, 100))
        self.ship_rect = self.ship_small.get_rect()
        self.ship_rect.center = self.pantalla_rect.center

        self.r_flag = False
        self.l_flag = False
        self.u_flag = False
        self.d_flag = False

    def movement(self):
        """movement of the ship depends of the flags"""

        if self.r_flag and self.ship_rect.right < self.pantalla_rect.right:
            self.ship_rect.x += 4
        if self.l_flag and self.ship_rect.left > 0:
            self.ship_rect.x -= 4
        if self.u_flag and self.ship_rect.top > 0:
            self.ship_rect.y -= 4
        if self.d_flag and self.ship_rect.bottom < self.pantalla_rect.bottom:
            self.ship_rect.y += 4

    def materialize(self):
        """draw the ship in the screen"""
        self.pantalla.blit(self.ship_small, self.ship_rect)
