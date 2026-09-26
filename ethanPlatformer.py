# Example file showing a circle moving on screen
import random
from ethanBullet import *
import pygame
from ethanPlatform import *
from ethanLevels import *
from ethanEnemies import*
ENEMYBULLET_COOLDOWN = 1
PLAYERBULLET_COOLDOWN = .2

# Player physics
PLAYER_SIZE = 40
HALF = PLAYER_SIZE / 2
MOVE_SPEED = 300
JUMP_SPEED = 575
GRAVITY = 1000
TERMINAL_VELOCITY = 1600
HEAD_BUMP_SPEED = 120      # downward speed after hitting a ceiling, so you bounce off instead of sticking
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


        
          
        
    
    
   
    
    keys = pygame.key.get_pressed()
    vel_x = (keys[pygame.K_d] - keys[pygame.K_a]) * MOVE_SPEED
    if keys[pygame.K_w] and canJump:
        vel_y = -JUMP_SPEED
        canJump = False
    if keys[pygame.K_e] and playerbulletcooldown < 0: 
        playerbulletcooldown = PLAYERBULLET_COOLDOWN
        currentPosition = player_pos.copy()
        newPlayerbullet = Bullet(currentPosition, (currentPosition.x+50, currentPosition.y))
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

    for platform in platformList:
        outcome = platform.update(screen, player_rect)

        if outcome == "escape":
            currentLevel += 1
            player_pos.x = platform.spawnx
            player_pos.y = platform.spawny
            if currentLevel <= len(levels):
                platformList = levels[currentLevel-1]()
                enemyList = enemies[currentLevel-1]()
                vel_y = 0
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
