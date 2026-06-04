import pygame

# A platform is just a pygame.Rect that also remembers how to draw itself
# (its color) and what kind of platform it is (its type).
class CustomPlatform(pygame.Rect):
    def __init__(self, posx, posy, width, height, color="black", type="normal"):
        super().__init__(posx, posy, width, height)
        self.color = color
        self.type = type
