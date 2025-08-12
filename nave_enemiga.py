import pygame
from pygame.sprite import Sprite


class NaveEnemiga(Sprite):
    """Class to manage the enemy ships."""

    def __init__(self, game):
        super().__init__()

        # Game references
        self.options = game.options
        self.rect_screen = game.pantalla

        # Update the NaveEnemiga and set the correct size
        self.original_image = pygame.image.load("./images/enemyship.png")
        self.scale_image = pygame.transform.scale(
            self.original_image, (self.options.enemy_width, self.options.enemy_height)
        )
        self.image = self.scale_image.convert_alpha()

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
