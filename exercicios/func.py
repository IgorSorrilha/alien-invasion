import sys
import pygame
from disparos import Disparo

def check_keydown_events(event, ai_settings, screen, nave, disparos):
    """Responde a pressionamentos de tecla."""
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True   
    
    elif event.key == pygame.K_DOWN:
        nave.moving_down = True
    
    elif event.key == pygame.K_UP:
        nave.moving_up = True  

    elif event.key == pygame.K_SPACE:
        disparar(ai_settings, screen, nave, disparos)

def disparar(ai_settings, screen, nave, disparos):
    if len(disparos) < ai_settings.disparos_allowed:
        novo_disparo = Disparo(ai_settings, screen, nave)
        disparos.add(novo_disparo)
        
        
def check_keyup_events(event, nave):
    """Responde a solturas de tecla."""
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
            
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False
    
    elif event.key == pygame.K_UP:
        nave.moving_up = False
    
    elif event.key == pygame.K_DOWN:
        nave.moving_down = False

def check_events(ai_settings, screen, nave, disparos):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, nave, disparos)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, nave)
        
def update_screen(ai_settings, screen, nave, disparos):
    """Atualiza as imagens na tela e alterna para a nova tela"""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    for disparo in disparos.sprites():
        disparo.desenhar_disparo()
        
    nave.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()

def disparos_update(disparos):
    disparos.update()

    for disparo in disparos.copy():
            if disparo.rect.bottom <= 0:
                disparos.remove(disparo)