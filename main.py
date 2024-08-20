# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame # type: ignore
from constants import *
from player import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    #dt = delta time
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #screen.fill(pygame.Color(0,0,0))
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        #limit to 60 fps
        dt = clock.tick(60) / 1000

        



if __name__ == "__main__":
    main()
