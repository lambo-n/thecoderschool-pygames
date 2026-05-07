# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
#screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1280, 720))
# 1280 x 720
# 640 x 360
clock = pygame.time.Clock()
running = True
dt = 0
gameState = "titleScreen"
playerCount = 2
jumpCount = 2
gamemode = "normal"
# Normal, Bomb, Freeze, Infection
gamemodeList = ["Normal", "Bomb", "Freeze", "Infection"]
gamemodeIndex = 0
platformDevMode = False
taggedPlayer = random.randint(0, 4)
print(taggedPlayer)

SCREEN_HEIGHT = screen.get_height()
SCREEN_WIDTH = screen.get_width()
SCREEN_AVERAGE_LENGTH = (SCREEN_HEIGHT + SCREEN_WIDTH) / 2

fontWidth = int(SCREEN_AVERAGE_LENGTH / (1000 / 80))
FONT = pygame.font.SysFont(None, fontWidth)

TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 1000)
countdown_seconds = 100

PLAYER_HEIGHT = SCREEN_HEIGHT / (720 / 20)
PLAYER_WIDTH = SCREEN_WIDTH / (1280 / 20)
PLAYER_MOVEMENT_SPEED = SCREEN_WIDTH / (1280 / 250)
PLAYER_JUMP_HEIGHT = SCREEN_HEIGHT / (720 / 425)
PLAYER_GRAVITY = SCREEN_HEIGHT / (720 / 700)

TAG_COOLDOWN = 3.0
tag_cooldowns = [0.0] * 5

player1_pos = pygame.Vector2((SCREEN_WIDTH * 1) / 6, SCREEN_HEIGHT - 100)
player2_pos = pygame.Vector2((SCREEN_WIDTH * 2) / 6, SCREEN_HEIGHT - 100)
player3_pos = pygame.Vector2((SCREEN_WIDTH * 3) / 6, SCREEN_HEIGHT - 100)
player4_pos = pygame.Vector2((SCREEN_WIDTH * 4) / 6, SCREEN_HEIGHT - 100)
player5_pos = pygame.Vector2((SCREEN_WIDTH * 5) / 6, SCREEN_HEIGHT - 100)

player1_alive = False
player2_alive = False
player3_alive = False
player4_alive = False
player5_alive = False

player_positions = [player1_pos, 
                    player2_pos, 
                    player3_pos, 
                    player4_pos,
                    player5_pos]

player1_velocity = 0
player2_velocity = 0
player3_velocity = 0
player4_velocity = 0
player5_velocity = 0

player_velocities = [player1_velocity, 
                     player2_velocity, 
                     player3_velocity, 
                     player4_velocity, 
                     player5_velocity]

player_jump_counts = [jumpCount, jumpCount, jumpCount, jumpCount, jumpCount]

