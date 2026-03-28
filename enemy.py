import pygame

class Enemy:
    def __init__ (self, pos):
        self.pos = pos 
        self.image = pygame.image.load("assets/enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        
    def update(self, player_pos, dt):
        pass
        
    def get_rect(self):
        return pygame.Rect(self.pos.x, self.pos.y, self.image.get_width(), self.image.get_height())

    def draw(self, screen):
        screen.blit(self.image, self.pos)