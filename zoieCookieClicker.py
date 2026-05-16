# Example file showing a basic pygame "game loop"
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
totalCookies = 0
cps = 1
clickPower = 1
timeAccumulator = 0

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
                

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((100,200,255))

    # RENDER YOUR GAME HERE
    screen.blit (cookieImage,cookieRect)
    font = pygame.font.SysFont("Georgia",40)
    cookieText = font.render(f"Cookies: {totalCookies}", True, (0,0,0))
    screen.blit (cookieText, (50,50))


    # UPGRADES AND SHOP
    pygame.draw.rect(screen,  (55,0,0), backdropRect)
    pygame.draw.rect(screen, "white", upgrade1Rect)
    pygame.draw.rect(screen, "white", upgrade2Rect)
    pygame.draw.rect(screen, "white", upgrade3Rect)
    pygame.draw.rect(screen, "white", upgrade4Rect)













    # flip() the display to put youn screen
    pygame.display.flip()
      # limits FPS to 60

    dt = clock.tick(60) / 1000
    timeAccumulator += dt
    if timeAccumulator >= 1:
        totalCookies += cps
        timeAccumulator -= 1

pygame.quit()
