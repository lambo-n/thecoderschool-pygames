# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 640), pygame.FULL)
clock = pygame.time.Clock()
running = True
rect1 = pygame.Rect(250, 500, 500, 500)

# game loop OR draw()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("light blue")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, "yellow", rect1)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()