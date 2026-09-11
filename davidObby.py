# Example file showing a circle moving on screen
import pygame
from davidPlatform import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
canJump = False

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
playerRect = pygame.Rect(player_pos.x - 32, player_pos.y - 32, 64,64)
playerHitbox = pygame.Rect(player_pos.x - 34, player_pos.y - 34, 67 ,67)


playerImage = pygame.image.load("assets/jumpboy.png").convert_alpha()
playerImage = pygame.transform.scale(playerImage, (64, 64))
gravity = 0

# lvl 1 platforms
platform1lvl1 = ObbyPlatform(0,650,1280,100,"blue")
platform2lvl1 = ObbyPlatform(50,500,300,50,"black")
platform3lvl1 = ObbyPlatform(200,325,300,50,"black")
platform4lvl1 = ObbyPlatform(500,200,300,50,"black")
escapeRect1 = Escape(1200,100,50,50,"gold", 100, 600)

lvl1List = [platform1lvl1,platform2lvl1,platform3lvl1,platform4lvl1,escapeRect1]

# lvl 2 platforms
platform1lvl2 = ObbyPlatform(0,650,1280,100,"blue")
platform2lvl2 = ObbyPlatform(400,400,1,1,"black")
platform3lvl2 = ObbyPlatform(200,600,1,1,"black")
platform4lvl2 = ObbyPlatform(700,200,1,1,"black")
escapeRect2 = Escape(900,100,50,50,"gold", 100, 600)




lvl2List = [platform1lvl2, platform2lvl2, platform3lvl2, platform4lvl2,escapeRect2]

# lvl 3 platforms
platform1Lvl3 = ObbyPlatform(40,670,100,230,"blue")
platform2Lvl3 = ObbyPlatform(500,700,30,20,"black")
platform3Lvl3 = ObbyPlatform(700,500,20,20,"black")
platform4Lvl3 = ObbyPlatform(400,300,1,1,"light grey")
platform5Lvl3 = ObbyPlatform(800,200,1,1,"light grey")
escapeRect3 = Escape(900,100,50,50,"gold", 500, 600)
killblock = Killblock(0,900,1280,100,"red")


lvl3List = [platform1Lvl3,platform2Lvl3,platform3Lvl3,platform4Lvl3,platform5Lvl3,escapeRect3,killblock]

#lvl 4 platforms

platform1lvl4 = ObbyPlatform(450,600,300,200,"blue")
platform2lvl4 = ObbyPlatform(450,100,10,900,"black")
platform3lvl4 = ObbyPlatform(900,100,10,900,"black")
teleportplatform1 = Teleporter(800,400,50,50,"red",1000,100)
escapeRect4 = Escape(1100,100,50,50,"gold", 500, 600)
killblock = Killblock(0,900,1280,100,"red")



lvl4List = [platform1lvl4,platform2lvl4,platform3lvl4,teleportplatform1,escapeRect4,killblock]


#lvl 5 platforms

platform1lvl5 = ObbyPlatform(0,650,1280,100,"blue")
platform2lvl5 = ObbyPlatform(850,170,10,10,"black")
killblock = Killblock(600,450,100,50,"red")
teleportplatform2 = Teleporter(150,600,20,20,"white",900,100)
escapeRect5 = Escape(1100,100,50,50,"gold", 500, 600)


lvl5List = [platform1lvl5,teleportplatform2,killblock,platform2lvl5,escapeRect5]


#lvl 6 platforms


platform1lvl6 = ObbyPlatform(600,690,1,2,"blue")
platform2lvl6 = ObbyPlatform(200,500,1,2,"black")
platform3lvl6 = ObbyPlatform(400,500,1,2,"black")
platform4lvl6 = ObbyPlatform(800,100,1,2,"black")
platform5lvl6 = ObbyPlatform(900,600,1,2,"black")


lvl6List = [platform1lvl6,platform2lvl6,platform3lvl6,platform4lvl6,platform5lvl6]



levels = [lvl1List,lvl2List,lvl3List,lvl4List,lvl5List,lvl6List]

currentLvl = 4
currentPlatformList = lvl1List




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
        gravity = -525 * dt
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
    playerHitbox = pygame.Rect(player_pos.x - 34, player_pos.y - 34, 67 ,67)
    
    
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



    



        
    # if playerHitbox.colliderect(killblock.rect) and (currentLvl == 5):
    #     running = False

        


    # PRINT STUFF ON SCREEN
    screen.fill("white")


    # print/move platforms
    currentPlatformList = levels[currentLvl - 1]
    for platform in currentPlatformList:
        pygame.draw.rect(screen, platform.color, platform.rect)
        outcome = platform.update(screen,player_pos,playerHitbox)
        
        if outcome == "kill":
            running = False
            print("You Died")
        elif outcome == "teleport":
            player_pos.x = platform.teleportX
            player_pos.y = platform.teleportY
        elif outcome == "escape":
            currentLvl += 1
            if currentLvl > len(levels):
                running = False
                print("you win")
            player_pos.x = platform.escapeX
            player_pos.y = platform.escapeY


    screen.blit(playerImage, playerRect)
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
