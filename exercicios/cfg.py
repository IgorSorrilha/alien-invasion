class Cfg():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""

    def __init__(self):
       
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.nave_speed_factor = 1.5

        self.disparo_speed_factor = 1
        self.disparo_width = 3
        self.disparo_height = 15
        self.disparo_color = 230, 60, 60
        self.disparos_allowed = 3
        
