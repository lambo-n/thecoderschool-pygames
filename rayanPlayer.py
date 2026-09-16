import pygame

player1_image = pygame.image.load("assets/jumpboy.png")
player1_image = pygame.transform.scale(player1_image, (140, 140))

player1_punch = pygame.image.load("assets/cops.png")
player1_punch = pygame.transform.scale(player1_punch, (140, 140))

player2_image = pygame.image.load("assets/cryingChild.png")
player2_image = pygame.transform.scale(player2_image, (140, 140))

player2_punch = pygame.image.load("assets/cave.jpeg")
player2_punch = pygame.transform.scale(player2_punch, (140, 140))

class Player:
    def __init__(self, pos, gravity, canJump, player_id):
        self.pos = pos
        self.rect = pygame.Rect(self.pos.x-70, self.pos.y-70, 140, 140)
        self.gravity = gravity
        self.canJump = canJump
        self.player_id = player_id
        self.punching = False
        self.punch_Frame = 0
        self.iframe = 0
        self.health = 1
    
    def update(self, dt):
        self.gravity += 1000 * dt
        self.pos.y += self.gravity * dt
        self.rect = pygame.Rect(self.pos.x-70, self.pos.y-70, 140, 140)
        self.iframe -= 1
        
        if self.punching:
            self.punch_Frame += 1
            
        if self.punch_Frame >= 60:
            self.punching = False
            self.punch_Frame = 0
        
    def input(self, keys, dt):
        
        if self.player_id == "p1":
            if keys[pygame.K_w] and self.canJump:
                self.gravity = -600
                self.canJump = False
            if keys[pygame.K_a]:
                self.pos.x -= 300 * dt
            if keys[pygame.K_d]:
                self.pos.x += 300 * dt
            if keys[pygame.K_q]:
                self.punching = True
            
        
        
        
        if self.player_id == "p2":
            if keys[pygame.K_UP] and self.canJump:
                self.gravity = -600
                self.canJump = False
            if keys[pygame.K_LEFT]:
                self.pos.x -= 300 * dt
            if keys[pygame.K_RIGHT]:
                self.pos.x += 300 * dt
            if keys[pygame.K_RSHIFT]:
                self.punching = True

    def draw(self, screen):
        # punch frame = 60 frames
        if self.player_id == "p1":  
            if self.punching:
                screen.blit(player1_punch, self.rect)
            else:
                screen.blit(player1_image, self.rect)
                
                
                
        if self.player_id == "p2":
            if self.punching:
                screen.blit(player2_punch, self.rect)
            else:
                screen.blit(player2_image, self.rect)
        
        
        
 