mapAfloorBase = pygame.Rect(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 75))
mapAplatform1 = pygame.Rect(SCREEN_WIDTH / (1280 / 400), SCREEN_HEIGHT / (720 / 500), SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (1280 / 36))
mapAplatform2 = pygame.Rect(SCREEN_WIDTH / (1280 / 700), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (720 / 20))
mapAplatform3 = pygame.Rect(0, SCREEN_HEIGHT / (720 / 300), SCREEN_WIDTH / (1280 / 400), SCREEN_HEIGHT / (720 / 20))
mapAplatform4 = pygame.Rect(SCREEN_WIDTH / (1280 / 100), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (720 / 20))
mapAplatform5 = pygame.Rect(SCREEN_WIDTH / (1280 / 700), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 100))
mapAplatform6 = pygame.Rect(0, SCREEN_HEIGHT / (720 / 500), SCREEN_WIDTH / (1280 / 100), SCREEN_HEIGHT / (720 / 20))
mapAplatform7 = pygame.Rect(SCREEN_WIDTH / (1280 / 100), SCREEN_HEIGHT / (720 / 200), SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (720 / 20))
mapAplatform8 = pygame.Rect(SCREEN_WIDTH / (1280 / 800), SCREEN_HEIGHT / (720 / 550), SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (720 / 20))
mapAplatform9 = pygame.Rect(SCREEN_WIDTH / (1280 / 1100), SCREEN_HEIGHT / (720 / 550), SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (720 / 20))
mapAplatform10 = pygame.Rect(SCREEN_WIDTH / (1280 / 1100), SCREEN_HEIGHT / (720 / 275), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 145))
mapAplatform11 = pygame.Rect(SCREEN_WIDTH / (1280 / 1075), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 40), SCREEN_HEIGHT / (720 / 20))
mapAplatform12 = pygame.Rect(SCREEN_WIDTH / (1280 / 1190), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 100), SCREEN_HEIGHT / (720 / 20))
mapAplatform13 = pygame.Rect(SCREEN_WIDTH / (1280 / 1100), SCREEN_HEIGHT / (720 / 475), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 75))
mapAplatform14 = pygame.Rect(SCREEN_WIDTH / (1280 / 1190), SCREEN_HEIGHT / (720 / 475), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 20))
mapAplatform15 = pygame.Rect(SCREEN_WIDTH / (1280 / 1120), SCREEN_HEIGHT / (720 / 325), SCREEN_WIDTH / (1280 / 25), SCREEN_HEIGHT / (720 / 20))
mapAplatform16 = pygame.Rect(SCREEN_WIDTH / (1280 / 1100), SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 145))

mapA = [mapAfloorBase, mapAplatform1, mapAplatform2, mapAplatform3, mapAplatform4, mapAplatform5, mapAplatform6, mapAplatform7, mapAplatform8, mapAplatform9, mapAplatform10, mapAplatform11, mapAplatform12, mapAplatform13, mapAplatform14, mapAplatform15, mapAplatform16]
mapB = []

downArrowImage = pygame.image.load("arrow1.png").convert_alpha()
downArrowImage = pygame.transform.scale(downArrowImage, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Menu UI Elements
jumpCountIncrement = pygame.Rect(SCREEN_WIDTH / 2 + 280, 475, 75, 75)
jumpCountDecrement = pygame.Rect(SCREEN_WIDTH / 2 - 353, 475, 75, 75)

playerCountIncrement = pygame.Rect(SCREEN_WIDTH / 2 + 280, 375, 75, 75)
playerCountDecrement = pygame.Rect(SCREEN_WIDTH / 2 - 353, 375, 75, 75)

gamemodeIncrement = pygame.Rect(SCREEN_WIDTH / 2 + 280, 275, 75, 75)
gameModeDecrement = pygame.Rect(SCREEN_WIDTH / 2 - 353, 275, 75, 75)



menuStart = pygame.Rect((SCREEN_WIDTH / (1280 / 440), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 400), SCREEN_HEIGHT / (720 / 150)))

