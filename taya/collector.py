# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(200, 50)
circle_pos=pygame.Vector2(300,90)

player_hitbox = pygame.Rect(190, 40, 60, 60)
circle_hitbox = pygame.Rect(290, 80, 20, 20)

# game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #circle_pos.x += 573* dt
    
    player_hitbox = pygame.Rect(player_pos.x - 30, player_pos.y - 30, 60, 60)
    circle_hitbox = pygame.Rect(circle_pos.x - 10, circle_pos.y - 10, 20, 20)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")


    pygame.draw.circle(screen, "yellow", circle_pos, 10)
    pygame.draw.circle(screen, "magenta", player_pos, 30)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()