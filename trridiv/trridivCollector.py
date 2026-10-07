# Example file showing a circle moving on screen
from random import *

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
square_pos = pygame.Vector2(1000, 300)

# print(player_pos.x)
# print(player_pos.y)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    


    playerHitbox = pygame.Rect(player_pos.x-20, player_pos.y-20, 40, 40)
    pygame.draw.circle(screen, "red", player_pos, 40)
    
    pygame.draw.rect(screen, "blue", (square_pos.x, square_pos.y, 50, 50))
    
    # if playerHitbox.colliderect(rectValue):
    #     square_pos.x = 700
    #     square_pos.y = 400

    print(square_pos)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()