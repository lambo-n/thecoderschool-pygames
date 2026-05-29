# Example file showing a circle moving on screen
import pygame

from davidPlatform import ObbyPlatform

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

digdugImage = pygame.image.load("assets/digdug.png").convert_alpha()
digdugImage = pygame.transform.scale(digdugImage, (64, 64))

escapeRect = pygame.Rect(1200, 100, 50, 50)

gravity = 0

platform1 = ObbyPlatform(100, 600, 200, 20, "gray")

# Create some platforms
platforms = [
    ObbyPlatform(100, 600, 200, 20, "gray"),
    ObbyPlatform(400, 500, 1280, 20, "gray"),
    ObbyPlatform(700, 400, 200, 20, "gray")
]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    for platform in platforms:
        platform.update(screen)

    pygame.draw.rect(screen, "gold", escapeRect)

    gravity += 12 * dt
    player_pos.y += gravity

    # Build the rect AFTER moving, so collision tests the current position
    playerRect = pygame.Rect(player_pos.x - 32, player_pos.y - 32, 64, 64)

    # Platform collisions
    canJump = False
    for platform in platforms:
        if playerRect.colliderect(platform):
            overlap_top    = playerRect.bottom - platform.top
            overlap_bottom = platform.bottom - playerRect.top
            overlap_left   = playerRect.right - platform.left
            overlap_right  = platform.right - playerRect.left
            overlap_y = min(overlap_top, overlap_bottom)
            overlap_x = min(overlap_left, overlap_right)

            if overlap_y <= overlap_x:
                # Vertical collision
                if gravity >= 0 and overlap_top <= overlap_bottom:
                    playerRect.bottom = platform.top
                    gravity = 0
                    canJump = True
                else:
                    playerRect.top = platform.bottom
                    gravity = 0
            else:
                # Horizontal collision
                if overlap_left <= overlap_right:
                    playerRect.right = platform.left
                else:
                    playerRect.left = platform.right
            player_pos.x = playerRect.centerx
            player_pos.y = playerRect.centery  
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and canJump:
        player_pos.y -= 20
        gravity = -600 * dt
        canJump = False
        
    if keys[pygame.K_s]:
        pass
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # Draw the player at its final, collision-corrected position
    screen.blit(digdugImage, (player_pos.x - 32, player_pos.y - 32))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()