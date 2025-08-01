import pygame

import sys

from nave import Nave


class Rocket:
    """control overall of the game"""

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.reloj = pygame.time.Clock()
        self.nave = Nave(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
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
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.nave.r_flag = False
                    elif event.key == pygame.K_LEFT:
                        self.nave.l_flag = False
                    elif event.key == pygame.K_UP:
                        self.nave.u_flag = False
                    elif event.key == pygame.K_DOWN:
                        self.nave.d_flag = False

            self.nave.movement()
            self.pantalla.fill("black")
            self.nave.materialize()
            pygame.display.flip()
            self.reloj.tick(60)


rocket = Rocket()
rocket.run_game()
