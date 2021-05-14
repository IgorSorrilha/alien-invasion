import pygame
from pygame.sprite import Group
from cfg import Cfg
from nave import Nave
import func as gf


def run_game():
    # Inicializa o pygame, as configurações e o objeto screen
    pygame.init()
    ai_settings = Cfg()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("invasao alien")

    # Cria uma espaçonave
    nave = Nave(ai_settings, screen)

    disparos = Group()
    
    # Inicializa o laço principal do jogo
    while True:
        # Observa eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, nave, disparos)
        nave.update()
        gf.disparos_update(disparos)
        gf.update_screen(ai_settings, screen, nave, disparos)

run_game()