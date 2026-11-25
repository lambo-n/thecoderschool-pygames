# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
gravity = 0
canJump = True

player_width = 70
player_height = 70

player_pos = pygame.Vector2(640, 360)
player_rect = pygame.Rect(player_pos.x, player_pos.y, player_width, player_height)

# a block that scrolls across the screen (the level moves, not the player)
spike_pos = pygame.Vector2(1280, 505)
spike_rect = pygame.Rect(spike_pos.x, spike_pos.y, 70, 70)
scroll_speed = 400

geometry_dash_cube_image = pygame.image.load("assets/defaulticon.png").convert_alpha()
geometry_dash_cube_image = pygame.transform.scale(geometry_dash_cube_image, (player_width,player_height))

stereo_madness_background = pygame.image.load("assets/stereomadnessbackground.webp").convert_alpha()
stereo_madness_background = pygame.transform.scale(stereo_madness_background, (1280, 720))

# game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and canJump:
        gravity = 700
        player_pos.y = 504
        canJump = False

    gravity -= 1870 * dt
    player_pos.y -= gravity * dt

    if player_pos.y >= 505:
        player_pos.y = 505
        gravity = 0
        canJump = True

    # move the block left; once it's off the left edge, send it back to the right
    spike_pos.x -= scroll_speed * dt

    if spike_pos.x < -100:
        spike_pos.x = 1350

    spike_rect = pygame.Rect(spike_pos.x, spike_pos.y, 70, 70)
    spike_hitbox = spike_rect.inflate(-50, -50)

    player_rect = pygame.Rect(player_pos.x, player_pos.y, player_width, player_height)

    # make the player lose if they touch the spike's hitbox
    if player_rect.colliderect(spike_hitbox):
        running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(stereo_madness_background, (0, 0))

    screen.blit(geometry_dash_cube_image, player_rect)

    pygame.draw.rect(screen, (0, 0, 0), spike_rect)
    pygame.draw.rect(screen, (255, 0, 0), spike_hitbox, 2)  # debug: show hitbox outline
    pygame.draw.line(screen, (255, 255, 255), (0, 575), (1280, 575))



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
