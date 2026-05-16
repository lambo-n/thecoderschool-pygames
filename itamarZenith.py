# Example file showing a circle moving on screen
import pygame
from zoieMovingPlatform import MovingPlatform

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
gravity = 0
canJump = False

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

player_pos = pygame.Vector2(48, 590)

# xpos, ypos, xwidth, yheight
# use variables for end portal position at lvl 5
endPortal = pygame.Rect(1120, 150, 50, 10)


platform1 = pygame.Rect(300, 500, 200, 10)
platform2 = pygame.Rect(750, 350, 200, 10)
platform3 = pygame.Rect(750, 150, 200, 10)
platformG = pygame.Rect(0, 630, 1280, 20)
lvl1platforms = [platform1, platform2, platform3, platformG]
lvl1movingplatforms = []

platformb1 = pygame.Rect(700, 250, 200, 10)
platformb2 = pygame.Rect(500, 450, 200, 10)
lvl2platforms = [platformb1, platformG, platformb2]
lvl2movingplatforms = []

platformc1 = MovingPlatform(900, 550, 50, 10, moving_dir=1, bound_min=150, bound_max=600)
platformc2 = MovingPlatform(400, 350, 50, 10, moving_dir=-1, bound_min=150, bound_max=500)
lvl3platforms = [platformc1.rect, platformc2.rect, platformG]
lvl3movingplatforms = [platformc1, platformc2]

currentLvlList = lvl1platforms
currentLvlMovingList = lvl1movingplatforms
currentLvl = 4

squareImage = pygame.image.load("assets/digdug.png")
squareImage = pygame.transform.scale(squareImage, (40, 40))

font = pygame.font.SysFont(None, 40)

user_input = ""
input_feedback = ""

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if currentLvl == 4 and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_input.strip() == "4":
                    currentLvl = 5
                    user_input = ""
                    input_feedback = ""
                    player_pos = pygame.Vector2(48, 590)
                else:
                    input_feedback = "Wrong! Try again."
                    #CONTINUE
                    user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.unicode.isprintable():
                user_input += event.unicode
            
    screen.fill("white")

            
    if currentLvl == 1:
        currentLvlList = lvl1platforms
        currentLvlMovingList = lvl1movingplatforms
    elif currentLvl == 2:
        currentLvlList = lvl2platforms
        currentLvlMovingList = lvl2movingplatforms
    elif currentLvl == 3:
        currentLvlList = lvl3platforms
        currentLvlMovingList = lvl3movingplatforms
    elif currentLvl == 4:
        currentLvlList = [platformG]
        currentLvlMovingList = []
        
        mathProblem = font.render("2 + 2 = ?", True, "red")
        screen.blit(mathProblem, (WIDTH / 2 - 80, HEIGHT / 2 - 60))

        # Draw input box
        input_box = pygame.Rect(WIDTH / 2 - 80, HEIGHT / 2, 160, 40)
        pygame.draw.rect(screen, "black", input_box, 2)
        input_surf = font.render(user_input, True, "black")
        screen.blit(input_surf, (input_box.x + 5, input_box.y + 5))

        # Draw feedback
        if input_feedback:
            feedback_surf = font.render(input_feedback, True, "orange")
            screen.blit(feedback_surf, (WIDTH / 2 - 80, HEIGHT / 2 + 50))

    # fill the screen with a color to wipe away anything from last frame
  

    gravity += 1000 * dt
    player_pos.y += gravity * dt

    player_rect = pygame.Rect(player_pos.x, player_pos.y, 40, 40)

    
    
    # Platform collisions
    for platform in currentLvlList:
        if player_rect.colliderect(platform):
            # Landing on top
            if gravity >= 0 and player_rect.bottom - platform.top <= 20:
                player_rect.bottom = platform.top
                player_pos.y = player_rect.y
                gravity = 0
                canJump = True
            # Hitting the bottom
            elif gravity < 0 and platform.bottom - player_rect.top <= 20:
                player_rect.top = platform.bottom
                player_pos.y = player_rect.y
                gravity = -gravity * 0.3
            # Side collision
            else:
                if player_rect.centerx < platform.centerx:
                    player_rect.right = platform.left
                else:
                    player_rect.left = platform.right
                player_pos.x = player_rect.x
                
    for movingPlatform in currentLvlMovingList:
        movingPlatform.update(dt)
        

    player_rect.clamp_ip(screen.get_rect())
    player_pos.x = player_rect.x

    for platform in currentLvlList:
        pygame.draw.rect(screen, "black", platform)
    screen.blit(squareImage, player_rect)

    pygame.draw.rect(screen, "green", endPortal)

    if player_rect.colliderect(endPortal):
        player_pos = pygame.Vector2(48, 590)
        currentLvl += 1


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and canJump:
        player_pos.y -= 10
        gravity = -600
        canJump = False

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
