import pygame

class CustomPlatform:
    def __init__ (self, posx, posy, width, height, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)



    @property
    def top(self): return self.rect.top
    @property
    def bottom(self): return self.rect.bottom
    @property
    def left(self): return self.rect.left
    @property
    def right(self): return self.rect.right

    def update(self,screen, player_rect=None):
        pygame.draw.rect(screen, self.color, self.rect)
        return None




class EscapeDoor(CustomPlatform):
    def __init__(self, posx, posy, width, height, spawnx, spawny):
        super().__init__(posx, posy, width, height, "green")
        self.spawnx = spawnx
        self.spawny = spawny 


    def update(self, screen, player_rect):
        super().update(screen)

        if player_rect is not None and player_rect.colliderect(self.rect):
            return "escape"


