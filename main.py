# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame # type: ignore
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from score import *
from sys import exit
from lives import *
from pulse import *
from explosions import *

def main():
    #initialise
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids game")
    clock = pygame.time.Clock()
    dt = 0 # dt = delta time
    score = Score()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    pulses = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Pulse.containers = (pulses, updatable, drawable)
    Explosions.containers = (explosions, updatable,drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def quitgame():
        print(f"Manually exited the game. You're score was: {score}")
        exit()


    #main game loop
    while True:
        if pygame.key.get_pressed()[pygame.K_ESCAPE]: #exit if escape is pressed
            quitgame()

        for event in pygame.event.get(): #exit if the X on the window is clicked
            if event.type == pygame.QUIT:
                quitgame()
            
        screen.fill("black")

        for update in updatable:
            update.update(dt)
        for draw in drawable:
            draw.draw(screen)

        for asteroid in asteroids:
            if player.collision_check(asteroid):
                if player.lives > 1:
                    player.respawn()
                else:
                    print(f"Game over! You're score was: {score}")
                    exit()
            for shot in shots:
                if shot.collision_check(asteroid):
                    explosion = Explosions(*shot.position, asteroid.radius / 2)

                    shot.kill()
                    asteroid.split(score)
            for pulse in pulses:
                if pulse.collision_check(asteroid):
                    asteroid.kill()


        score.show_score(screen) # show score text
        show_lives(screen, player) # show lives text

        pygame.display.flip() #write to screen

        #limit to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
