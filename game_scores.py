import pygame.font

import resource_manager as rm


class GameScores:
    """Manages the logic for tracking & updating game scores"""

    def __init__(self, game):
        """
        Initialize attributes of the class using the provided game instance.
        """
        self.pantalla = game.pantalla
        self.rect_pnt = game.rect_pnt
        self.stats = game.stats

        font_size = int(self.rect_pnt.height * 0.07)
        self.fuente = pygame.font.SysFont("Impact", font_size)
        self.font = pygame.font.SysFont("Courier New", font_size)

        self.score_background = rm.resources.score
        self.rect_score_background = self.score_background.get_rect()
        self.rect_score_background.centerx = self.rect_pnt.centerx
        self.rect_score_background.top = self.rect_pnt.top + (
            self.rect_pnt.height * 0.05
        )
        self.format_score()

        self.record_background = rm.resources.record
        self.rect_record_background = self.record_background.get_rect()
        self.rect_record_background.centerx = self.rect_pnt.centerx
        self.rect_record_background.top = self.rect_pnt.top + (
            self.rect_pnt.height * 0.3
        )
        self.format_record()

        self.lives_button = rm.resources.lives_button
        self.rect_lives_button = self.lives_button.get_rect()
        self.rect_lives_button.center = (
            self.rect_pnt.width * 0.2,
            self.rect_pnt.height * 0.6,
        )
        self.format_lives()

    def format_score(self):
        """Format the current score & render it as an image for display."""
        round_score = int(round(self.stats.score, -1))
        score_str = f"{round_score:,}"
        self.score_font = self.fuente.render(score_str, True, "white")
        self.rect_score_font = self.score_font.get_rect()
        self.rect_score_font.centerx = self.rect_pnt.centerx
        self.rect_score_font.top = self.rect_score_background.bottom

    def format_record(self):
        """Format the highest score & render it as an image for display."""
        round_record = int(round(self.stats.record, -1))
        record_str = f"{round_record:,}"
        self.record_font = self.fuente.render(record_str, True, "white")
        self.rect_record_font = self.record_font.get_rect()
        self.rect_record_font.centerx = self.rect_pnt.centerx
        self.rect_record_font.top = self.rect_record_background.bottom

    def format_lives(self):
        """
        Render the 'Lives'label as a text image & centers it on the lives
        button for display on the screen.
        """
        lives_str = "Lives"
        self.lives_font = self.font.render(lives_str, True, "white")
        self.rect_lives_font = self.lives_font.get_rect()
        self.rect_lives_font.center = self.rect_lives_button.center

    def draw_scores(self):
        """
        Render & display score visuals & other related components on the
        screen.
        """
        self.pantalla.blit(self.score_background, self.rect_score_background)
        self.pantalla.blit(self.score_font, self.rect_score_font)

        self.pantalla.blit(
            self.record_background, self.rect_record_background
        )
        self.pantalla.blit(self.record_font, self.rect_record_font)

        self.pantalla.blit(self.lives_button, self.rect_lives_button)
        self.pantalla.blit(self.lives_font, self.rect_lives_font)
