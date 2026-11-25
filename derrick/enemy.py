import pygame

class Enemy:

    def __init__(self, posx, posy, width, height, direction, speed, firerate, offset, color="white"):

        self.x = posx
        self.y = posy
        self.w = width
        self.h = height
        self.d = direction
        self.s = speed
        self.f = firerate
        self.ofs = offset
        self.color = color
        self.rect = pygame.Rect(posx, posy, width, height)
        self.image = pygame.image.load("assets/CannonFrame0.png")
        self.image = pygame.transform.scale(self.image, (width, height))
    def draw(self, screen):

        screen.blit(self.image, self.rect)
        
    def update(self, dt):
        
        # timer coder goes here
        
        return "shoot"
