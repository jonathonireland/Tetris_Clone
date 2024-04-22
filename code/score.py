from settings import *

class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT *SCORE_HEIGHT_FRACTION - (20)))
        self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - (20), WINDOW_HEIGHT - (20)))
        self.display_surface = pygame.display.get_surface()
    
    def run(self):
        self.display_surface.blit(self.surface,self.rect)