import pygame

class Projectile:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 40
        self.image = pygame.image.load("assets/bomb.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        
    # move the projectile
    def update(self, dt):
        self.x += 100 * dt
    
    # draw it on the screen
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    