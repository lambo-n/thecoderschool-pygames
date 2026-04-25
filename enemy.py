import pygame
import random

class Enemy:
    def __init__ (self, pos):
        self.pos = pygame.Vector2(pos)
        self.image = pygame.image.load("assets/robotVillain.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.speed = 100
        self.directionChange = 0
        self.direction = 1
        
    def update(self, dt):
        if self.directionChange >= 50:
            self.directionChange = 0
            self.direction *= -1
            
        self.directionChange += 1
            
        self.pos.x += self.direction * self.speed * dt
        
    def shootChance(self):
        randomNum = random.randint(0, 1000)
        if randomNum < 5:
            return self.pos
        else: 
            return None
        
    def get_rect(self):
        return pygame.Rect(self.pos.x, self.pos.y, self.image.get_width(), self.image.get_height())

    def draw(self, screen):
        screen.blit(self.image, self.pos)