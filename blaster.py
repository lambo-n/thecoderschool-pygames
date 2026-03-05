# Example file showing a circle moving on screen
import pygame
import random
from bullet import *
from enemy import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)

playerImage = pygame.image.load("assets/cowboyReady.png").convert_alpha()
playerImage = pygame.transform.scale(playerImage, (80, 80))

bulletList = []
enemyList = []

enemyImage = pygame.image.load("assets/digdug.png").convert_alpha()
enemyImage = pygame.transform.scale(enemyImage, (50, 50))
newEnemy = Enemy(pygame.Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)), enemyImage)
enemyList.append(newEnemy)

gravity = 0
canJump = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
            copyPos = player_pos.copy()
            bulletList.append(Bullet((copyPos.x + 40, copyPos.y + 40), mouse_pos))

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")  
    
    player_pos.y += gravity * dt
    
    if player_pos.y < HEIGHT - 160:
        gravity += 1000 * dt
        canJump = False
    else:
        gravity = 0
        canJump = True


        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and canJump:
        gravity = -600
        canJump = False
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        
    for bullet in bulletList[:]:
        bullet.update(dt)
        bullet.draw(screen)
        if not (0 <= bullet.pos.x <= WIDTH and 0 <= bullet.pos.y <= HEIGHT):
            bulletList.remove(bullet)
            
    for enemy in enemyList[:]:
        enemy.update(player_pos, dt)
        enemy.draw(screen)
        
    
    screen.blit(playerImage, player_pos)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()