# Example file showing a circle moving on screen
import random

import pygame
from platformTemplate import *
from rayanPlayer import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((920, 720))
clock = pygame.time.Clock()
running = True
dt = 0
gravity1 = 0
canJump = False
playerList = []

player1_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() / 2 + 200, screen.get_height() / 2)



# xpos, ypos, xwidth, yheight
platformGround = CustomPlatform(0, 600, 920, 100, "white")
platform1 = CustomPlatform(50, 250, 180, 20, "white")
platform2 = CustomPlatform(400, 400, 180, 20, "white")
platform3 = CustomPlatform(700, 250, 180, 20, "white")


platformList = [platformGround, platform1, platform2, platform3]



player1 = Player(player1_pos, 0, canJump, "p1")
player2 = Player(player2_pos,  0, canJump, "p2")

playerList = [player1, player2]

font = pygame.font.SysFont("meslolgldznerdfontmono", 40)
avail = pygame.font.get_fonts()
print(f"{avail}\n")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
        
        
    
    keys = pygame.key.get_pressed()
    for player in playerList:
        player.input(keys, dt)
        player.update(dt)



    # Platform collisions using minimum overlap (MTV)
    canJump = False
    for platform in platformList:
        for player in playerList:
            if player.rect.colliderect(platform):
                overlap_top    = player.rect.bottom - platform.top
                overlap_bottom = platform.bottom - player.rect.top
                overlap_left   = player.rect.right - platform.left
                overlap_right  = platform.right - player.rect.left
                overlap_y = min(overlap_top, overlap_bottom)
                overlap_x = min(overlap_left, overlap_right)

                if overlap_y <= overlap_x:
                    # Vertical collision
                    if overlap_top <= overlap_bottom:
                        # Landing on top: only if not moving upward
                        if player.gravity >= 0:
                            player.rect.bottom = platform.top
                            player.gravity = 0
                            player.canJump = True
                    else:
                        # Head bump: only if actually moving upward
                        if player.gravity < 0:
                            player.rect.top = platform.bottom
                            player.gravity = 0
                else:
                    # Horizontal collision
                    if overlap_left <= overlap_right:
                        player.rect.right = platform.left
                    else:
                        player.rect.left = platform.right
                player.pos.x = player.rect.centerx
                player.pos.y = player.rect.centery
    
    screen.fill("black")

    for platform in platformList:
        platform.update(screen)
    
    for player in playerList:
        player.draw(screen)
        
        if player.punching:
            if player.player_id == "p1" and player.rect.colliderect(player2.rect) and player2.iframe <= 0:
                player2.iframe = 60
                print("Player 1 hit Player 2!")
                player2.health -= 1
                
            if player.player_id == "p2" and player.rect.colliderect(player1.rect) and player1.iframe <= 0:
                player1.iframe = 60
                print("Player 2 hit Player 1!")
                player1.health -= 1

        if player.health <= 0:
            if player.player_id == "p1":
                screen.fill("black")
                
                text_surface = font.render("Player 2 Wins!", True, "white")
                text_rect = text_surface.get_rect(center=(460, 360))
                screen.blit(text_surface, text_rect)
                
                break
            elif player.player_id == "p2":
                screen.fill("white")
                
                text_surface = font.render("Player 1 Wins!", True, "black")
                text_rect = text_surface.get_rect(center=(460, 360))
                screen.blit(text_surface, text_rect)
                
                break

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()