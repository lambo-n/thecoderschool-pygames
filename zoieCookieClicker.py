# Example file showing a basic pygame "game loop"
import math

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
cookieX = 640
cookieY = 360
cookieImage = pygame.image.load("assets/cookie.png").convert_alpha()
cookieImage = pygame.transform.scale(cookieImage,(150,150))
cookieRect = cookieImage.get_rect(center=(cookieX, cookieY))
totalCookies = 100000
cps = 0
clickPower = 1
timeAccumulator = 0
cursorCost = 35
grandmaCost = 130
farmCost = 500
minesCost = 1000

# MENU ELEMENTS
backdropRect = pygame.Rect(800,50,450,600)
upgrade1Rect = pygame.Rect(825,90,400,100)
upgrade2Rect = pygame.Rect(825, 235, 400,100)
upgrade3Rect = pygame.Rect(825,380,400,100)
upgrade4Rect = pygame.Rect(825,525, 400,100)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if cookieRect.collidepoint(event.pos):
                totalCookies += clickPower
            
            # cursor
            if upgrade1Rect.collidepoint(event.pos):
                
                # check if player can afford upgrade
                # give player upgrade
                # subtract cost from total cookies
                # increase cost for next upgrade
                if totalCookies >= cursorCost:
                    cps += 1
                    totalCookies -= cursorCost
                    cursorCost *= 1.2
                    cursorCost = int(math.floor(cursorCost))
                    
            # grandma
            if upgrade2Rect.collidepoint(event.pos):
                if totalCookies >= grandmaCost:
                    cps += 5
                    totalCookies -= grandmaCost
                    grandmaCost *= 1.2
                    grandmaCost = int(math.floor(grandmaCost))
                    
            # farm
            if upgrade3Rect.collidepoint(event.pos):
                if totalCookies >= farmCost:
                    cps += 10
                    totalCookies -= farmCost
                    farmCost *= 1.2
                    farmCost = int(math.floor(farmCost))
            
            # mines
            if upgrade4Rect.collidepoint(event.pos):
                if totalCookies >= minesCost:
                    cps += 20
                    totalCookies -= minesCost
                    minesCost *= 1.2
                    minesCost = int(math.floor(minesCost))
                
    # Update the game state
    dt = clock.tick(60) / 1000
    timeAccumulator += dt
    if timeAccumulator >= 1:
        totalCookies += cps
        timeAccumulator -= 1            
                

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((100,200,255))

    # RENDER YOUR GAME HERE
    screen.blit (cookieImage,cookieRect)
    font = pygame.font.SysFont("Georgia",40)
    cookieText = font.render(f"Cookies: {totalCookies}", True, (0,0,0))
    cpsText = font.render(f"CPS: {cps}", True, (0,0,0))
    clickPowerText = font.render(f"Click Power: {clickPower}", True, (0,0,0))

    screen.blit (cookieText, (50,50))
    screen.blit (cpsText, (50,100))
    screen.blit (clickPowerText, (50,150))
    
    # display upgrade costs


    # UPGRADES AND SHOP
    pygame.draw.rect(screen,  (55,0,0), backdropRect)
    pygame.draw.rect(screen, "white", upgrade1Rect)
    pygame.draw.rect(screen, "white", upgrade2Rect)
    pygame.draw.rect(screen, "white", upgrade3Rect)
    pygame.draw.rect(screen, "white", upgrade4Rect)













    # flip() the display to put youn screen
    pygame.display.flip()
      # limits FPS to 60



pygame.quit()
