import pygame

class Projectile:
    def __init__(self, pos, direction, tag):
        self.pos = pygame.Vector2(pos)
        self.direction = pygame.Vector2(direction, 0).normalize()
        self.speed = 250
        self.image = pygame.image.load("assets/bitcoin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 10))
        self.tag = tag
        
    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        
    def get_rect(self):
        return pygame.Rect(self.pos.x, self.pos.y, self.image.get_width(), self.image.get_height())
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)