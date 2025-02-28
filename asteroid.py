import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self):
        pygame.draw.circle(self.x, self.y, self.radius, 2)

    def update(self, dt):
        self.x += self.velocity * dt
        self.y += self.velocity * dt