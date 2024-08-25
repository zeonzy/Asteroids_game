import pygame # type: ignore
from constants import *

class Score():
    def __init__(self):
        self.score = 0
        self.size = 20
        self.pos_x = SCREEN_WIDTH -200
        self.pos_y = 5

    def show_score(self, screen):
        #render white score text
        default_font = pygame.freetype.Font(None, self.size).render(f"Score: {self.score}", fgcolor = (255,255,255))
        return screen.blit(default_font[0], (self.pos_x, self.pos_y))

    def add_score(self, add):
        self.score += add
    
    def __str__(self):
        return str(self.score)
    
    
