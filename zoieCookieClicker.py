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
# Each upgrade is a dictionary. Add more entries here and the menu
# automatically becomes scrollable.
upgrades = [
    {"name": "Cursor",  "cost": 35,   "cps": 1,  "desc": "increases cps by 1."},
    {"name": "Grandma", "cost": 130,  "cps": 5,  "desc": "increases cps by 5."},
    {"name": "Farm",    "cost": 500,  "cps": 10, "desc": "increases cps by 10."},
    {"name": "Mines",   "cost": 1000, "cps": 20, "desc": "increases cps by 20."},
    {"name": "Factory", "cost": 5000, "cps": 50, "desc": "increases cps by 50."},
    {"name": "Bank",    "cost": 20000,"cps": 100,"desc": "increases cps by 100."},
]

# MENU ELEMENTS
backdropRect = pygame.Rect(800,50,450,600)

# Scrollable upgrade-menu layout
itemX = 825          # left edge of each upgrade box
itemWidth = 400      # width of each upgrade box
itemHeight = 100     # height of each upgrade box
itemSpacing = 145    # vertical distance between the top of one box and the next
menuTop = 90         # y of the first box when not scrolled

scrollOffset = 0
# how far down the full list of upgrades extends
contentHeight = len(upgrades) * itemSpacing
# how much of the menu is actually visible inside the backdrop
visibleHeight = backdropRect.bottom - menuTop
# the most we ever need to scroll (0 if everything already fits)
maxScroll = max(0, contentHeight - visibleHeight)

secondShopRect = pygame.Rect(50, 235, 400, 400)
tool1Rect = pygame.Rect(75, 260, 100, 100)
tool2Rect = pygame.Rect(200, 260, 100, 100)
tool3Rect = pygame.Rect(325, 260, 100, 100)





while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # scroll the upgrade menu with the mouse wheel
        if event.type == pygame.MOUSEWHEEL:
            scrollOffset -= event.y * 30
            scrollOffset = max(0, min(scrollOffset, maxScroll))

        if event.type == pygame.MOUSEBUTTONUP:
            if cookieRect.collidepoint(event.pos):
                totalCookies += clickPower

            # only handle upgrade clicks that land inside the menu area,
            # so we don't buy through a box that's scrolled out of view
            if backdropRect.collidepoint(event.pos):
                for index, upgrade in enumerate(upgrades):
                    itemRect = pygame.Rect(itemX,
                                           menuTop + index * itemSpacing - scrollOffset,
                                           itemWidth, itemHeight)
                    if itemRect.collidepoint(event.pos):
                        # check if player can afford it, then buy it
                        if totalCookies >= upgrade["cost"]:
                            cps += upgrade["cps"]
                            totalCookies -= upgrade["cost"]
                            upgrade["cost"] = int(math.floor(upgrade["cost"] * 1.2))
                
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

    # Only draw inside the backdrop, so scrolled boxes get clipped at the edges
    screen.set_clip(backdropRect)
    for index, upgrade in enumerate(upgrades):
        itemRect = pygame.Rect(itemX,
                               menuTop + index * itemSpacing - scrollOffset,
                               itemWidth, itemHeight)
        pygame.draw.rect(screen, "white", itemRect)
        line1 = font.render(f'{upgrade["name"]}: ${formatNumber(upgrade["cost"])}', True, "black")
        line2 = font.render(upgrade["desc"], True, "black")
        screen.blit(line1, (itemRect.x + 5, itemRect.y + 10))
        screen.blit(line2, (itemRect.x + 5, itemRect.y + 50))
    screen.set_clip(None)

    # secondary shop
    pygame.draw.rect(screen, (0, 55, 0), secondShopRect)
    pygame.draw.rect(screen, "white", tool1Rect)
    pygame.draw.rect(screen, "white", tool2Rect)
    pygame.draw.rect(screen, "white", tool3Rect)


    # flip() the display to put youn screen
    pygame.display.flip()
      # limits FPS to 60



pygame.quit()



