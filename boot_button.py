import pygame.font

import resource_manager as rm


class BotonInicio:
    """Manages the game's startup process triggered by the start button."""

    def __init__(self, game, msg):
        """Initialize all the attributes of the class."""
        self.pantalla = game.pantalla
        self.rect_pnt = game.rect_pnt

        self.text_color = "white"
        self.fuente = pygame.font.SysFont(None, 48)

        self.image = rm.resources.boton_inicio
        self.rect = self.image.get_rect()
        self.rect.center = self.rect_pnt.center
        self._boton_msg(msg)

    def _boton_msg(self, msg):
        """_"""
        self.msg_image = self.fuente.render(msg, True, self.text_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_boton(self):
        """-"""
        self.pantalla.blit(self.image, self.rect)
        self.pantalla.blit(
            self.msg_image, (self.msg_rect.x, self.msg_rect.y - 5)
        )
