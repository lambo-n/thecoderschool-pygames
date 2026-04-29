import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Load sprite sheet and split into 3 frames
pacboySpritesheet = pygame.image.load("assets/pacboy.png").convert_alpha()
pacboySpritesheet = pygame.transform.scale(pacboySpritesheet, (150, 50))
sheet_width = pacboySpritesheet.get_width()
sheet_height = pacboySpritesheet.get_height()
frame_width = sheet_width // 3
frames = [
    pacboySpritesheet.subsurface((i * frame_width, 0, frame_width, sheet_height))
    for i in range(3)
]

# Animation state
anim_frame = 0
anim_timer = 0
FRAME_DURATION = 0.1  # seconds per frame

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # Advance animation
    anim_timer += dt
    if anim_timer >= FRAME_DURATION:
        anim_timer -= FRAME_DURATION
        anim_frame = (anim_frame + 1) % len(frames)

    screen.blit(frames[anim_frame], player_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()