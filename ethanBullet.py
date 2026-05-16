import pygame

class Bullet:
    def __init__ (self, pos, target):
        self.pos = pos
        self.bounces = 0
        direction = target - pos
        if direction.length() > 0:
            self.direction = direction.normalize()
        else:
            self.direction = pygame.Vector2(0, -1)

    def update(self, dt):
        self.pos += self.direction * 500 * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, "black", self.pos, 10)

    def collidepoint(self, point):
        return self.pos.distance_to(point) < 40