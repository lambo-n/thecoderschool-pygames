# Example file showing a circle moving on screen
import random
from bullet import *
import pygame
from custom_platform import *
from levels import *
from enemies import*
ENEMYBULLET_COOLDOWN = 1
PLAYERBULLET_COOLDOWN = .2
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
gravity = 0
canJump = False
bulletcooldown = ENEMYBULLET_COOLDOWN
playerHealth = 20
player_pos = pygame.Vector2(300, 600)
playerbulletcooldown = PLAYERBULLET_COOLDOWN
PlayerBulletDamage = 6

# xpos, ypos, xwidth, yheight


currentLevel = 1
platformList = levels[currentLevel-1]()
gameWOn = False


Enemybulletlist = []
playerbulletlist = []
enemyList = enemies[currentLevel - 1]()

font = pygame.font.SysFont(None, 40)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # bullet loop
    bulletcooldown -= dt
    playerbulletcooldown -= dt

    if bulletcooldown <0:
        bulletcooldown = ENEMYBULLET_COOLDOWN
        randomPos = pygame.Vector2(random.randint(0, 1280), -10)
        newBullet = Bullet(randomPos, player_pos)
        Enemybulletlist.append(newBullet)


        
          
        
    
    
   
    
    gravity += 1000 * dt
    player_pos.y += gravity * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and canJump:
        gravity = -575
        canJump = False
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_e] and playerbulletcooldown < 0: 
        playerbulletcooldown = PLAYERBULLET_COOLDOWN
        currentPosition = player_pos.copy()
        newPlayerbullet = Bullet(currentPosition, (currentPosition.x+50, currentPosition.y))
        playerbulletlist.append(newPlayerbullet)


    # Rebuild rect after movement so collisions use updated position
    player_rect = pygame.Rect(player_pos.x - 20, player_pos.y - 20, 40, 40)

    # Platform collisions using minimum overlap (MTV)
    canJump = False
    for platform in platformList:
        if isinstance(platform, EscapeDoor):
            continue
        if player_rect.colliderect(platform):
            overlap_top    = player_rect.bottom - platform.top
            overlap_bottom = platform.bottom - player_rect.top
            overlap_left   = player_rect.right - platform.left
            overlap_right  = platform.right - player_rect.left
            overlap_y = min(overlap_top, overlap_bottom)
            overlap_x = min(overlap_left, overlap_right)

            if overlap_y <= overlap_x:
                # Vertical collision
                if gravity >= 0 and overlap_top <= overlap_bottom:
                    player_rect.bottom = platform.top
                    gravity = 0
                    canJump = True
                else:
                    player_rect.top = platform.bottom
                    gravity = 0
            else:
                # Horizontal collision
                if overlap_left <= overlap_right:
                    player_rect.right = platform.left
                else:
                    player_rect.left = platform.right
            player_pos.x = player_rect.centerx
            player_pos.y = player_rect.centery

    player_rect.clamp_ip(screen.get_rect())
    player_pos.x = player_rect.centerx
    player_pos.y = player_rect.centery
    
    screen.fill("black")

    for platform in platformList:
        outcome = platform.update(screen, player_rect)

        if outcome == "escape":
            currentLevel += 1
            player_pos.x = platform.spawnx
            player_pos.y = platform.spawny
            if currentLevel <= len(levels):
                platformList = levels[currentLevel-1]()
                enemyList = enemies[currentLevel-1]()
                gravity = 0
                Enemybulletlist.clear()
            else:
                running = False
            break

    for enemy in enemyList:
        enemy.update(dt)
        enemy.draw(screen)
        if player_rect.colliderect(enemy.rect):
            playerHealth -= 5
            enemyList.remove(enemy)
        if enemy.health <= 0:
            enemyList.remove(enemy)


    for bullet in playerbulletlist:
        bullet.update(dt)
        bullet.draw(screen,"blue")
        playerbulletrect = pygame.Rect( bullet.pos.x - 10, bullet.pos.y - 10 , 20, 20)

        if bullet.pos.x > 1280 or bullet.pos.x < 0:
            print("PlayerBulletGone")
            playerbulletlist.remove(bullet) 

        for enemy in enemyList:
            if playerbulletrect.colliderect(enemy.rect):
                enemy.health -= 6
                playerbulletlist.remove(bullet)

        





    for bullet in Enemybulletlist:
        bullet.update(dt)
        bullet.draw(screen, "red")
        bullet_rect = pygame.Rect( bullet.pos.x - 10, bullet.pos.y - 10 , 20, 20 )
        if bullet_rect.colliderect(player_rect):
            playerHealth -= 1
            Enemybulletlist.remove(bullet)
        if bullet.pos.x >= 1280:
            Enemybulletlist.remove(bullet)
        if bullet.pos.y >= 720:
            Enemybulletlist.remove(bullet)




    if playerHealth <= 0:
        running = False
    
    pygame.draw.rect(screen, "gold", player_rect)


    pygame.draw.rect(screen,"red", (player_pos.x- 40 , player_pos.y- 60, 80, 10 ))
    pygame.draw.rect(screen,"green", (player_pos.x- 40 , player_pos.y- 60, 80/20 * playerHealth, 10 ))
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
