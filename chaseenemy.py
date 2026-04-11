import pygame
import random

class Enemy:
    def __init__(self):
        self.direction = random.choice([-1, 1])
        
        self.pos = pygame.Vector2(0, 0)
        self.pos.y = random.randint(50, 550)
        
        if self.direction == 1:
            self.pos.x = 50
        else:
            self.pos.x = 1180
        
        self.health = 10

        
    def update(self, dt):
        self.pos.x += 100 * dt * self.direction
        