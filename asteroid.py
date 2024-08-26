from circleshape import *
from score import *
from drop import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position  += (self.velocity * dt)

    def split(self,score):
        self.kill()

        if self.radius == 3 * ASTEROID_MIN_RADIUS: #large asteroid
            score.add_score(20)
        elif self.radius == 2 * ASTEROID_MIN_RADIUS: # mediums asteroid
            score.add_score(50)
        elif self.radius ==  ASTEROID_MIN_RADIUS: # small asteroid
            score.add_score(50)
            # make the smallest astroid drop random loot
            drop_loot = Drop(*self.position, 15)

        else: # tbd
            score.add_score(200)
        

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        asteroid1 = Asteroid(*self.position,self.radius - ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(*self.position,self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = self.velocity * 1.2
        asteroid2.velocity = self.velocity * 1.2
        asteroid1.velocity = self.velocity.rotate(random_angle)
        asteroid2.velocity = self.velocity.rotate(-random_angle)



