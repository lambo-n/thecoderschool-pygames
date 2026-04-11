# Example file showing a circle moving on screen
import pygame
from moving_platform import MovingPlatform
from chaseenemy import Enemy

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
gravity = 0
canJump = False
enemyTimer = 0
enemySpawnTime = 2
coinX = 600
coinY = 150
lives = 5

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

batImage = pygame.image.load("assets/robotVillain.png").convert_alpha()
batImage = pygame.transform.scale(batImage, (50, 50))

coinImage = pygame.image.load("assets/bitcoin.png").convert_alpha()
coinImage = pygame.transform.scale(coinImage, (30, 30))
coinRect = coinImage.get_rect(center=(coinX, coinY))


# xpos, ypos, xwidth, yheight
platformGround = pygame.Rect(0, 600, 1280, 20)
platform1 = MovingPlatform(100, 250, 150, 20, moving_dir=1, bound_min=50, bound_max=1180, axis='x')
platform2 = MovingPlatform(400, 450, 150, 20, moving_dir=-1, bound_min=50, bound_max=1180, axis='x')
platform3 = MovingPlatform(700, 150, 150, 20, moving_dir=1, bound_min=50, bound_max=1180, axis='x')
platform4 = MovingPlatform(100, 350, 150, 20, moving_dir=1, bound_min=50, bound_max=1180, axis='x')


platformList = [platformGround, platform1.rect, platform2.rect, platform3.rect, platform4.rect]

movingPlatformList = [platform1, platform2, platform3, platform4]

testEnemy = Enemy()
enemyList = [testEnemy]


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Move player with platform if standing on it



    for platform in platformList:
        pygame.draw.rect(screen, "white", platform)
        
    player_rect_cur = pygame.Rect(int(player_pos.x) - 20, int(player_pos.y) - 20, 40, 40) 
        
    for movingPlatform in movingPlatformList:
        movingPlatform.update(dt)
        
       
        if (player_rect_cur.bottom == movingPlatform.rect.top and
            player_rect_cur.right > movingPlatform.rect.left and
            player_rect_cur.left < movingPlatform.rect.right):
            player_pos.x += movingPlatform.rect.left - movingPlatform.prev_x

    player_rect = pygame.Rect(player_pos.x - 20, player_pos.y - 20, 40, 40)
    pygame.draw.rect(screen, "gold", player_rect)

    screen.blit(coinImage, coinRect)
    
    if player_rect.collideRect(coinRect):
        #coinX = random.randint()
        coins += 1

    for enemy in enemyList:
        enemy.update(dt)
        screen.blit(batImage, (enemy.pos.x, enemy.pos.y))
        
        if player_rect.colliderect(enemy.get_rect()):
            print("Player hit!")
            enemyList.remove(enemy)
            lives -= 1
        
        if enemy.pos.x < -50 or enemy.pos.x > 1300:
            enemy.direction *= -1

    if enemyTimer >= enemySpawnTime:
        newEnemy = Enemy()
        enemyList.append(newEnemy)
        enemyTimer = 0
        
    enemyTimer += dt

    gravity += 1000 * dt
    player_pos.y += gravity * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and canJump:
        gravity = -600
        canJump = False
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    # Rebuild rect after movement so collisions use updated position
    player_rect = pygame.Rect(player_pos.x - 20, player_pos.y - 20, 40, 40)

    # Platform collisions using minimum overlap (MTV)
    canJump = False
    for platform in platformList:
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

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()