import pygame

# stationary platforms, player in top left
# enemies are at the bottom shooting projectiles up
# player can drop projectiles on enemies down below



pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 1 / 60

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

playerSprite = pygame.image.load("assets/digdug.png").convert_alpha()
playerSprite = pygame.transform.scale(playerSprite, (80, 80))

platformGround = pygame.Rect(0, 600, 1280, 100)
platform1 = pygame.Rect(300, 500, 200, 10)
platform2 = pygame.Rect(750, 350, 200, 10)
platformList = [platformGround, platform1, platform2]

velocity = pygame.Vector2(0, 0)
on_ground = False
SPEED = 300
JUMP_SPEED = -500
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
    screen.fill("purple")
    for platform in platformList:
        pygame.draw.rect(screen, "white", platform)
    screen.blit(playerSprite, player_pos)

    pygame.display.flip()

pygame.quit()