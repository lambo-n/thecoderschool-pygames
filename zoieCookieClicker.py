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
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if cookieRect.collidepoint(event.pos):
                totalCookies += 1
                print (totalCookies)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    screen.blit (cookieImage,cookieRect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
