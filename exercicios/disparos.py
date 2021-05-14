import pygame
from pygame.sprite import Sprite

class Disparo(Sprite):
    """Uma classe que administra projéteis disparados pela espaçonave"""

    def __init__(self, ai_settings, screen, nave):
        """Cria um objeto para o projétil na posição atual da espaçonave."""
        super(Disparo, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.disparo_width,
            ai_settings.disparo_height)
        
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.disparo_color
        self.speed_factor = ai_settings.disparo_speed_factor

    
    def update(self):
        """Move o projétil para cima na tela."""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def desenhar_disparo(self):
        """Desenha o projétil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)

