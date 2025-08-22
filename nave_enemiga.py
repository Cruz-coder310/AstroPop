import pygame
from pygame.sprite import Sprite

import resource_manager as rm


class NaveEnemiga(Sprite):
    """Class to manage the enemy ships."""

    def __init__(self, game):
        """initialize the attributes of the NaveEnemiga class."""
        super().__init__()

        # Game references
        self.options = game.options
        self.rect_screen = game.pantalla

        # Load the 'NaveEnemiga' asset from the resources module.
        self.image = rm.resources.enemigo_image
        self.mask = rm.resources.enemigo_mask

        # position of the enemyship
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def vertical_edges(self):
        """Detect vertical edge contact and return a boolean result."""
        rect_pnt = self.rect_screen.get_rect()
        return (self.rect.bottom >= rect_pnt.bottom) or (self.rect.top <= 0)

    def update(self):
        """Handle individual enemy ship motion across the screen."""
        self.y += self.options.enemy_speed * self.options.armada_direction
        self.rect.x = self.x
        self.rect.y = self.y
