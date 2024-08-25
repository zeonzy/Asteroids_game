# calculations from this post: https://www.reddit.com/r/learnpython/comments/guikog/draw_a_star_using_pygame/
import pygame # type: ignore
from math import cos, sin, pi

class Explosions(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.outer_radius = radius / 10
        self.inner_radius = self.outer_radius / 3
        self.max_radius = radius
        self.position = pygame.Vector2(x, y)
        self.grow = True
        self.points = 5
        self.exp_speed = 1.2

    def draw(self, screen):
        r_seq = [self.inner_radius, self.outer_radius]*self.points
        STAR_BASE_POLY = tuple(
        pygame.Vector2(r*cos(2*pi*index/(self.points * 2) - pi/2), r*sin(2*pi*index/(self.points * 2) - pi/2)) 
        for r, index in zip(r_seq, range((self.points * 2)))
        )
        star_at_coords = [vertex + self.position for vertex in STAR_BASE_POLY]
        pygame.draw.polygon(screen, (255,255,255), star_at_coords, 1)

    def update(self, dt):
        if self.outer_radius < 5 and self.grow == False:
            self.kill()

        if self.grow:
            self.inner_radius = self.inner_radius * self.exp_speed
            self.outer_radius = self.outer_radius * self.exp_speed
            if self.outer_radius >= self.max_radius:
                self.grow = False
        else:
            self.inner_radius = self.inner_radius / self.exp_speed
            self.outer_radius = self.outer_radius / self.exp_speed