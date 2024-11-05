import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def split(self):
        rand_a = random.uniform(20, 50)
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_v1 = self.velocity.rotate(rand_a)
        new_v2 = self.velocity.rotate(-rand_a)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        speed_inc = 1.2
        new_rock1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_rock2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_rock1.velocity = new_v1 * speed_inc
        new_rock2.velocity = new_v2 * speed_inc
        

    def update(self, dt):
        self.position += (self.velocity * dt)