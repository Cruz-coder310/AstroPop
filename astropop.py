import pygame
import sys
from nave import Nave
from options import Options
import resource_manager
from balas import Bala
from nave_enemiga import NaveEnemiga


class AstroPop:
    """Main game class that controls AstroPop."""

    def __init__(self):
        """Initialize game attributes and Pygame settings."""
        pygame.init()
        self.options = Options()
        self.reloj = pygame.time.Clock()

        self.pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.rect_pnt = self.pantalla.get_rect()
        pygame.display.set_caption("AstroPop")

        # Asset management
        resource_manager.init_manager(self.options)

        # Initialize sprite groups
        # Player nave.
        self.naves = pygame.sprite.Group()
        self.nave = Nave(self)
        self.naves.add(self.nave)
        # Balas.
        self.balas = pygame.sprite.Group()
        # Enemyships.
        self.enemigos = pygame.sprite.Group()
        self._create_armada()

    def run_game(self):
        """Main game loop running at 60 FPS."""
        while True:
            self._process_events()
            self.naves.update()
            self._update_balas()
            self._update_armada()
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
            self.nave.moving_up = True
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
            self.nave.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.nave.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.balas) < self.options.balas:
            new_bala = Bala(self)
            self.balas.add(new_bala)

    def _update_balas(self):
        """
        Update the position of the balas on the screen & remove those that have
        moved off-screen.
        """
        self.balas.update()
        for bala in self.balas:
            if bala.rect.left >= self.rect_pnt.right:
                bala.kill()
        # This print lets me see if the bala was deleted after moving off-screen.
        # print(len(self.balas))
        self._check_collide_bullet_enemy()

    def _check_collide_bullet_enemy(self):
        """removes any balas & enemigos that have collided."""
        collision = pygame.sprite.groupcollide(
            self.balas, self.enemigos, True, True, collided=self._hitbox_collision
        )
        if not self.enemigos:
            self.balas.empty()
            self._create_armada()

    def _hitbox_collision(self, sprite_1, sprite_2):
        """
        Detects if the bala's rectangle intersects with the enemy's hitbox.
        """
        return sprite_1.rect.colliderect(sprite_2.hitbox)

    def _create_armada(self):
        """Build an enemy armada based on the screen dimensions."""
        enemigo = NaveEnemiga(self)
        rect_width, rect_height = enemigo.rect.size
        current_x = self.rect_pnt.width - rect_width
        current_y = self.options.margen_enemigo

        while current_x > (2 * rect_width + self.options.margen_enemigo):
            while (current_y + rect_height) < (
                self.rect_pnt.height - self.options.margen_enemigo
            ):
                self._create_enemy(current_y, current_x)
                current_y += rect_height + self.options.margen_enemigo
            current_x -= rect_width + self.options.margen_enemigo
            current_y = self.options.margen_enemigo

    def _create_enemy(self, value_y, value_x):
        """Generate an enemy with coordinates for proper armada placement."""
        new_enemy = NaveEnemiga(self)
        new_enemy.rect.x = value_x
        new_enemy.rect.y = value_y
        new_enemy.x = value_x
        new_enemy.y = value_y
        self.enemigos.add(new_enemy)

    def _update_armada(self):
        """Animate the armada as it travels across the screen."""
        self._check_vertical_edges()
        self.enemigos.update()

    def _check_vertical_edges(self):
        """Identify if an enemy is located toward the top or bottom edge."""
        for enemigo in self.enemigos:
            if enemigo.vertical_edges():
                self._change_armada_direction()
                break

    def _change_armada_direction(self):
        """Switch the armada's direction if it touches either edge."""
        for enemigo in self.enemigos:
            enemigo.x -= float(self.options.armada_left_speed)
        self.options.armada_direction *= -1

    def _render_screen(self):
        """Draw all game elements on pantalla."""
        self.pantalla.fill("black")
        self.naves.draw(self.pantalla)
        self.balas.draw(self.pantalla)
        self.enemigos.draw(self.pantalla)
        pygame.display.flip()


# Game execution.
if __name__ == "__main__":
    game = AstroPop()
    game.run_game()
