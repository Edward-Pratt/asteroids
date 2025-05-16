import random

import pygame.draw

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "grey",self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        degree = random.uniform(20, 50)
        new_direction_1 = self.velocity.rotate(degree)
        new_direction_2 = self.velocity.rotate(-degree)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_direction_1 * 1.2
        asteroid_2.velocity = new_direction_2 * 1.2
