import pygame

#TYPES:
# normal - black
# phase - purple

# A platform is just a pygame.Rect that also remembers how to draw itself
# (its color) and what kind of platform it is (its type).
class CustomPlatform(pygame.Rect):
    def __init__(self, posx, posy, width, height, type="normal"):
        super().__init__(posx, posy, width, height)
        self.type = type
        
        if type == "normal":
            self.color = "black"
        elif type == "phase":
            self.color = "purple"
        elif type == "bounce":
            self.color = "blue"
        else:
            self.color = "black"
    
