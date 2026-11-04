# Example file showing a circle moving on screen
import random
from bullet import *
import pygame
from custom_platform import *
from levels import *
from enemies import*
from powers import*
ENEMYBULLET_COOLDOWN = 1
PLAYERBULLET_COOLDOWN = .2

# Player physics
PLAYER_SIZE = 40
HALF = PLAYER_SIZE / 2

GRAVITY = 1000
TERMINAL_VELOCITY = 1600
HEAD_BUMP_SPEED = 120    # downward speed after hitting a ceiling, so you bounce off instead of sticking
MAX_PHYSICS_DT = 1 / 30    # a lag spike can't fling the player through a platform
EPSILON = 0.001            # touching edges (standing on a floor, leaning on a wall) don't count as overlap


# Collisions are resolved one axis at a time (x, then y), and only against
# platform faces the player actually crossed this frame.  That means a wall is
# always a wall, a floor is always a floor, and nothing snaps you backwards.

def player_box(pos):
    return pos.x - HALF, pos.y - HALF, pos.x + HALF, pos.y + HALF


def push_out(pos, solids):
    """Move the player out of any platform they are already inside (bad spawn, level change)."""
    for r in solids:
        left, top, right, bottom = player_box(pos)
        if left >= r.right - EPSILON or right <= r.left + EPSILON or top >= r.bottom - EPSILON or bottom <= r.top + EPSILON:
            continue
        # Smallest push wins; ties favour standing on top
        pushes = [(bottom - r.top, 0, -1), (r.bottom - top, 0, 1), (right - r.left, -1, 0), (r.right - left, 1, 0)]
        distance, sx, sy = min(pushes, key=lambda p: p[0])
        pos.x += sx * distance
        pos.y += sy * distance


def move_x(pos, dx, solids, bounds):
    """Move sideways, stopping at the first wall crossed.  Returns True if blocked."""
    left, top, right, bottom = player_box(pos)
    new_x = pos.x + dx
    blocked = False
    for r in solids:
        if top >= r.bottom - EPSILON or bottom <= r.top + EPSILON:
            continue  # platform is above or below us, not beside us
        if dx > 0 and right <= r.left + EPSILON and new_x + HALF > r.left:
            new_x = r.left - HALF
            blocked = True
        elif dx < 0 and left >= r.right - EPSILON and new_x - HALF < r.right:
            new_x = r.right + HALF
            blocked = True
    if new_x - HALF < bounds.left:
        new_x = bounds.left + HALF
        blocked = True
    elif new_x + HALF > bounds.right:
        new_x = bounds.right - HALF
        blocked = True
    pos.x = new_x
    return blocked


def move_y(pos, dy, solids, bounds):
    """Move vertically.  Returns "ground" if we landed, "ceiling" if we hit our head, else None."""
    left, top, right, bottom = player_box(pos)
    new_y = pos.y + dy
    hit = None
    for r in solids:
        if left >= r.right - EPSILON or right <= r.left + EPSILON:
            continue  # platform is beside us, not above or below
        if dy >= 0 and bottom <= r.top + EPSILON and new_y + HALF > r.top - EPSILON:
            new_y = r.top - HALF
            hit = "ground"
        elif dy < 0 and top >= r.bottom - EPSILON and new_y - HALF < r.bottom:
            new_y = r.bottom + HALF
            hit = "ceiling"
    if new_y + HALF >= bounds.bottom:
        new_y = bounds.bottom - HALF
        hit = "ground"
    elif new_y - HALF < bounds.top:
        new_y = bounds.top + HALF
        hit = "ceiling"
    pos.y = new_y
    return hit


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
vel_x = 0
vel_y = 0
canJump = False
bulletcooldown = ENEMYBULLET_COOLDOWN
playerHealth = 10
player_pos = pygame.Vector2(300, 600) #300, 600
playerbulletcooldown = PLAYERBULLET_COOLDOWN
PlayerBulletDamage = 6
currentPosition = player_pos.copy()
aim = "left"
speedTimer = 0
jumpTimer = 0
invinTimer = 0
pierceTimer = 0
currentPower = None
pierce = False
move_speed = 375 # 375
jump_speed = 575 #575
invincibility = False
lives = 1
# testPower1 = PowerUp(400,400, "life")
# testPower2 = PowerUp(400,500, "speed")
# testPower3 = PowerUp(400,600, "jumpboost")
# testPower4 = PowerUp(400,100, "health")
# testPower5 = PowerUp(400,300, "immunity")
# testPower6 = PowerUp(400,200, "pierce")




# xpos, ypos, xwidth, yheight


currentLevel = 1
platformList = levels[currentLevel-1]()
gameWOn = False

