# Example file showing a circle moving on screen
import random
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0

# init position 2d vectors
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
coin_pos = pygame.Vector2(200, 200)

# initialize game logic variables
coinsCollected = 0

# load and scale images
coinImage = pygame.image.load("assets/bomb.png").convert_alpha()
coinImage = pygame.transform.scale(coinImage, (64, 64))

robberImage = pygame.image.load("assets/digdug.png").convert_alpha()
robberImage = pygame.transform.scale(robberImage, (64, 64))


# text font
font = pygame.font.SysFont(None, 40)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 0, 0))
    
    # number of coins collected display
    textScore = font.render(str(coinsCollected), True, (255, 255, 255))
    screen.blit(textScore, (50, 50))
    
    # robber player sprite
    robberRect = robberImage.get_rect(center=player_pos)
    screen.blit(robberImage, robberRect)
   
    # coin sprite 
    coinRect = coinImage.get_rect(center=coin_pos)
    screen.blit(coinImage, coinRect)
    
   
    # collision check between player and coin
    if robberRect.colliderect(coinRect):
        coin_pos.x = random.randint(0, 1280)
        coin_pos.y = random.randint(0, 720)
        print("coin collected")        
        coinsCollected += 1    
        
    # input key handler
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
