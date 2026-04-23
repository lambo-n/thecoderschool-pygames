import pygame
from enemy import Enemy
from boltsProjectile import Projectile
import random

# stationary platforms, player in top left
# enemies are at the bottom shooting projectiles up
# player can drop projectiles on enemies down below



pygame.init()
screen = pygame.display.set_mode((600, 900))
clock = pygame.time.Clock()
running = True
dt = 1 / 60

player_pos = pygame.Vector2(10, 10)

playerSprite = pygame.image.load("assets/digdug.png").convert_alpha()
playerSprite = pygame.transform.scale(playerSprite, (80, 80))



backgroundImage = pygame.image.load("assets/flappyBackground.png").convert()
backgroundImage = pygame.transform.scale(backgroundImage, (900, 900))


# posX, posY, widthX, heightY
platformGround = pygame.Rect(0, 800, 1280, 100)

platform1 = pygame.Rect(0, 100, 200, 25)
platform2 = pygame.Rect(400, 100, 200, 25)
platform3 = pygame.Rect(0, 250, 200, 25)
platform4 = pygame.Rect(400, 250, 200, 25)
platform5 = pygame.Rect(0, 400, 200, 25)
platform6 = pygame.Rect(400, 400, 200, 25)
platform7 = pygame.Rect(200, 600, 200, 25)

platformList = [platformGround, platform1, platform2, platform3, platform4, platform5, platform6, platform7]



possibleSpawnList = [
    (50, 750),
    (450, 750),
    (50, 350),
    (450, 350),
]   

# random = random.randint(0, 3)
enemy1 = Enemy(possibleSpawnList[0])
enemy2 = Enemy(possibleSpawnList[1])
enemy3 = Enemy(possibleSpawnList[2])
enemy4 = Enemy(possibleSpawnList[3])

projectile1 = Projectile((50, 750), pygame.Vector2(0, -1))


enemyList = [enemy1, enemy2, enemy3, enemy4]
    
velocity = pygame.Vector2(0, 0)
on_ground = False
SPEED = 300
JUMP_SPEED = -650
GRAVITY = 1000

while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    velocity.x = 0
    if keys[pygame.K_a]:
        velocity.x = -SPEED
    if keys[pygame.K_d]:
        velocity.x = SPEED
    if keys[pygame.K_SPACE] and on_ground:
        velocity.y = JUMP_SPEED

    velocity.y += GRAVITY * dt

    # Move X, resolve X collisions
    player_pos.x += velocity.x * dt
    player_rect = playerSprite.get_rect(topleft=player_pos)
    for platform in platformList:
        if player_rect.colliderect(platform):
            if velocity.x > 0:
                player_rect.right = platform.left
            elif velocity.x < 0:
                player_rect.left = platform.right
            player_pos.x = player_rect.x
            velocity.x = 0

    # Move Y, resolve Y collisions
    on_ground = False
    player_pos.y += velocity.y * dt
    player_rect = playerSprite.get_rect(topleft=player_pos)
    for platform in platformList:
        if player_rect.colliderect(platform):
            if velocity.y > 0:
                player_rect.bottom = platform.top
                on_ground = True
            elif velocity.y < 0:
                player_rect.top = platform.bottom
            player_pos.y = player_rect.y
            velocity.y = 0

    # Draw
    screen.fill("yellow")
    for platform in platformList:
        pygame.draw.rect(screen, "brown", platform)
        
    for enemy in enemyList:
        enemy.draw(screen)
        enemy.update(dt)
        
    screen.blit(playerSprite, player_pos)

    pygame.display.flip()

pygame.quit()