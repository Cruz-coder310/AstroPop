import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    """A class to manage bullets in the main game."""

    def __init__(self, game):
        """Initialize bullet attributes & position."""
        super().__init__()

        # Game references.
        self.options = game.options
        self.nave = game.nave

        # Load & scale bullet image.
        self.image_1 = pygame.image.load("./images/proto.png")
        self.image_scale = pygame.transform.scale(
            self.image_1, (self.options.bala_widht, self.options.bala_height)
        )
        self.image = self.image_scale.convert_alpha()

        # Position bullet at ship's right side.
        self.rect = self.image.get_rect()
        self.rect.midright = self.nave.rect.midright

        # Store the position as a float for smooth movement.
        self.x = float(self.rect.x)

    def update(self):
        """Move bullet horizontally based on bullet speed."""
        self.x += self.options.bala_speed
        self.rect.x = self.x
