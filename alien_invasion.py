import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    # Inicializa o pygame, as configurações e o objeto screen
    pygame.init() 
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria o botão Play
    play_button = Button(ai_settings, screen, "Jogar")

    # Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)
    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    # Cria um alienígena 
    aliens = Group()

    # Cria a frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Inicializa o laço principal do jogo
    while True:
        # Observa eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
            aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, 
                bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                 bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
            bullets, play_button)

run_game() 