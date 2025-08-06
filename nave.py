import pygame
from pygame.sprite import Sprite


class Nave(Sprite):
    """Class to manage the player's ship in the main game."""

    def __init__(self, game):
        """Initialize ship attributes & load image."""
        super().__init__()

        # Get game references.
        self.pantalla = game.pantalla
        self.pantalla_rect = self.pantalla.get_rect()
        self.options = game.options

        # Load and scale ship image.
        self.ship = pygame.image.load("./images/UFO.png")
        self.ship_scale = pygame.transform.scale(self.ship, (100, 100))
        self.image = self.ship_scale.convert_alpha()

        # Position ship at left center of screen.
        self.rect = self.image.get_rect()
        self.rect.midleft = self.pantalla_rect.midleft

        # Store position as floats for smooth movement.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.maving_up = False
        self.moving_down = False

    def update(self):
        """Update ship positon based on movement flags."""
        if self.moving_right and self.rect.right < self.pantalla_rect.centerx // 2:
            self.x += self.options.nave_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.options.nave_speed
        if self.maving_up and self.rect.top > 0:
            self.y -= self.options.nave_speed
        if self.moving_down and self.rect.bottom < self.pantalla_rect.bottom:
            self.y += self.options.nave_speed

        # Update rect position.
        self.rect.x = self.x
        self.rect.y = self.y
