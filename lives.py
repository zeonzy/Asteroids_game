import pygame # type: ignore
from constants import *

size = 20
pos_x = 5
pos_y = 5

def show_lives(screen, player):
    #render white score text
    default_font = pygame.freetype.Font(None, size).render(f"Lives: {player.lives}", fgcolor = (255,255,255))
    return screen.blit(default_font[0], (pos_x, pos_y))
    
    
    
