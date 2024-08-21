# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame # type: ignore
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    #initialise
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    #dt = delta time
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    #main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for update in updatable:
            update.update(dt)
        for draw in drawable:
            draw.draw(screen)
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                return

        
        pygame.display.flip()

        #limit to 60 fps
        dt = clock.tick(60) / 1000

        



if __name__ == "__main__":
    main()
