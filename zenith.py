# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
gravity = 0
canJump = False

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# xpos, ypos, xwidth, yheight
platform1 = pygame.Rect(300, 500, 200, 10)
platform2 = pygame.Rect(700, 400, 200, 10)
platformG = pygame.Rect(0, 600, WIDTH, 20)

platformList = [platform1, platform2, platformG]


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")


    gravity += 1000 * dt
    player_pos.y += gravity * dt

    player_rect = pygame.Rect(player_pos.x, player_pos.y, 40, 40)
    
    # Platform collisions
    for platform in platformList:
        if player_rect.colliderect(platform):
            # Landing on top
            if gravity >= 0 and player_rect.bottom - platform.top <= 20:
                player_rect.bottom = platform.top
                player_pos.y = player_rect.y
                gravity = 0
                canJump = True
            # Hitting the bottom
            elif gravity < 0 and platform.bottom - player_rect.top <= 20:
                player_rect.top = platform.bottom
                player_pos.y = player_rect.y
                gravity = -gravity * 0.3
            # Side collision
            else:
                if player_rect.centerx < platform.centerx:
                    player_rect.right = platform.left
                else:
                    player_rect.left = platform.right
                player_pos.x = player_rect.x

    player_rect.clamp_ip(screen.get_rect())
    player_pos.x = player_rect.x

    for platform in platformList:
        pygame.draw.rect(screen, "black", platform)
    pygame.draw.rect(screen, "red", player_rect)
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and canJump:
        player_pos.y -= 10
        gravity = -600
        canJump = False

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