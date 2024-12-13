from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, WHITE
import pygame


class Player(CircleShape):
    
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)

        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def rotate_left(self, dt):
        self.rotate(dt)

    def rotate_right(self, dt):
        self.rotate(dt * -1) 

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def move_forward(self, dt):
        self.move(dt)
        
    def move_backward(self, dt):
        self.move(dt * -1)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate_left(dt)
        if keys[pygame.K_d]:
            self.rotate_right(dt)
        if keys[pygame.K_w]:
            self.move_forward(dt)
        if keys[pygame.K_s]:
            self.move_backward(dt)