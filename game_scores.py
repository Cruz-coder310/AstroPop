import pygame.font

import resource_manager as rm


class GameScores:
    """Manages the logic for tracking & updating game scores"""

    def __init__(self, game):
        """"""
        self.pantalla = game.pantalla
        self.rect_pnt = game.rect_pnt
        self.stats = game.stats

        self.fuente = pygame.font.SysFont(None, 60)
        self.score_image1 = rm.resources.score
        self.score_rect = self.score_image1.get_rect()
        self.score_rect.centerx = self.rect_pnt.centerx

        self.format_score()

    def format_score(self):
        """"""
        round_score = round(self.stats.score, -1)
        score_str = f"{round_score:,}"
        self.score_image = self.fuente.render(score_str, True, "white")
        self.rect_score = self.score_image.get_rect()
        self.rect_score.centerx = self.rect_pnt.centerx
        self.rect_score.y = self.rect_pnt.y + 50

    def draw_scores(self):
        """"""
        self.pantalla.blit(self.score_image, self.rect_score)
        self.pantalla.blit(self.score_image1, self.score_rect)
