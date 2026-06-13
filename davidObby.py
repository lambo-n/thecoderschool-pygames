# Example file showing a circle moving on screen
import pygame
from davidPlatform import ObbyPlatform

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
canJump = False

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
playerRect = pygame.Rect(player_pos.x - 32, player_pos.y - 32, 64,64)

playerImage = pygame.image.load("assets/blasterboy.png").convert_alpha()
playerImage = pygame.transform.scale(playerImage, (64, 64))
gravity = 0

# LEVEL 1
platform1lvl1 = ObbyPlatform(0,650,1280,100,"blue")
platform2lvl1 = ObbyPlatform(50,500,300,50,"black")
platform3lvl1 = ObbyPlatform(200,325,300,50,"black")
platform4lvl1 = ObbyPlatform(500,200,300,50,"black")

lvl1List = [platform1lvl1, platform2lvl1, platform3lvl1, platform4lvl1]

# LEVEL 2
platform1lvl2 = ObbyPlatform(0,650,1280,100,"blue")
platform2lvl2 = ObbyPlatform(50,500,300,50,"black")
platform3lvl2 = ObbyPlatform(200,325,300,50,"black")
platform4lvl2 = ObbyPlatform(500,200,300,50,"black")


lvl2List = [platform1lvl2, platform2lvl2, platform3lvl2, platform4lvl2]



levels = [lvl1List, lvl2List]

currentPlatformList = lvl2List

currentLevel = 1


escapeRect = pygame.Rect(1000,100,50,50)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # PLAYER MOVEMENT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and canJump == True:
        player_pos.y -= 20
        gravity = -600 * dt
        canJump = False
    if keys[pygame.K_s]:
        pass
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        
        
    # GRAVITY PHYSICS
    gravity += 12 * dt
    player_pos.y += gravity
    

    # UPDATE PLAYER POSITION
    playerRect = pygame.Rect(player_pos.x - 32, player_pos.y - 32, 64,64)
    

     #PLATFORM PHYSICS
    currentPlatformList = levels[currentLevel - 1]
    canJump = False
    for platform in currentPlatformList:
        if playerRect.colliderect(platform):
            overlap_top = playerRect.bottom - platform.top
            overlap_bottom = platform.bottom - playerRect.top
            overlap_left = playerRect.right - platform.left
            overlap_right = platform.right - playerRect.left
            overlap_y = min(overlap_top, overlap_bottom)
            overlap_x = min(overlap_left, overlap_right)

            if overlap_y <= overlap_x:
                if gravity >= 0 and overlap_top <= overlap_bottom:
                    playerRect.bottom = platform.top
                    gravity = 0
        
                    canJump = True
                else:
                    playerRect.top = platform.bottom
                    gravity = 0 
            else:
                if overlap_left <= overlap_right:
                    playerRect.right = platform.left
                else:
                    playerRect.left = platform.right
            player_pos.x = playerRect.centerx
            player_pos.y = playerRect.centery
            
    
    # DRAW THINGS ON  SCREEN
    screen.fill("white")
        
    currentPlatformList = levels[currentLevel - 1]
    for platform in currentPlatformList:
        platform.update(screen)
        
        
    pygame.draw.rect(screen,"gold",escapeRect)

    screen.blit(playerImage,playerRect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
