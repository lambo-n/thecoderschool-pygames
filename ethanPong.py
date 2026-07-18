import pygame
import random
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
pong1Height = 115
pong2Height = 115
circle_pos = pygame.Vector2(600,300)
speedx = random.randrange(300,601,100) * random.randrange(-1,2,2)
speedy = random.randrange(300,601,100) * random.randrange(-1,2,2)
points1 = 0
points2 = 0
powerupShow = True
redPowerUp = False
bluePowerUp = False


powerupImage = pygame.image.load("assets/powerupImage.png").convert_alpha()
powerupImage = pygame.transform.scale(powerupImage, (70, 70))
powerup_pos = pygame.Vector2 (random.randint(0,WIDTH), random.randint(0, HEIGHT))

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
        player1_y -= 500 * dt
    if keys[pygame.K_s] and player1_y <= 485:
        player1_y += 500 * dt

    # player 2
    if keys[pygame.K_UP] and player2_y >= 0:
        player2_y -= 500 * dt
    if keys[pygame.K_DOWN] and player2_y <= 485:
        player2_y += 500 * dt

  
    # hitboxes
    circleHitBox = pygame.Rect(circle_pos.x-7.5,circle_pos.y - 7.5 ,15,15)
    pong1 = pygame.Rect(100,player1_y,25,pong1Height)
    pong2 =  pygame.Rect(1100,player2_y,25,pong2Height)
    
    
    powerupRect = powerupImage.get_rect(center = powerup_pos)
    if powerupShow == True:
        screen.blit(powerupImage, powerupRect)
    else:
        powerupRect = pygame.Rect(0,0,0,0)
   
    # collision checks
# powerupHitbox = pygame.Rect(powerup_pos.x, powerup_pos.y,50,60)


    if powerupRect.colliderect(circleHitBox):
        powerupShow = False
        
        if speedx > 0: 
            redPowerUp = True
        elif speedx < 0:
            bluePowerUp = True
    
    if redPowerUp == True:
        pong1Height = 200
    else:
        pong1Height = 115
        
    if bluePowerUp == True:
        pong2Height = 200
    else:
        pong2Height = 115


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
        powerup_pos.x = random.randint(0,WIDTH)
        powerup_pos.y = random.randint(0,HEIGHT)
        speedx = random.randrange(300,601,100) * random.randrange(-1,2,2)
    if circle_pos.x > 1200:
        points1 += 1
        print("Points1")
        circle_pos.x = 600
        circle_pos.y = 300
        powerup_pos.x = random.randint(0,WIDTH)
        powerup_pos.y = random.randint(0,HEIGHT)
        speedx =  speedx = random.randrange(300,601,100) * random.randrange(-1,2,2)

    font = pygame.font.SysFont("Arial", 40)
    livesText = font.render(f"{points1} - {points2}", True, "white")
    screen.blit(livesText, (560,0))
    
    
    if points1 == 5 or points2 ==5:
        running = False
        
        
        
    if points1 == 5:
        screen.fill("red")

    elif points2 ==5:
        screen.fill("blue")
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
