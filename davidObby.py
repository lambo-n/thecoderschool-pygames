# Example file showing a circle moving on screen
import pygame
from obby_platform import ObbyPlatform

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
canJump = False

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
playerRect = pygame.Rect(player_pos.x - 32, player_pos.y - 32, 32,32)

playerImage = pygame.image.load("assets/jumpboy.png").convert_alpha()
playerImage = pygame.transform.scale(playerImage, (32, 32))
gravity = 0

# lvl 1 platforms
platform1lvl1 = ObbyPlatform(0,650,1280,100,"blue")
platform2lvl1 = ObbyPlatform(50,500,300,50,"black")
platform3lvl1 = ObbyPlatform(200,325,300,50,"black")
platform4lvl1 = ObbyPlatform(500,200,300,50,"black")

lvl1List = [platform1lvl1,platform2lvl1,platform3lvl1,platform4lvl1]

# lvl 2 platforms
platform1lvl2 = ObbyPlatform(0,650,1280,100,"blue")
platform2lvl2 = ObbyPlatform(400,400,1,1,"black")
platform3lvl2 = ObbyPlatform(200,600,1,1,"black")
platform4lvl2 = ObbyPlatform(700,200,1,1,"black")


lvl2List = [platform1lvl2, platform2lvl2, platform3lvl2, platform4lvl2]


levels = [lvl1List,lvl2List]


currentLvl = 2
currentPlatformList = lvl1List

escapeRect = pygame.Rect(1000,100,50,50)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # MOVEMENT
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


    # GRAVITY
    gravity += 12 * dt
    player_pos.y += gravity
    
    
    # update player hitbox
    playerRect = pygame.Rect(player_pos.x - 32, player_pos.y - 32, 64,64)


    # COLLISION CHECKS
    # platform physics
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


    # door collision check
    if escapeRect.colliderect(playerRect):
        gravity = 0
        player_pos.x = 100
        player_pos.y = 600
        currentLvl += 1



    # PRINT STUFF ON SCREEN
    screen.fill("white")


    # print/move platforms
    currentPlatformList = levels[currentLvl - 1]
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
