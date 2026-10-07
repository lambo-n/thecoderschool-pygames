# Example file showing a circle moving on screen
from random import randint
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() - 200)

playerImage = pygame.image.load("assets/digdug.png").convert_alpha()
playerImage = pygame.transform.scale(playerImage, (100, 100))

soda_pos = pygame.Vector2(screen.get_width() / 2, -50)
sodaImage = pygame.image.load("assets/bomb.png").convert_alpha()
sodaImage = pygame.transform.scale(sodaImage, (50, 50))

points = 0

font = pygame.font.SysFont(None, 40)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")
    
    playerRect = playerImage.get_rect(center=player_pos)
    screen.blit(playerImage, playerRect)
    
    sodaRect = sodaImage.get_rect(center=soda_pos)
    screen.blit(sodaImage, sodaRect)
    
    soda_pos.y += 10
    
    if playerRect.colliderect(sodaRect):
        soda_pos.y = -50
        soda_pos.x = randint(0, screen.get_width())
        points += 1
        
    pointText = font.render(str(points), True, (255, 255, 255))
    screen.blit(pointText, (50, 50))
    
    if soda_pos.y > screen.get_height():
        soda_pos.y = -50
        soda_pos.x = randint(0, screen.get_width())
    

    keys = pygame.key.get_pressed()

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



# # from processing import*
# from random import*

# def setup():
#  size(500,500)
 
#  global appleY
#  appleY = 0
 
#  global appleX
#  appleX = 190
 
#  global playerX, score
#  playerX = 190
#  score = 0
 
 
 
#  global cippertsprite
#  cippertsprite = loadImage("cippertsprite.png")
 
#  global applesprite
#  applesprite = loadImage("fuzzsprite.png")

# def draw ():
#   background (0,0,225)
  
  
#   global appleY, appleX, playerX
  
#   global cippertsprite
#   image(cippertsprite,playerX,400,50,50)
  
#   global applesprite
#   image(applesprite,appleX,appleY,50,50)
#   print(appleY)
#   appleY = appleY + 5
#   #appleY = 5
  
#   if appleY > 500:
#     appleY = 0
#     appleX = randint (0,300)
    
#   display()
#   collision()
    
    
#   if keyPressed:
#     if key =="a":
#      playerX -= 8
#     if key == "d":
#      playerX += 8
    
# def display():
#   global score
  

  
  
#   fill(255,255,255)
#   textSize(20)
#   displayText = "Score: " + str(score)
#   text(displayText,12,20)
  
# def collision():
#  global playerX, appleX, appleY, score
#  playerY = 400
 
#  if playerX -10 <= appleX <= playerX + 60 and playerY <= appleY <= playerY + 50: 
#    print("chaught")
#    score += 1
#    appleY = 0
#    appleX = randint (0,300)

  
  
# run()