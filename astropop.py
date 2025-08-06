import pygame
import sys
from nave import Nave
from options import Options
from balas import Bala


class AstroPop:
    """Main game class that controls AstroPop."""

    def __init__(self):
        """Initialize game attributes and pygame settings."""
        pygame.init()
        self.pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("AstroPop")
        self.options = Options()
        self.reloj = pygame.time.Clock()

        # Initialize sprite groups and player nave.
        self.naves = pygame.sprite.Group()
        self.nave = Nave(self)
        self.naves.add(self.nave)
        self.balas = pygame.sprite.Group()

    def run_game(self):
        """Main game loop running at 60 FPS."""
        while True:
            self._process_events()
            self.nave.update()
            self.balas.update()
            self._render_screen()
            self.reloj.tick(60)

    def _process_events(self):
        """Handle keyboard and system events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)

    def _handle_keydown(self, event):
        """Process key press events for movement and actions."""
        if event.key == pygame.K_RIGHT:
            self.nave.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.nave.moving_left = True
        elif event.key == pygame.K_UP:
            self.nave.maving_up = True
        elif event.key == pygame.K_DOWN:
            self.nave.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _handle_keyup(self, event):
        """Process key release events to stop movement."""
        if event.key == pygame.K_RIGHT:
            self.nave.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.nave.moving_left = False
        elif event.key == pygame.K_UP:
            self.nave.maving_up = False
        elif event.key == pygame.K_DOWN:
            self.nave.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bala = Bala(self)
        self.balas.add(new_bala)

    def _render_screen(self):
        """Draw all game elements on pantalla."""
        self.pantalla.fill("black")
        self.balas.draw(self.pantalla)
        self.naves.draw(self.pantalla)
        pygame.display.flip()


# Game execution.
if __name__ == "__main__":
    game = AstroPop()
    game.run_game()
