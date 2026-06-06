# Example file showing a basic pygame "game loop"
import math

import pygame

def formatNumber(number):
    suffix = ["", "K", "M", "B", "T", "Qd", "Qn", "Sx", "Sp", "O", "N", "D"]
    index = 0
    
    #1,000,000
    #1,000
    #1
    while number >= 1000 and index < len(suffix) - 1:
        number /= 1000
        index += 1
    if index == 0:
        # small numbers stay as whole numbers
        return f"{int(number)}"
    # show one decimal place, e.g. 1.5K
    return f"{number:.1f}{suffix[index]}"


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
cookieX = 640
cookieY = 360
cookieImage = pygame.image.load("assets/cookie.png").convert_alpha()
cookieImage = pygame.transform.scale(cookieImage,(300,300))
cookieRect = cookieImage.get_rect(center=(cookieX, cookieY))
totalCookies = 0
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

secondShopRect = pygame.Rect(50, 235, 400, 400)
tool1Rect = pygame.Rect(75, 260, 100, 100)
tool2Rect = pygame.Rect(200, 260, 100, 100)
tool3Rect = pygame.Rect(325, 260, 100, 100)
tool4Rect = pygame.Rect(75, 385, 100, 100)
tool5Rect = pygame.Rect(200, 385, 100, 100)
tool6Rect = pygame.Rect(325, 385, 100, 100)
tool7Rect = pygame.Rect(75, 510, 100, 100)
tool8Rect = pygame.Rect(200, 510, 100, 100)
tool9Rect = pygame.Rect(325, 510, 100, 100)







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
    cookieText = font.render(f"Cookies: {formatNumber(totalCookies)}", True, (0,0,0))
    cpsText = font.render(f"CPS: {cps}", True, (0,0,0))
    clickPowerText = font.render(f"Click Power: {clickPower}", True, (0,0,0))

    screen.blit (cookieText, (50,50))
    screen.blit (cpsText, (50,100))
    screen.blit (clickPowerText, (50,150))
    


    # UPGRADES AND SHOP
    pygame.draw.rect(screen,  (55,0,0), backdropRect)
    pygame.draw.rect(screen, "white", upgrade1Rect)
    pygame.draw.rect(screen, "white", upgrade2Rect)
    pygame.draw.rect(screen, "white", upgrade3Rect)
    pygame.draw.rect(screen, "white", upgrade4Rect)

    # secondary shop
    pygame.draw.rect(screen, (0, 55, 0), secondShopRect)
    
    pygame.draw.rect(screen, "white", tool1Rect)
    pygame.draw.rect(screen, "white", tool2Rect)
    pygame.draw.rect(screen, "white", tool3Rect)
    pygame.draw.rect(screen, "white", tool4Rect)
    pygame.draw.rect(screen, "white", tool5Rect)
    pygame.draw.rect(screen, "white", tool6Rect)
    pygame.draw.rect(screen, "white", tool7Rect)
    pygame.draw.rect(screen, "white", tool8Rect)
    pygame.draw.rect(screen, "white", tool9Rect)


    # display upgrade costs
    upgrade1line1 = font.render(f"Cursor: ${formatNumber(cursorCost)}, and cps", True, "black")
    upgrade1line2 = font.render("increased by 1.", True, "black")
    screen.blit(upgrade1line1, (830, 100))
    screen.blit(upgrade1line2, (830, 130))

    upgrade2line1 = font.render(f"Grandma: ${formatNumber(grandmaCost)}, ", True, "black")
    upgrade2line2 = font.render("and cps increases by 5. ", True, "black")
    screen.blit(upgrade2line1, (830, 245))
    screen.blit(upgrade2line2, (830, 275))

    upgrade3line1 = font.render(f"Farm: ${formatNumber(farmCost)}, ", True, "black")
    upgrade3line2 = font.render("and cps increases by 10. ", True, "black")
    screen.blit(upgrade3line1, (830, 390))
    screen.blit(upgrade3line2, (830, 420))

    upgrade4line1 = font.render(f"Mines: ${formatNumber(minesCost)}, ", True, "black")
    upgrade4line2 = font.render("and cps increases by 20. ", True, "black")
    screen.blit(upgrade4line1, (830, 535))
    screen.blit(upgrade4line2, (830, 565))


    # flip() the display to put youn screen
    pygame.display.flip()
      # limits FPS to 60



pygame.quit()



