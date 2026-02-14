# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

bottomPipe_pos = pygame.Vector2(screen.get_width() - 100, screen.get_height() - 100)
topPipe_pos = bottomPipe_pos - pygame.Vector2(0, 520)

gravity = 0
space_pressed = False

flappyBirdImage = pygame.image.load("assets/flappybird.png").convert_alpha()
flappyBirdImage = pygame.transform.scale(flappyBirdImage, (50, 50))

bottomPipeImage = pygame.image.load("assets/pipes.png").convert_alpha()
bottomPipeImage = pygame.transform.scale(bottomPipeImage, (100, 200))

topPipeImage = pygame.transform.flip(bottomPipeImage, False, True)
topPipeImage = pygame.transform.scale(topPipeImage, (100, 200))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    flappyBirdRect = flappyBirdImage.get_rect(center=player_pos)
    screen.blit(flappyBirdImage, flappyBirdRect)
    
    bottomPipeRect = bottomPipeImage.get_rect(center=bottomPipe_pos)
    screen.blit(bottomPipeImage, bottomPipeRect)
    
    topPipeRect = topPipeImage.get_rect(center=topPipe_pos)
    screen.blit(topPipeImage, topPipeRect)
    
    gravity += 1
    player_pos.y += gravity
    
    bottomPipe_pos.x -= 5
    topPipe_pos = bottomPipe_pos - pygame.Vector2(0, 520)
    
    if bottomPipe_pos.x < -50:
        bottomPipe_pos.x = screen.get_width() + 50
    
    if bottomPipeRect.collidepoint(player_pos) or topPipeRect.collidepoint(player_pos):
        running = False
    
    if player_pos.y > screen.get_height() or player_pos.y < 0:
        running = False



    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]: 
        if not space_pressed:
            gravity = -20
            space_pressed = True
    else:
        space_pressed = False


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.time.delay(2000)
pygame.quit()