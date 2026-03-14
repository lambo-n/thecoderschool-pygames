# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

playerSprite = pygame.image.load("assets/digdug.png").convert_alpha()
playerSprite = pygame.transform.scale(playerSprite, (80, 80))

platformGround = pygame.Rect(0, 600, 1280, 100)
platform1 = pygame.Rect(300, 500, 200, 10)
platform2 = pygame.Rect(750, 350, 200, 10)  

platformList = [platformGround, platform1, platform2]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    player_rect = playerSprite.get_rect(topleft=player_pos)
    screen.blit(playerSprite, player_pos)
    
    for platform in platformList:
        pygame.draw.rect(screen, "white", platform)
        
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