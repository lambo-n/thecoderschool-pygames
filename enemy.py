import pygame

class Enemy:
    def __init__ (self, pos, enemyType):
        self.pos = pos
        
        if enemyType == "normal":
            self.health = 100
            self.speed = 100
            self.strength = 1
            self.image = pygame.image.load("assets/digdug.png").convert_alpha()
            
        self.image = pygame.transform.scale(self.image, (50, 50))
        
    def update(self, player_pos, dt):
        # Move towards the player
        dx = player_pos.x - self.pos.x
        dy = player_pos.y - self.pos.y
        distance = max(1, (dx**2 + dy**2)**0.5)
        self.pos.x += (dx / distance) * self.speed * dt
        self.pos.y += (dy / distance) * self.speed * dt
        
    def get_rect(self):
        return pygame.Rect(self.pos.x, self.pos.y, self.image.get_width(), self.image.get_height())

    def draw(self, screen, ):
        screen.blit(self.image, self.pos)