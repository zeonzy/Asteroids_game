from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        velocity = ASTEROID_SPEED
        self.position  += (self.velocity * dt)



