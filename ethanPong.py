import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
running = True
dt = 0

HEIGHT = screen.get_height()
WIDTH = screen.get_width()

player1_y = HEIGHT / 2
player2_y = HEIGHT / 2
circle_pos = pygame.Vector2(600,300)
speedx = 300
speedy = 300
points1 = 0
points2 = 0



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    

    # moving stuff
    circle_pos.x += speedx * dt
    circle_pos.y += speedy * dt

    keys = pygame.key.get_pressed()
    # player 1
    if keys[pygame.K_w] and player1_y >= 0:
        player1_y -= 390 * dt
    if keys[pygame.K_s] and player1_y <= 485:
        player1_y += 390 * dt

    # player 2
    if keys[pygame.K_UP] and player2_y >= 0:
        player2_y -= 390 * dt
    if keys[pygame.K_DOWN] and player2_y <= 485:
        player2_y += 390 * dt

  
    # hitboxes
    circleHitBox = pygame.Rect(circle_pos.x-7.5,circle_pos.y - 7.5 ,15,15)
    pong1 = pygame.Rect(100,player1_y,25,115)
    pong2 =  pygame.Rect(1100,player2_y,25,115)
    
    
   
    # collision checks


    if circleHitBox.right >= WIDTH or circleHitBox.left <= 0:
      
        print("bounce")

    if circleHitBox.top <= 0 or circleHitBox.bottom >= 600:
        speedy *= -1
        print("BOUNCE")
    
    if pong1.colliderect(circleHitBox):
        speedx *= -1
        circle_pos.x = pong1.right + 7.5

    if pong2.colliderect(circleHitBox):
        speedx *= -1
        circle_pos.x = pong2.left - 7.5

    if pong1.colliderect(circleHitBox) or pong2.colliderect(circleHitBox):
        speedx *= 1.05
    # check
    if circle_pos.x < 0: 
        points2 += 1
        print("Points2")
        circle_pos.x = 600
        circle_pos.y = 300
        speedx = 1
    if circle_pos.x > 1200:
        points1 += 1
        print("Points1")
        circle_pos.x = 600
        circle_pos.y = 300
        speedx = 1

    font = pygame.font.SysFont("Arial", 40)
    livesText = font.render(f"{points1} - {points2}", True, "white")
    screen.blit(livesText, (560,0))
    
    
    if points1 == 5 or points2 ==5:
        running = False
        
        
        
    # if points1 == 5:
    #     screen.fill("red")

    # elif points2 ==5:
    #     screen.fill("blue")
# pong1 = red pong2 = blue



    # drawing stuff    
    midline = pygame.draw.line(screen, "grey",(600,0), (600, 600), 20)
    circle = pygame.draw.circle(screen,"white",circle_pos, 15)
    pygame.draw.rect(screen, "red", pong1)
    pygame.draw.rect( screen, "blue", pong2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
