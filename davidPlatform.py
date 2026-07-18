import pygame

class ObbyPlatform:
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

    def update(self,screen, player_pos ,playerHitbox):
        pygame.draw.rect(screen, self.color, self.rect)
        return False


        


class Teleporter(ObbyPlatform):
    def __init__(self, posx, posy, width, height, color,teleportX,teleportY):

        super().__init__(posx, posy, width, height, color)

        self.teleportX = teleportX
        self.teleportY = teleportY
        

    def update(self,screen,player_pos,playerHitbox):
        super().update(screen, player_pos ,playerHitbox)
  
        if playerHitbox.colliderect(self.rect):
            player_pos.x = self.teleportX
            player_pos.y = self.teleportY




class Killblock(ObbyPlatform):
    def __init__(self, posx, posy, width, height, color):

        super().__init__(posx, posy, width, height, color)
    
    def update(self,screen,player_pos,playerHitbox):
            super().update(screen, player_pos ,playerHitbox)
    
            return playerHitbox.colliderect(self.rect)
                

class Escape(ObbyPlatform):


    def __init__(self, posx, posy, width, height, color,escapeX,escapeY):

        super().__init__(posx, posy, width, height, color)

        self.escapeX = escapeX
        self.escapeY = escapeY

    def update(self,screen,player_pos,playerHitbox):
            super().update(screen, player_pos ,playerHitbox)
    
            if playerHitbox.colliderect(self.rect):
                print("escape")










