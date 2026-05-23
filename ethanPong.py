# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
running = True
dt = 0

player1_y = screen.get_height() / 2
player2_y = screen.get_height() / 2
circle_pos = pygame.Vector2(600, 300)

speedx = 300
speedy = 300



# game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    midline = pygame.draw.line(screen, "white", (600, 0), (600, 600), 20)
    

    circle = pygame.draw.circle(screen, "white", circle_pos, 15)
    
    circle_pos.x += speedx * dt
    circle_pos.y += speedy * dt
    
    pong1 = pygame.Rect(100, player1_y, 25, 115)
    pygame.draw.rect(screen, "red", pong1)
    
    pong2 = pygame.Rect(1100, player2_y, 25, 115)
    pygame.draw.rect(screen, "blue", pong2)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y >= 0: 
        player1_y -= 300 * dt
    if keys[pygame.K_s] and player1_y <= 600-115:
        player1_y += 300 * dt
        
    if keys[pygame.K_UP] and player2_y >= 0:
        player2_y -= 300 * dt
    if keys[pygame.K_DOWN] and player2_y <= 600-115:
        player2_y += 300 * dt 

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()