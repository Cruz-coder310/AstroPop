import pygame.font
from pygame.sprite import Group
from nave import Nave

import resource_manager as rm


class GameScores:
    """Manages the logic for tracking & updating game scores"""

    def __init__(self, game):
        """
        Initialize attributes of the class using the provided game instance.
        """
        self.game = game
        self.pantalla = game.pantalla
        self.rect_pnt = game.rect_pnt
        self.stats = game.stats

        font_size = int(self.rect_pnt.height * 0.07)
        fuente_size = int(self.rect_pnt.height * 0.1)
        self.fuente = pygame.font.SysFont("Impact", font_size)
        self.font = pygame.font.SysFont("Impact", fuente_size)

        self.score_panel = rm.resources.panel_pause_blue
        self.rect_score_panel = self.score_panel.get_rect()

        self.score_label = rm.resources.score
        self.rect_score_label = self.score_label.get_rect()
        self.rect_score_label.centerx = self.rect_score_panel.centerx
        self.rect_score_label.top = self.rect_score_panel.height * 0.1
        self.format_score()

        self.record_label = rm.resources.record
        self.rect_record_label = self.record_label.get_rect()
        self.rect_record_label.centerx = self.rect_score_panel.centerx
        self.rect_record_label.top = self.rect_score_panel.height * 0.5
        self.format_record()

        self.lives_panel = rm.resources.panel_pause_red
        self.rect_lives_panel = self.lives_panel.get_rect()
        self.rect_lives_panel.midright = self.rect_pnt.midright
        self.format_lives()
        self.prepare_naves()

    def format_score(self):
        """Format the current score & render it as an image for display."""
        round_score = int(round(self.stats.score, -1))
        score_str = f"{round_score:,}"
        self.score_font = self.fuente.render(score_str, True, "white")
        self.rect_score_font = self.score_font.get_rect()
        self.rect_score_font.centerx = self.rect_score_panel.centerx
        self.rect_score_font.top = self.rect_score_label.bottom

    def format_record(self):
        """Format the highest score & render it as an image for display."""
        round_record = int(round(self.stats.record, -1))
        record_str = f"{round_record:,}"
        self.record_font = self.fuente.render(record_str, True, "white")
        self.rect_record_font = self.record_font.get_rect()
        self.rect_record_font.centerx = self.rect_score_panel.centerx
        self.rect_record_font.top = self.rect_record_label.bottom

    def format_lives(self):
        """
        Render the 'Lives'label as a text image & centers it on the lives
        button for display on the screen.
        """
        lives_str = "Lives"
        self.lives_font = self.font.render(lives_str, True, "white")
        self.rect_lives_font = self.lives_font.get_rect()
        self.rect_lives_font.centerx = self.rect_lives_panel.centerx
        self.rect_lives_font.centery = self.rect_lives_panel.height * 0.25

    def prepare_naves(self):
        """
        Draws ship icons on the panel to show how many lives the player has
        left.
        """
        self.naves = Group()
        top_margen = self.rect_lives_panel.height * 0.3
        spacing = self.rect_pnt.height * 0.05
        initial_position = self.rect_lives_panel.top + top_margen
        for nave_index in range(self.stats.vidas + 1):
            nave = Nave(self.game)
            nave.rect.centerx = self.rect_lives_panel.centerx
            vertical_offset = nave_index * (nave.rect.height + spacing)
            nave.rect.top = initial_position + vertical_offset
            self.naves.add(nave)

    def draw_scores(self):
        """
        Render & display score visuals & other related components on the
        screen.
        """

        self.pantalla.blit(self.score_panel, self.rect_score_panel)
        self.pantalla.blit(self.score_label, self.rect_score_label)
        self.pantalla.blit(self.score_font, self.rect_score_font)

        self.pantalla.blit(self.record_label, self.rect_record_label)
        self.pantalla.blit(self.record_font, self.rect_record_font)

        self.pantalla.blit(self.lives_panel, self.rect_lives_panel)
        self.pantalla.blit(self.lives_font, self.rect_lives_font)
        self.naves.draw(self.pantalla)
