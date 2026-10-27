# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_width = 70
player_height = 70

player_pos = pygame.Vector2(640, 360)
player_rect = pygame.Rect(player_pos.x, player_pos.y, player_width, player_height)

geometry_dash_cube_image = pygame.image.load("assets/defaulticon.png").convert_alpha()
geometry_dash_cube_image = pygame.transform.scale(geometry_dash_cube_image, (player_width,player_height))

# game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    player_rect = pygame.Rect(player_pos.x, player_pos.y, player_width, player_height)
    screen.blit(geometry_dash_cube_image, player_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()