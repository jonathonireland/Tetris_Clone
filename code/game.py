from settings import *

class Game:
    def __init__(self):

        # general 
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))

        # lines
        self.line_surface = self.surface.copy()
        self.line_surface.fill((0,255,0))
        self.line_surface.set_colorkey((0,255,0))
        self.line_surface.set_alpha(120)

        #test
        self.block = Block()

    def draw_grid(self):
        for col in range(1,COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.surface, LINE_COLOR, (x, 0), (x, self.surface.get_height()), 1)
        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.surface, LINE_COLOR, (0, y), (self.surface.get_width(),y), 1)        

    def run(self):

        # drawing
        self.surface.fill(GRAY)

        self.draw_grid()
        self.display_surface.blit(self.surface, (20,20))
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)

class Block(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = (0,0))