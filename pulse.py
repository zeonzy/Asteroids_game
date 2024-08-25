from circleshape import *
from score import *

class Pulse(CircleShape):
    def __init__(self, x, y, start_radius, end_radius):
        super().__init__(x, y, start_radius)
        self.end_radius = end_radius
        self.cur_radius = start_radius

        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.cur_radius, 2)
        pygame.draw.circle(screen, "white", self.position, self.cur_radius + 1, 2)

    def update(self, dt):
        if self.cur_radius < self.end_radius:
            self.cur_radius += 4
            self.radius = self.cur_radius
        else:
            self.kill()