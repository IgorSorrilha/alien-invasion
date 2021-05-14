import sys

import pygame

def iniciar_jogo():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    color = (230, 230, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                event.key

        screen.fill(color)
        pygame.display.flip()

iniciar_jogo()