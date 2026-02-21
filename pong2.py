# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

leftPaddle_pos = pygame.Vector2(25, screen.get_height() / 2)
rightPaddle_pos = pygame.Vector2(screen.get_width() - 75, screen.get_height() / 2)
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

leftPaddleImage = pygame.image.load("assets/pipes.png").convert_alpha()
leftPaddleImage = pygame.transform.scale(leftPaddleImage, (50, 130))

rightPaddleImage = pygame.image.load("assets/pipes.png").convert_alpha()
rightPaddleImage = pygame.transform.scale(rightPaddleImage, (50, 130))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    screen.blit(leftPaddleImage, leftPaddle_pos)
    screen.blit(rightPaddleImage, rightPaddle_pos)
    
    pygame.draw.circle(screen, "white", ball_pos, 10)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        leftPaddle_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        leftPaddle_pos.y += 300 * dt
    if keys[pygame.K_UP]:
        rightPaddle_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        rightPaddle_pos.y += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()