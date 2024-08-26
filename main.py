import pygame # type: ignore
# this allows us to use code from
# the open-source pygame library
# throughout this file

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from score import *
from sys import exit
from lives import *
from pulse import *
from explosions import *
from drop import *

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
    drops = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Pulse.containers = (pulses, updatable, drawable)
    Explosions.containers = (explosions, updatable, drawable)
    Drop.containers = (drops, updatable, drawable)

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
        
        # Make a black background    
        screen.fill("black")

        for asteroid in asteroids:
            # if a collision between player and astroid is detected V
            if player.collision_check(asteroid):
                # if the player has immortality left
                if player.immortal_timer > 0:
                    asteroid.split(score)
                    explosion = Explosions(*asteroid.position, asteroid.radius / 2)
                #if player has a shield
                elif player.shield:
                    # TBD maybe make an actual shield to interact with?
                    # maybe make it multi tiered?
                    new_pulse = Pulse(*player.position, PLAYER_RADIUS, PLAYER_RADIUS * 4)
                    player.shield = False
                else:
                    # if player is hit
                    if player.lives > 1:
                        player.respawn()
                    else:
                        print(f"Game over! You're score was: {score}")
                        exit()
            # if a collision between a shot and player is detected V
            for shot in shots:
                if shot.collision_check(asteroid):
                    explosion = Explosions(*shot.position, asteroid.radius / 2)

                    shot.kill()
                    asteroid.split(score)
            
            # if collision between a pulse effect and and astroid is detected V
            for pulse in pulses:
                if pulse.collision_check(asteroid):
                    asteroid.kill()

            # if collision between player and a drop occurs
            for drop in drops:
                if player.collision_check(drop):
                    # TBD just shield for now, make more usefull
                    drop.give_loot(player)


        score.show_score(screen) # show score text
        show_lives(screen, player) # show lives text

        for update in updatable:
            update.update(dt)
            #print(update)
        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip() #write to screen

        #limit to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
