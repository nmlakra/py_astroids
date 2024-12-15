from circleshape import CircleShape
from constants import WHITE
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt