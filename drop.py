import pygame # type: ignore
from constants import *
from circleshape import *
from player import *
import random

# creates a loot table, see CONSTANTS
table_size = LOOT_TABLE[0]
final_table = [None,] * table_size
for loot in LOOT_TABLE[1:]:
    counter = 0
    item = loot[0]
    amount = loot[1]
    if counter + amount <= table_size:
        for i in range(amount):
            final_table[counter] = item
            counter += 1
    else:
        print("To much loot for the sized table")
    #print(final_table)



class Drop(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # roll to see if there's loot, if not kill itself
        random_roll = int(random.uniform(0,table_size))
        if final_table[random_roll] == None:
            self.kill()
        self.pos_x = x
        self.pos_y = y
        self.radius = radius
        self.timer = LOOT_TIMER
        self.item = final_table[random_roll]
    
    def give_loot(self, player):
        if self.item == "S":
            self.give_shield(player)

    def give_shield(self, player):
        player.shield = True
        self.kill()

    def draw(self, screen):
        # returns tuple with (screen, rect)
        def_font = pygame.freetype.Font(None, 12).render(f"S", fgcolor = (255,255,255))
        # rect = (left, top, width, height)
        # using half the width and height to center the text in the circle
        screen.blit(def_font[0], (self.pos_x - (def_font[1][2] / 2), self.pos_y - (def_font[1][3] / 2)))
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            self.kill()