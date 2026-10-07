# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
spiritCount = 0
gameState = "playing"

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
spirit_pos = pygame.Vector2(500, 200)

freddyImage = pygame.image.load("assets/robotVillain.png").convert_alpha()
freddyImage = pygame.transform.scale(freddyImage, (100, 100))

spiritImage = pygame.image.load("assets/cryingChild.png").convert_alpha()
spiritImage = pygame.transform.scale(spiritImage, (50, 50))

shopImage = pygame.image.load("assets/cave.jpeg").convert_alpha()
shopImage = pygame.transform.scale(shopImage, (200, 100))
shopRect = shopImage.get_rect(topleft=(640, 600))

font = pygame.font.SysFont(None, 40)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
           
            if shopRect.collidepoint(mx, my):
                print("shop")
                        

    if gameState == "playing":        
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("brown")
        
        freddyRect = freddyImage.get_rect(center=player_pos)
        spiritRect = spiritImage.get_rect(center=spirit_pos)
        
        if freddyRect.colliderect(spiritRect):
            randomNumX = random.randint(0, 1280)
            randomNumY = random.randint(0, 720)
            
            
            spiritCount += 1
            print(spiritCount)
            
            spirit_pos = pygame.Vector2(randomNumX, randomNumY)
        
        screen.blit(freddyImage, player_pos)
        screen.blit(spiritImage, spirit_pos)
        screen.blit(shopImage, (640, 600))
        
        text = font.render(str(spiritCount), True, "black")
        screen.blit(text, (50, 50))

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