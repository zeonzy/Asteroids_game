from circleshape import *
from shot import *
from pulse import *
from explosions import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.radius = PLAYER_RADIUS
        self.lives = PLAYER_STARTING_LIVES
        self.shield = False #TBD
        self.timer = 0
        self.immortal_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):

        if self.immortal_timer > 0:
            pygame.draw.polygon(screen, "red", self.triangle(), 2) # TBD change effect!
        else:
            pygame.draw.polygon(screen, "white", self.triangle(), 2)

        if self.shield:
            pygame.draw.circle(screen, "white", self.position, self.radius + 5, 1)
            pygame.draw.circle(screen, "white", self.position, self.radius + 10, 1)
        pass

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        shot = Shot(*self.position, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN

    def respawn(self):
        explosion = Explosions(*self.position, self.radius * 2)
        self.lives -= 1
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        pulse = Pulse(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, 200)
        self.immortal_timer = 0.5

    def update(self, dt):
        #small optimisation to make sure we only modify the timer if there's something to time
        if self.timer >= 0:
            self.timer -= dt
        if self.immortal_timer >= 0:
            self.immortal_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)  
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()