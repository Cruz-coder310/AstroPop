import pygame
from pygame.sprite import Sprite

import resource_manager as rm


class Bala(Sprite):
    """A class to manage bullets in the main game."""

    def __init__(self, game):
        """initialize the attributes of the Bala class."""
        super().__init__()

        # Game references.
        self.options = game.options
        self.nave = game.nave

        # Load the 'Bala' asset from the resources module.
        self.image = rm.resources.bala_img

        # Position bullet at ship's right side.
        self.rect = self.image.get_rect()
        self.rect.midright = self.nave.rect.midright

        # Store the position as a float for smooth movement.
        self.x = float(self.rect.x)

    def update(self):
        """Move bullet horizontally based on bullet speed."""
        self.x += self.options.bala_speed
        self.rect.x = self.x