powerList = powers[currentLevel - 1]()
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


        
          
        
    
    
   
    
    keys = pygame.key.get_pressed()
    vel_x = (keys[pygame.K_d] - keys[pygame.K_a]) * move_speed
    
    if keys[pygame.K_w] and canJump:
        vel_y = -jump_speed
        canJump = False
    if keys[pygame.K_d]:
        aim = "right"
        
    if keys[pygame.K_a]:
        aim = "left"

    if keys[pygame.K_e] and playerbulletcooldown < 0: 
        playerbulletcooldown = PLAYERBULLET_COOLDOWN
        currentPosition = player_pos.copy()

        if aim == "right":
            newPlayerbullet = Bullet(currentPosition, (currentPosition.x+50, currentPosition.y))


        if aim == "left":
            newPlayerbullet = Bullet(currentPosition, (currentPosition.x-50, currentPosition.y))
        
       
        playerbulletlist.append(newPlayerbullet)

    # Player physics: gravity, then move and collide one axis at a time
    physics_dt = min(dt, MAX_PHYSICS_DT)
    solids = [platform.rect for platform in platformList if not isinstance(platform, EscapeDoor)]
    bounds = screen.get_rect()
    push_out(player_pos, solids)

    vel_y = min(vel_y + GRAVITY * physics_dt, TERMINAL_VELOCITY)

    if move_x(player_pos, vel_x * physics_dt, solids, bounds):
        vel_x = 0

    canJump = False
    hit = move_y(player_pos, vel_y * physics_dt, solids, bounds)
    if hit == "ground":
        vel_y = 0
        canJump = True
    elif hit == "ceiling":
        vel_y = HEAD_BUMP_SPEED

    player_rect = pygame.Rect(round(player_pos.x - HALF), round(player_pos.y - HALF), PLAYER_SIZE, PLAYER_SIZE)

    screen.fill("black")

    # testPower1.draw(screen)
    # testPower2.draw(screen)
    # testPower3.draw(screen)
    # testPower4.draw(screen)
    # testPower5.draw(screen)
    # testPower6.draw(screen)



    

    for platform in platformList:
        outcome = platform.update(screen, player_rect)

        if outcome == "escape":
            playerHealth = 10
            currentLevel += 1
            player_pos.x = platform.spawnx
            player_pos.y = platform.spawny
            if currentLevel <= len(levels):
                platformList = levels[currentLevel-1]()
                enemyList = enemies[currentLevel-1]()
                powerList = powers[currentLevel - 1]()
                vel_y = 0
                Enemybulletlist.clear()
            else:
                running = False
            break


    for power in powerList:
            power.draw(screen)
            if player_rect.colliderect(power.rect):
                powerList.remove(power)

                if power.type == "speed":
                    move_speed = 600
                    speedTimer = 600
                if power.type == "health":
                    playerHealth = 10  
                if power.type == "jumpboost":
                    jump_speed = 700
                    jumpTimer = 600
                if power.type == "invincibility":
                    invincibility = True
                    invinTimer = 600
                    print("PICK UP THE INVINCIBILITY")
                if power.type == "pierce":
                    pierce = True
                    pierceTimer = 600
                if power.type == "life":
                    lives += 1


    if speedTimer <= 0:
        move_speed = 375
    else:
        speedTimer -= 1

    if jumpTimer <= 0:
        jump_speed_speed = 375
    else:
        jumpTimer -= 1
        
    if invinTimer <= 0:
        invincibility = False
    else:
        invinTimer -= 1

    if pierceTimer <= 0:
        pierce = False
    else:
        pierceTimer -= 1

    for enemy in enemyList:
        enemy.update(dt)
        enemy.draw(screen)
        if player_rect.colliderect(enemy.rect):
            if invincibility == False:
                playerHealth -= 5
            else:
                print("should be invincible")
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

        for platform in platformList:
            if playerbulletrect.colliderect(platform.rect) and pierce == False:
                playerbulletlist.remove(bullet)





    for bullet in Enemybulletlist:
        bullet.update(dt)
        bullet.draw(screen, "red")
        bullet_rect = pygame.Rect( bullet.pos.x - 10, bullet.pos.y - 10 , 20, 20 )
        if bullet_rect.colliderect(player_rect):
            if invincibility == False:
                playerHealth -= 1

            Enemybulletlist.remove(bullet)
        if bullet.pos.x >= 1280:
            Enemybulletlist.remove(bullet)
        if bullet.pos.y >= 720:
            Enemybulletlist.remove(bullet)


    if playerHealth <= 0:
        lives -= 1
        playerHealth = 10
        invincibility = True
        invinTimer = 100


    if lives <= 0:
        running = False
    
    pygame.draw.rect(screen, "gold", player_rect)


    pygame.draw.rect(screen,"red", (player_pos.x- 40 , player_pos.y- 60, 80, 10 ))
    if invincibility == True:
        bar_color = "yellow"
    else:
        bar_color = "green"
    pygame.draw.rect(screen, bar_color, (player_pos.x- 40 , player_pos.y- 60, 80/10 * playerHealth, 10 ))
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()