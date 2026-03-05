import pygame

class Enemy:
    def __init__ (self, pos, image):
        self.pos = pos
        self.image = image
        
    def update(self, player_pos, dt):
        # Move towards the player
        dx = player_pos.x - self.pos.x
        dy = player_pos.y - self.pos.y
        distance = max(1, (dx**2 + dy**2)**0.5)
        self.pos.x += (dx / distance) * 100 * dt
        self.pos.y += (dy / distance) * 100 * dt
        
    def draw(self, screen, ):
        screen.blit(self.image, self.pos)