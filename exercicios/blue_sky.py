import sys
import pygame
from crash import Crash

def rg():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('blue sky')
    bg_color = (0, 0, 230)

    crash = Crash(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)

        crash.blitme()

        pygame.display.flip()
rg()

