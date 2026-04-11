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

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

batImage = pygame.image.load("assets/robotVillain.png").convert_alpha()
batImage = pygame.transform.scale(batImage, (50, 50))

# xpos, ypos, xwidth, yheight
platformGround = pygame.Rect(0, 600, 1280, 20)
platform1 = pygame.Rect(400, 500, 200, 20)
platform4 = MovingPlatform(100, 400, 150, 20, moving_dir=1, bound_min=50, bound_max=1180, axis='x')

platformList = [platformGround, platform1, platform4.rect]

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

    # Move the moving platform left and right
    platform4.update(dt)

    # Move player with platform if standing on it
    player_rect_cur = pygame.Rect(int(player_pos.x) - 20, int(player_pos.y) - 20, 40, 40)
    if (player_rect_cur.bottom == platform4.rect.top and
            player_rect_cur.right > platform4.rect.left and
            player_rect_cur.left < platform4.rect.right):
        player_pos.x += platform4.rect.left - platform4.prev_x


    for platform in platformList:
        pygame.draw.rect(screen, "white", platform)

    player_rect = pygame.Rect(player_pos.x - 20, player_pos.y - 20, 40, 40)
    pygame.draw.rect(screen, "gold", player_rect)

    for enemy in enemyList:
        enemy.update(dt)
        screen.blit(batImage, (enemy.pos.x, enemy.pos.y))
        
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