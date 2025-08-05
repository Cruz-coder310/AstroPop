import pygame

import sys

from nave import Nave

from options import Options

from balas import Bala


class Rocket:
    """control overall of the game"""

    def __init__(self):
        """initialize the attributes of the game"""
        pygame.init()

        self.pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("AstroPop")

        self.options = Options()
        self.nave = Nave(self)
        self.balas = Bala(self)
        self.reloj = pygame.time.Clock()

    def run_game(self):
        """main loop to run the game"""
        while True:
            self._events()
            self.nave.movement()
            self._art_painting()
            self.reloj.tick(60)

    def _events(self):
        """recolect all the event from the keyboard"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._movement_keydown(event)
            elif event.type == pygame.KEYUP:
                self._movement_keyup(event)

    def _movement_keydown(self, event):
        """recive all the keydown movements & act about it"""
        if event.key == pygame.K_RIGHT:
            self.nave.r_flag = True
        elif event.key == pygame.K_LEFT:
            self.nave.l_flag = True
        elif event.key == pygame.K_UP:
            self.nave.u_flag = True
        elif event.key == pygame.K_DOWN:
            self.nave.d_flag = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _movement_keyup(self, event):
        """recive all the keydown movements & act about it"""
        if event.key == pygame.K_RIGHT:
            self.nave.r_flag = False
        elif event.key == pygame.K_LEFT:
            self.nave.l_flag = False
        elif event.key == pygame.K_UP:
            self.nave.u_flag = False
        elif event.key == pygame.K_DOWN:
            self.nave.d_flag = False

    def _art_painting(self):
        """drawing the all art in the screen"""
        self.pantalla.fill("black")
        self.nave.materialize()
        self.balas.materialize()
        pygame.display.flip()


rocket = Rocket()
rocket.run_game()
