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

newEnemy = Enemy(pygame.Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)) , "normal")
enemyList.append(newEnemy)

health = 100
gravity = 0
canJump = False

font = pygame.font.SysFont(None, 40)
while running == True:
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

    textHealth = font.render(str(health), True, (0, 0, 255))
    screen.blit(textHealth, (50, 600))
        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and canJump:
        gravity = -600
        canJump = False
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        
    screen.blit(playerImage, player_pos)
        
    for bullet in bulletList[:]:
        bullet.update(dt)
        bullet.draw(screen)
        if not (0 <= bullet.pos.x <= WIDTH and 0 <= bullet.pos.y <= HEIGHT):
            bulletList.remove(bullet)
            
        for enemy in enemyList[:]:
            enemyRect = enemy.get_rect()
            
            if enemyRect.collidepoint(bullet.pos) and bullet:
                enemy.health -= 5
                bulletList.remove(bullet)
                
            if enemy.health <= 0 and enemy:
                enemyList.remove(enemy)
                
            
            
    for enemy in enemyList[:]:
        enemyRect = enemy.get_rect()
        
        if enemyRect.collidepoint(player_pos):
            health -= enemy.strength
            
        enemy.update(player_pos, dt)
        enemy.draw(screen)
        
        
    if health <= 0:
        running = False
    
  
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()