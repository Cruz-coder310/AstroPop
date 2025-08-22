import pygame
from pygame.sprite import Sprite

import resource_manager as rm


class Nave(Sprite):
    """Class to manage the player's ship in the main game."""

    def __init__(self, game):
        """initialize the attributes of the Nave class."""
        super().__init__()

        # Get game references.
        self.rect_pnt = game.rect_pnt
        self.options = game.options

        # Load the 'Nave' asset from the resources module.
        self.image = rm.resources.nave_image
        self.mask = rm.resources.nave_mask

        # Position ship at left-center of screen.
        self.rect = self.image.get_rect()
        self.set_position()

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def set_position(self):
        """Position the nave at the left-center of the screen."""
        self.rect.midleft = self.rect_pnt.midleft
        # Store position as floats for smooth movement.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update ship positon based on movement flags."""
        if (
            self.moving_right
            and self.rect.right < self.rect_pnt.centerx // 2
        ):
            self.x += self.options.nave_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.options.nave_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.options.nave_speed
        if self.moving_down and self.rect.bottom < self.rect_pnt.bottom:
            self.y += self.options.nave_speed

        # Update rect position.
        self.rect.x = self.x
        self.rect.y = self.y
