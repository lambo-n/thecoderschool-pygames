# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player1_pos = pygame.Vector2(25, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() - 75, screen.get_height() / 2)
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ballSpeedX = 5
ballSpeedY = 5


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    player1 = pygame.Rect(player1_pos.x, player1_pos.y, 50, 130)
    player2 = pygame.Rect(player2_pos.x, player2_pos.y, 50, 130)

    # move ball
    ball_pos += pygame.Vector2(ballSpeedX, ballSpeedY)
    ball = pygame.Rect(ball_pos.x - 10, ball_pos.y - 10, 20, 20)

    # wall bounce
    if ball.top < 0 or ball.bottom > screen.get_height():
        ballSpeedY *= -1

    # paddle collisions
    if ball.colliderect(player1):
        ballSpeedX = abs(ballSpeedX)
        ball_pos.x = player1_pos.x + 50 + 10
        offset = (ball_pos.y - (player1_pos.y + 65)) / 65
        ballSpeedY = offset * 7

    if ball.colliderect(player2):
        ballSpeedX = -abs(ballSpeedX)
        ball_pos.x = player2_pos.x - 10
        offset = (ball_pos.y - (player2_pos.y + 65)) / 65
        ballSpeedY = offset * 7

    # draw
    pygame.draw.rect(screen, "red", player1)
    pygame.draw.rect(screen, "blue", player2)
    pygame.draw.circle(screen, "white", ball_pos, 10)
    
      
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player2_pos.y += 300 * dt
    if keys[pygame.K_w]:
        player1_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player1_pos.y += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
