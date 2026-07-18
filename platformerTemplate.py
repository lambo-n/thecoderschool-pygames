# Example file showing a circle moving on screen
import random

import pygame
from platformTemplate import CustomPlatform

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
gravity = 0
canJump = False

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


# xpos, ypos, xwidth, yheight
platformGround = pygame.Rect(0, 600, 1280, 20)
platform1 = CustomPlatform(100, 250, 150, 20, "white")
platform2 = CustomPlatform(400, 450, 150, 20, "white")
platform3 = CustomPlatform(700, 150, 150, 20, "white")
platform4 = CustomPlatform(100, 350, 150, 20, "white")


platformList = [platformGround, platform1.rect, platform2.rect, platform3.rect, platform4.rect]




font = pygame.font.SysFont(None, 40)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
        
        
    player_rect = pygame.Rect(player_pos.x - 20, player_pos.y - 20, 40, 40)
    
   
    
    gravity += 1000 * dt
    player_pos.y += gravity * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and canJump:
        gravity = -600
        canJump = False
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    # Rebuild rect after movement so collisions use updated position
    player_rect = pygame.Rect(player_pos.x - 20, player_pos.y - 20, 40, 40)

    # Platform collisions using minimum overlap (MTV)
    canJump = False
    for platform in platformList:
        if player_rect.colliderect(platform):
            overlap_top    = player_rect.bottom - platform.top
            overlap_bottom = platform.bottom - player_rect.top
            overlap_left   = player_rect.right - platform.left
            overlap_right  = platform.right - player_rect.left
            overlap_y = min(overlap_top, overlap_bottom)
            overlap_x = min(overlap_left, overlap_right)

            if overlap_y <= overlap_x:
                # Vertical collision
                if gravity >= 0 and overlap_top <= overlap_bottom:
                    player_rect.bottom = platform.top
                    gravity = 0
                    canJump = True
                else:
                    player_rect.top = platform.bottom
                    gravity = 0
            else:
                # Horizontal collision
                if overlap_left <= overlap_right:
                    player_rect.right = platform.left
                else:
                    player_rect.left = platform.right
            player_pos.x = player_rect.centerx
            player_pos.y = player_rect.centery

    player_rect.clamp_ip(screen.get_rect())
    player_pos.x = player_rect.centerx
    player_pos.y = player_rect.centery
    
    screen.fill("black")

    for platform in platformList:
        pygame.draw.rect(screen, "white", platform)
    
    pygame.draw.rect(screen, "gold", player_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()