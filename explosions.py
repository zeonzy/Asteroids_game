# calculations from this post: https://www.reddit.com/r/learnpython/comments/guikog/draw_a_star_using_pygame/
import pygame # type: ignore
from math import cos, sin, pi

# Variable will be used as global to use memoization on the star coordinates
global_memoization_star_points = {}

def star_points(inner_radius, outer_radius, points):
    #this function calculates the points on a circle to draw a star shaped opbject
    global global_memoization_star_points

    #using memoization so we don't have to recalculate all the points all the time.
    key = (inner_radius, outer_radius, points)
    if key in global_memoization_star_points:
        return global_memoization_star_points[key]

    r_seq = [inner_radius, outer_radius]* points
    star_coords = tuple(
    pygame.Vector2(r*cos(2*pi*index/(points * 2) - pi/2), r*sin(2*pi*index/(points * 2) - pi/2)) 
    for r, index in zip(r_seq, range((points * 2)))
    )
    global_memoization_star_points[key] = star_coords
    return star_coords


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
        star_coords = star_points(self.inner_radius, self.outer_radius, self.points)
        star_at_coords = [vertex + self.position for vertex in star_coords]
        pygame.draw.polygon(screen, (255,255,255), star_at_coords, 1)

    def update(self, dt):
        if self.outer_radius < 5 and self.grow == False:
            self.kill()

        #makes the explosing first grow, then recede
        if self.grow:
            self.inner_radius = self.inner_radius * self.exp_speed
            self.outer_radius = self.outer_radius * self.exp_speed
            if self.outer_radius >= self.max_radius:
                self.grow = False
        else:
            self.inner_radius = self.inner_radius / self.exp_speed
            self.outer_radius = self.outer_radius / self.exp_speed