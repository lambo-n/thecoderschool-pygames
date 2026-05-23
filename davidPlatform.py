import pygame

class ObbyPlatform:
    def __init__(self, posx, posy, width, height, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)

    @property
    def top(self):    return self.rect.top
    @property
    def bottom(self): return self.rect.bottom
    @property
    def left(self):   return self.rect.left
    @property
    def right(self):  return self.rect.right

    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)