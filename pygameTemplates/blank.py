# Example file showing a circle moving on screen
import pygame
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


cookieimage = pygame.image.load(ASSETS / "cookie.png").convert_alpha()
cookieimage = pygame.transform.scale(cookieimage, (100, 120))

cookierect = pygame.Rect(400, 400, 100, 120)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    screen.blit(cookieimage, cookierect)

 

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000




pygame.time.wait(3000)
pygame.quit()