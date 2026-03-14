# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

leftPaddle_pos = pygame.Vector2(50, screen.get_height() / 2)
rightPaddle_pos = pygame.Vector2(screen.get_width() - 25, screen.get_height() / 2)

ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_speed = pygame.Vector2(300, 300)

leftPaddleImage = pygame.image.load("assets/pipes.png").convert_alpha()
leftPaddleImage = pygame.transform.scale(leftPaddleImage, (50, 130))

rightPaddleImage = pygame.image.load("assets/pipes.png").convert_alpha()
rightPaddleImage = pygame.transform.scale(rightPaddleImage, (50, 130))

player1Score = 0
player2Score = 0

font = pygame.font.SysFont(None, 100)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    leftPaddleRect = leftPaddleImage.get_rect(center=leftPaddle_pos)
    screen.blit(leftPaddleImage, leftPaddleRect)
    
    rightPaddleRect = rightPaddleImage.get_rect(center=rightPaddle_pos)
    screen.blit(rightPaddleImage, rightPaddleRect)
    
    text_surface = font.render(f"{player1Score} - {player2Score}", True, "white")
    text_rect = text_surface.get_rect(center=(screen.get_width() / 2, 30))
    screen.blit(text_surface, text_rect) 
    
    ball = pygame.draw.circle(screen, "white", ball_pos, 10)
    
      
    ball_pos += ball_speed * dt
    
    if ball_pos.y > screen.get_height() or ball_pos.y < 0:
        ball_speed.y *= -1
        
    if ball_pos.x > screen.get_width():
        ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        player1Score += 1
        
    if  ball_pos.x < 0:
        ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        player2Score += 1
    
    
    if ball.colliderect(leftPaddleRect):
        ball_speed.x = abs(ball_speed.x)
        ball_pos.x = leftPaddle_pos.x + 35
        offset = (ball_pos.y - leftPaddle_pos.y) / 65
        ball_speed.y = offset * 300

    if ball.colliderect(rightPaddleRect):
        ball_speed.x = -abs(ball_speed.x)
        ball_pos.x = rightPaddle_pos.x - 35
        offset = (ball_pos.y - rightPaddle_pos.y) / 65
        ball_speed.y = offset * 300
  
    
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