startGame = pygame.Rect((SCREEN_WIDTH / 2 - 250, 600, 500, 75))
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            jump_bindings = [pygame.K_w, pygame.K_t, pygame.K_i, pygame.K_LEFTBRACKET, pygame.K_UP]
            for idx, key in enumerate(jump_bindings):
                if event.key == key and player_jump_counts[idx] > 0:
                    player_velocities[idx] = -PLAYER_JUMP_HEIGHT
                    player_jump_counts[idx] -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if gameState == "titleScreen":
                if menuStart.collidepoint(event.pos):
                    gameState = "menu"
            
            if gameState == "menu":
                if playerCountIncrement.collidepoint(event.pos):
                    playerCount = min(playerCount + 1, 5)

                elif playerCountDecrement.collidepoint(event.pos):
                    playerCount = max(playerCount - 1, 2)

                elif jumpCountIncrement.collidepoint(event.pos):
                    jumpCount = min(jumpCount + 1, 15)

                elif jumpCountDecrement.collidepoint(event.pos):
                    jumpCount = max(jumpCount - 1, 1)

                elif gamemodeIncrement.collidepoint(event.pos):
                    if gamemodeIndex == 3:
                        gamemodeIndex = 0
                    else:
                        gamemodeIndex += 1
                elif gameModeDecrement.collidepoint(event.pos):
                    if gamemodeIndex == 0:
                        gamemodeIndex = 3
                    else:
                        gamemodeIndex -= 1

                elif startGame.collidepoint(event.pos):
                    gameState = "playing"
                    if playerCount >= 1:
                        player1_alive = True
                    if playerCount >= 2:
                        player2_alive = True
                    if playerCount >= 3:
                        player3_alive = True
                    if playerCount >= 4:
                        player4_alive = True
                    if playerCount >= 5:
                        player5_alive = True
                
        
        if event.type == TIMER_EVENT:
            countdown_seconds -= 1
            if countdown_seconds <= 0:
                pygame.time.set_timer(TIMER_EVENT, 0)
    if gameState == "titleScreen": # Checks if the gamestate is titleScreen

        screen.fill("#419af2") # Background
        pygame.draw.rect(screen, "white", (SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (720 / 50), SCREEN_WIDTH / (1280 / 840), SCREEN_HEIGHT / (720 / 200))) # Tag text
        pygame.draw.rect(screen, "white", menuStart) # Tag text

    elif gameState == "menu": # Checks if the gamestate is menu

        screen.fill("#419af2") # Background
        

        
        pygame.draw.rect(screen, "white", (SCREEN_WIDTH / 2 - 420, 50, 840, 175)) # Tag text

        pygame.draw.rect(screen, "white", (SCREEN_WIDTH / 2 - 250, 275, 500, 75)) # Type of gamemode

        pygame.draw.rect(screen, "white", (SCREEN_WIDTH / 2 - 250, 375, 500, 75)) # Amount of players box

        pygame.draw.rect(screen, "white", (SCREEN_WIDTH / 2 - 250, 475, 500, 75)) # Amount of Double Jumps

        pygame.draw.rect(screen, "green", startGame) # Start Game

        def right_tri(r):
            return [(r.left, r.top), (r.left, r.bottom), (r.right, r.centery)]
        def left_tri(r):
            return [(r.right, r.top), (r.right, r.bottom), (r.left, r.centery)]
        
        # Gamemode cycle increment and decrement
        pygame.draw.polygon(screen, "white", right_tri(gamemodeIncrement))
        pygame.draw.polygon(screen, "white", left_tri(gameModeDecrement))  

        # Player count increment and decrement
        pygame.draw.polygon(screen, "white", right_tri(playerCountIncrement))
        pygame.draw.polygon(screen, "white", left_tri(playerCountDecrement))

        # Jump count increment and decrement
        pygame.draw.polygon(screen, "white", right_tri(jumpCountIncrement))
        pygame.draw.polygon(screen, "white", left_tri(jumpCountDecrement))



        text_surface = FONT.render(str(gamemodeList[gamemodeIndex]), True, (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH / 2 - text_surface.get_width()// 2, 275))

        text_surface = FONT.render(str(playerCount) + " Players", True, (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH / 2 - text_surface.get_width()// 2, 375))

        jumpText = " Jumps" if jumpCount > 1 else " Jump"
        text_surface = FONT.render(str(jumpCount)+ jumpText, True, (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH / 2 - text_surface.get_width()// 2, 475))

    elif gameState == "playing": # Checks if the gamestate is playing
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("gray")

        playerAliveList = [player1_alive, player2_alive, player3_alive, player4_alive, player5_alive]

        while not playerAliveList[taggedPlayer]:
            taggedPlayer = random.randint(0, 4)

        # pygame.draw.circle(screen, "red", player1_pos, 40)
        # pygame.draw.circle(screen, "blue", player2_pos, 40)
        # pygame.draw.circle(screen, "green", player3_pos, 40)
        # pygame.draw.circle(screen, "yellow", player4_pos, 40)
        # pygame.draw.circle(screen, "orange", player5_pos, 40)

        if player1_alive:
            pygame.draw.rect(screen, "red", (player1_pos.x, player1_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
        if player2_alive:
            pygame.draw.rect(screen, "yellow", (player2_pos.x, player2_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
        if player3_alive:
            pygame.draw.rect(screen, "blue", (player3_pos.x, player3_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
        if player4_alive:
            pygame.draw.rect(screen, "green", (player4_pos.x, player4_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
        if player5_alive:
            pygame.draw.rect(screen, "purple", (player5_pos.x, player5_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))

        tagged_pos = player_positions[taggedPlayer]
        screen.blit(downArrowImage, (tagged_pos.x, tagged_pos.y - PLAYER_HEIGHT - 2))

        text_surface = FONT.render(str(countdown_seconds), True, (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH / 2 - fontWidth / 2, (SCREEN_HEIGHT / (1280 / 25))))

        if platformDevMode:
            for platform in mapA:
                None
        else:
            for platform in mapA:
                pygame.draw.rect(screen, "black", platform)

        for i in range(len(player_velocities)):
            player_velocities[i] += PLAYER_GRAVITY * dt

        for i in range(len(player_positions)):
            prev_bottom = player_positions[i].y + PLAYER_HEIGHT
            player_positions[i].y += player_velocities[i] * dt
            
            player_rect = pygame.Rect(player_positions[i].x, player_positions[i].y, PLAYER_WIDTH, PLAYER_HEIGHT)
            for platform in mapA:
                if player_rect.colliderect(platform):
                    if player_velocities[i] >= 0 and player_rect.bottom - platform.top <= 20:
                        player_positions[i].y = platform.y - PLAYER_HEIGHT
                        player_velocities[i] = 0
                        player_rect.y = player_positions[i].y
                    elif player_velocities[i] < 0 and platform.bottom - player_rect.top <= 20:
                        player_rect.top = platform.bottom
                        player_positions[i].y = player_rect.y
                        player_velocities[i] = -player_velocities[i] * 0.3
                    else:
                        if player_rect.centerx < platform.centerx:
                            player_rect.right = platform.left
                        else: player_rect.left = platform.right
                    player_positions[i].x = player_rect.x

        for i in range(len(tag_cooldowns)):
            if tag_cooldowns[i] > 0:
                tag_cooldowns[i] = max(0.0, tag_cooldowns[i] - dt)

        # Player-to-player collisions
        for i in range(len(player_positions)):
            if not playerAliveList[i]:
                continue
            player_rect = pygame.Rect(player_positions[i].x, player_positions[i].y, PLAYER_WIDTH, PLAYER_HEIGHT)
            for j in range(i + 1, len(player_positions)):
                if not playerAliveList[j]:
                    continue
                other_rect = pygame.Rect(player_positions[j].x, player_positions[j].y, PLAYER_WIDTH, PLAYER_HEIGHT)
                if player_rect.colliderect(other_rect):
                    if taggedPlayer == i and tag_cooldowns[i] <= 0:
                        taggedPlayer = j
                        tag_cooldowns[i] = TAG_COOLDOWN
                        tag_cooldowns[j] = TAG_COOLDOWN
                        print(taggedPlayer)
                    elif taggedPlayer == j and tag_cooldowns[j] <= 0:
                        taggedPlayer = i
                        tag_cooldowns[i] = TAG_COOLDOWN
                        tag_cooldowns[j] = TAG_COOLDOWN
                        print(taggedPlayer)
                    # Calculate overlap on each axis
                    overlap_x = min(player_rect.right, other_rect.right) - max(player_rect.left, other_rect.left)
                    overlap_y = min(player_rect.bottom, other_rect.bottom) - max(player_rect.top, other_rect.top)

                    if overlap_x < overlap_y:
                        # Horizontal push - each player gets pushed half the overlap
                        if player_positions[i].x < player_positions[j].x:
                            player_positions[i].x -= overlap_x / 2
                            player_positions[j].x += overlap_x / 2
                        else:
                            player_positions[i].x += overlap_x / 2
                            player_positions[j].x -= overlap_x / 2
                    else:
                        # Vertical push
                        if player_positions[i].y < player_positions[j].y:
                            player_positions[i].y -= overlap_y / 2
                            player_positions[j].y += overlap_y / 2
                        else:
                            player_positions[i].y += overlap_y / 2
                            player_positions[j].y -= overlap_y / 2
                        # Stop vertical velocity for both on vertical collision
                        player_velocities[i] = 0
                        player_velocities[j] = 0
                        # Re-resolve platform collisions so players can't be pushed through platforms
                        for pi in [i, j]:
                            p_rect = pygame.Rect(player_positions[pi].x, player_positions[pi].y, PLAYER_WIDTH, PLAYER_HEIGHT)
                            for platform in mapA:
                                if p_rect.colliderect(platform):
                                    player_positions[pi].y = platform.y - PLAYER_HEIGHT
                                    player_velocities[pi] = 0
                                    p_rect.y = player_positions[pi].y

            
        on_ground = []
        for i in range(len(player_positions)):
            check_rect = pygame.Rect(player_positions[i].x, player_positions[i].y + 1, PLAYER_WIDTH, PLAYER_HEIGHT)
            on_platform = any(check_rect.colliderect(platform) for platform in mapA)
            on_player = any(
                j != i and
                abs((player_positions[i].y + PLAYER_HEIGHT) - player_positions[j].y) <= 2 and
                player_positions[i].x + PLAYER_WIDTH > player_positions[j].x and
                player_positions[i].x < player_positions[j].x + PLAYER_WIDTH
                for j in range(len(player_positions))
            )
        
            on_ground.append(on_platform or on_player)

        for i in range(len(player_positions)):
            if on_ground[i]:
                player_jump_counts[i] = jumpCount
            elif player_jump_counts[i] == jumpCount:
                player_jump_counts[i] = jumpCount - 1

        keys = pygame.key.get_pressed()
        if player1_alive:
            if keys[pygame.K_w] and on_ground[0]:
                player_velocities[0] = -PLAYER_JUMP_HEIGHT
            if keys[pygame.K_a]:
                player1_pos.x -= PLAYER_MOVEMENT_SPEED * dt
            if keys[pygame.K_d]:
                player1_pos.x += PLAYER_MOVEMENT_SPEED * dt

        if player2_alive:    
            if keys[pygame.K_t] and on_ground[1]:
                player_velocities[1] = -PLAYER_JUMP_HEIGHT
            if keys[pygame.K_f]:
                player2_pos.x -= PLAYER_MOVEMENT_SPEED * dt
            if keys[pygame.K_h]:
                player2_pos.x += PLAYER_MOVEMENT_SPEED * dt
        
        if player3_alive:
            if keys[pygame.K_i] and on_ground[2]:
                player_velocities[2] = -PLAYER_JUMP_HEIGHT
            if keys[pygame.K_j]:
                player3_pos.x -= PLAYER_MOVEMENT_SPEED * dt
            if keys[pygame.K_l]:
                player3_pos.x += PLAYER_MOVEMENT_SPEED * dt
        
        if player4_alive:
            if keys[pygame.K_LEFTBRACKET] and on_ground[3]:
                player_velocities[3] = -PLAYER_JUMP_HEIGHT
            if keys[pygame.K_SEMICOLON]:
                player4_pos.x -= PLAYER_MOVEMENT_SPEED * dt
            if keys[pygame.K_RETURN]:
                player4_pos.x += PLAYER_MOVEMENT_SPEED * dt

        if player5_alive:
            if keys[pygame.K_UP] and on_ground[4]:
                player_velocities[4] = -PLAYER_JUMP_HEIGHT
            if keys[pygame.K_LEFT]:
                player5_pos.x -= PLAYER_MOVEMENT_SPEED * dt
            if keys[pygame.K_RIGHT]:
                player5_pos.x += PLAYER_MOVEMENT_SPEED * dt
            
        for pos in player_positions:
            pos.x = max(0, min(pos.x, SCREEN_WIDTH - PLAYER_WIDTH))
            pos.y = max(0, min(pos.y, SCREEN_HEIGHT - PLAYER_HEIGHT))  


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
