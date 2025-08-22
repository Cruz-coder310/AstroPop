import pygame
import sys
from time import sleep
from nave import Nave
from options import Options
import resource_manager
from balas import Bala
from nave_enemiga import NaveEnemiga
from boot_button import BotonInicio
from game_stats import GameStats
from game_scores import GameScores
from game_stages import GameStages


class AstroPop:
    """Main game class that controls AstroPop."""

    def __init__(self):
        """Initialize game attributes and Pygame settings."""
        pygame.init()
        self.reloj = pygame.time.Clock()

        self.pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.rect_pnt = self.pantalla.get_rect()
        pygame.display.set_caption("AstroPop")

        self.options = Options(self)

        # Asset management
        resource_manager.init_manager(self)
        self.background = resource_manager.resources.background

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
        # Flag to control whether the game is frozen.
        self.game_active = GameStages.START

        self.boton = BotonInicio(self, "Play")
        self.stats = GameStats(self)
        self.scores = GameScores(self)

    def run_game(self):
        """Main game loop running at 60 FPS."""
        while True:
            self._process_events()
            if self.game_active == GameStages.IN_GAME:
                self._update_nave()
                self._update_balas()
                self._update_armada()
            self._render_screen()
            self.reloj.tick(60)

    def _reset_positions(self, reset_enemigos=True):
        """
        Helper to reposition the ship, clear balas & optionally reset
        enemigos after life loss or game restart.
        """
        self.balas.empty()
        if reset_enemigos:
            self.enemigos.empty()
        self._create_armada()
        self.nave.set_position()

    def _process_events(self):
        """Handle keyboard and system events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_boton(mouse_pos)

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
        elif event.key == pygame.K_p:
            if self.game_active == GameStages.IN_GAME:
                self.game_active = GameStages.PAUSE
            elif self.game_active == GameStages.PAUSE:
                self.game_active = GameStages.IN_GAME
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

    def _check_play_boton(self, mouse_pos):
        """Helper to activate the game when the Play boton is clicked."""
        if (
            self.boton.rect.collidepoint(mouse_pos)
            and self.game_active == GameStages.START
        ):
            self.game_active = GameStages.IN_GAME
            self.stats.initial_values()
            self._reset_positions()
            self.options.set_default_speeds()
            self.scores.format_score()
            self.scores.prepare_naves()
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.balas) < self.options.balas:
            new_bala = Bala(self)
            self.balas.add(new_bala)

    def _update_nave(self):
        """Update the nave's position & check for collisions."""
        self.naves.update()
        # Check if the nave takes damage from enemy collisions.
        if pygame.sprite.spritecollideany(
            self.nave, self.enemigos, collided=pygame.sprite.collide_mask
        ):
            self._handle_life_loss()
        self._check_enemy_left_edge_hit()

    def _handle_life_loss(self):
        """
        Manages the nave's life loss in response to damage or enemy
        advancement.
        """
        if self.stats.vidas > 0:
            self.stats.vidas -= 1
            self._reset_positions()
            self.scores.prepare_naves()
            sleep(0.5)
        else:
            sleep(0.5)
            self.game_active = GameStages.START

    def _check_enemy_left_edge_hit(self):
        """
        Monitors enemy nave movement & activates hit behavior when they reach
        the left side of the screen
        """
        for enemigo in self.enemigos.sprites():
            if enemigo.rect.x <= 0:
                self._handle_life_loss()
                break

    def _update_balas(self):
        """
        Update the position of the balas on the screen & remove those that
        have moved off-screen.
        """
        self.balas.update()
        for bala in self.balas:
            if bala.rect.left >= self.rect_pnt.right:
                bala.kill()
        # This print lets me see if the bala was deleted after moving
        # off-screen.
        # print(len(self.balas))
        self._check_collide_bullet_enemy()

    def _check_collide_bullet_enemy(self):
        """removes any balas & enemigos that have collided."""
        collision = pygame.sprite.groupcollide(
            self.balas,
            self.enemigos,
            True,
            True,
            collided=pygame.sprite.collide_mask,
        )
        if collision:
            for enemy_list in collision.values():
                self.stats.score += self.options.enemy_value * len(
                    enemy_list
                )
                if self.stats.score > self.stats.record:
                    self.stats.record = self.stats.score
                    self.scores.format_record()
            self.scores.format_score()

        if not self.enemigos:
            self._reset_positions(reset_enemigos=False)
            self.options.increase_speeds()

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
        if self.game_active == GameStages.IN_GAME:
            self.pantalla.blit(self.background, (0, 0))
            self.naves.draw(self.pantalla)
            self.balas.draw(self.pantalla)
            self.enemigos.draw(self.pantalla)
        elif self.game_active == GameStages.START:
            self.pantalla.blit(self.background, (0, 0))
            self.boton.draw_boton()
            pygame.mouse.set_visible(True)
        elif self.game_active == GameStages.PAUSE:
            self.pantalla.fill("black")
            self.scores.draw_scores()
        pygame.display.flip()


# Game execution.
if __name__ == "__main__":
    game = AstroPop()
    game.run_game()
