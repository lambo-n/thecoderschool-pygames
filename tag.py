# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
jumpCount = 3
# normal, bomb, freeze, infection
gamemode = "normal"
gameState = "title" 
playerCount = 5
taggedPlayer = random.randint(0, playerCount - 1)


WIDTH = screen.get_width()
HEIGHT = screen.get_height()

PLAYER_HEIGHT = 20
PLAYER_WIDTH = 20
PLAYER_MOVEMENT_SPEED = 250
PLAYER_JUMP_HEIGHT = 300
PLAYER_GRAVITY = 550

player1_pos = pygame.Vector2(0, HEIGHT-100)
player2_pos = pygame.Vector2(200, HEIGHT-100)
player3_pos = pygame.Vector2(400, HEIGHT-100)
player4_pos = pygame.Vector2(600, HEIGHT-100)
player5_pos = pygame.Vector2(800, HEIGHT-100)

player1alive = False
player2alive = False
player3alive = False
player4alive = False
player5alive = False


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

player_jump_counts = [jumpCount, jumpCount, jumpCount, jumpCount, jumpCount]  # remaining jumps per player (max 2)

TAG_COOLDOWN = 2.0  # seconds before a newly-tagged player can tag back
tag_cooldowns = [0.0] * 5  # cooldown timer per player


floorBase = pygame.Rect(0, HEIGHT - 100, WIDTH, 10)
platform1 = pygame.Rect(400, 500, 200, 20)
platform2 = pygame.Rect(WIDTH / (1280/700), 400, 200, 20)
platform3 = pygame.Rect(0, 300, 400, 20)
platform4 = pygame.Rect(100, 400, 200, 20)
platform5 = pygame.Rect(700, 400, 20, 100)
platform6 = pygame.Rect(0, 500, 100, 20)
platform7 = pygame.Rect(100, 200, 200, 20)
platform8 = pygame.Rect(800, 550, 100, 20)

platforms = [floorBase, platform1, platform2, platform3, platform4, platform5, platform6, platform7, platform8]

downArrowImage = pygame.image.load("assets/downArrow.png").convert_alpha()
downArrowImage = pygame.transform.scale(downArrowImage, (PLAYER_WIDTH, PLAYER_HEIGHT))

fontWidth = 60
font = pygame.font.SysFont(None, fontWidth)

TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 1000)
countdown_seconds = 60


# TITLE UI ELEMENTS
titleStart = pygame.Rect(WIDTH/2 - 100, 500, 200, 50)

# MENU UI ELEMENTS
playerCountIncrement = pygame.Rect(WIDTH/2 + 110, 200, 50, 50)
playerCountDecrement = pygame.Rect(WIDTH/2 - 160, 200, 50, 50)

jumpCountIncrement = pygame.Rect(WIDTH/2 + 110, 300, 50, 50)
jumpCountDecrement = pygame.Rect(WIDTH/2 - 160, 300, 50, 50)

gamemodeIncrement = pygame.Rect(WIDTH/2 + 110, 400, 50, 50)
gamemodeDecrement = pygame.Rect(WIDTH/2 - 160, 400, 50, 50)

startGame = pygame.Rect(WIDTH/2 - 100, 600, 200, 50)





while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            jump_bindings = [pygame.K_w, pygame.K_t, pygame.K_i, pygame.K_UP, pygame.K_LEFTBRACKET]
            for idx, key in enumerate(jump_bindings):
                if event.key == key and player_jump_counts[idx] > 0:
                    player_velocities[idx] = -PLAYER_JUMP_HEIGHT
                    player_jump_counts[idx] -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if gameState == "title":
                if titleStart.collidepoint(event.pos):
                    gameState = "menu"
                    
            if gameState == "menu":
                if playerCountIncrement.collidepoint(event.pos):
                    playerCount = min(playerCount + 1, 5)
                elif playerCountDecrement.collidepoint(event.pos):
                    playerCount = max(playerCount - 1, 2)
                elif startGame.collidepoint(event.pos):
                    gameState = "playing"
                    if playerCount >= 1:
                        player1alive = True
                    if playerCount >= 2:
                        player2alive = True
                    if playerCount >= 3:
                        player3alive = True
                    if playerCount >= 4:
                        player4alive = True
                    if playerCount >= 5:
                        player5alive = True
                    

        if event.type == TIMER_EVENT:
            countdown_seconds -= 1
            if countdown_seconds <= 0:
                pygame.time.set_timer(TIMER_EVENT, 0) # Stop the timer
                
    if gameState == "title":
        screen.fill("white")
        
        pygame.draw.rect(screen,"lightgrey", titleStart)
    
    if gameState == "menu":
        screen.fill("white")
        
        playerCountDisplay = pygame.Rect(WIDTH/2 - 100, 200, 200, 50)
        pygame.draw.rect(screen, "lightgrey", playerCountDisplay)
        
        jumpCountDisplay = pygame.Rect(WIDTH/2 - 100, 300, 200, 50)
        pygame.draw.rect(screen, "lightgrey", jumpCountDisplay)
        
        gamemodeDisplay = pygame.Rect(WIDTH/2 - 100, 400, 200, 50)
        pygame.draw.rect(screen, "lightgrey", gamemodeDisplay)
        
        def right_tri(r):
            return [(r.left, r.top), (r.left, r.bottom), (r.right, r.centery)]
        def left_tri(r):
            return [(r.right, r.top), (r.right, r.bottom), (r.left, r.centery)]

        pygame.draw.polygon(screen, "lightgrey", right_tri(playerCountIncrement))
        pygame.draw.polygon(screen, "lightgrey", left_tri(playerCountDecrement))
        pygame.draw.polygon(screen, "lightgrey", right_tri(jumpCountIncrement))
        pygame.draw.polygon(screen, "lightgrey", left_tri(jumpCountDecrement))
        pygame.draw.polygon(screen, "lightgrey", right_tri(gamemodeIncrement))
        pygame.draw.polygon(screen, "lightgrey", left_tri(gamemodeDecrement))

        
        font = pygame.font.SysFont(None, 70)
        text_surface = font.render(str(playerCount), True, (0, 0, 0))
        screen.blit(text_surface, (WIDTH/2-10, 200))
        
        text_surface = font.render(str(jumpCount), True, (0, 0, 0))
        screen.blit(text_surface, (WIDTH/2-10, 300))

        text_surface = font.render(str(gamemode), True, (0, 0, 0))
        screen.blit(text_surface, (WIDTH/2-10, 400))

        pygame.draw.rect(screen, "lightgrey", startGame)
        font = pygame.font.SysFont(None, 50)
        text_surface = font.render("Start Game", True, (0, 0, 0))
        screen.blit(text_surface, (WIDTH/2 - 125, 600))


    elif gameState == "playing":
        playerAliveList = [player1alive, player2alive, player3alive, player4alive, player5alive ]

        screen.fill("white")
        
        while not playerAliveList[taggedPlayer]:
            taggedPlayer = random.randint(0, 4)
        
        if player1alive:
            pygame.draw.rect(screen, "red", (player1_pos.x, player1_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
        if player2alive:
            pygame.draw.rect(screen, "blue", (player2_pos.x, player2_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
        if player3alive:
            pygame.draw.rect(screen, "green", (player3_pos.x, player3_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
        if player4alive:
            pygame.draw.rect(screen, "yellow", (player4_pos.x, player4_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
        if player5alive:
            pygame.draw.rect(screen, "orange", (player5_pos.x, player5_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))


        
        text_surface = font.render(str(countdown_seconds), True, (0, 0, 0))
        screen.blit(text_surface, (WIDTH/2 - fontWidth/2, 50))

        tagged_pos = player_positions[taggedPlayer]
        screen.blit(downArrowImage, (tagged_pos.x, tagged_pos.y - PLAYER_HEIGHT - 2))

        for platform in platforms:
            pygame.draw.rect(screen, "black", platform)

        for i in range(len(player_velocities)):
            player_velocities[i] += PLAYER_GRAVITY * dt

        for i in range(len(player_positions)):
            prev_bottom = player_positions[i].y + PLAYER_HEIGHT
            player_positions[i].y += player_velocities[i] * dt
            
            player_rect = pygame.Rect(player_positions[i].x, player_positions[i].y, PLAYER_WIDTH, PLAYER_HEIGHT)
            for platform in platforms:
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

        # Tick tag cooldowns
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
                    if taggedPlayer == i and tag_cooldowns[j] <= 0:
                        taggedPlayer = j
                        tag_cooldowns[j] = TAG_COOLDOWN
                        tag_cooldowns[i] = TAG_COOLDOWN
                        print(taggedPlayer)
                    elif taggedPlayer == j and tag_cooldowns[i] <= 0:
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
                            for platform in platforms:
                                if p_rect.colliderect(platform):
                                    player_positions[pi].y = platform.y - PLAYER_HEIGHT
                                    player_velocities[pi] = 0
                                    p_rect.y = player_positions[pi].y

            
        on_ground = []
        for i in range(len(player_positions)):
            check_rect = pygame.Rect(player_positions[i].x, player_positions[i].y + 1, PLAYER_WIDTH, PLAYER_HEIGHT)
            on_platform = any(check_rect.colliderect(platform) for platform in platforms)
            on_player = any(
                j != i and
                abs((player_positions[i].y + PLAYER_HEIGHT) - player_positions[j].y) <= 2 and
                player_positions[i].x + PLAYER_WIDTH > player_positions[j].x and
                player_positions[i].x < player_positions[j].x + PLAYER_WIDTH
                for j in range(len(player_positions))
            )
        
            on_ground.append(on_platform or on_player)
            
        

        # Reset jump count when landing
        for i in range(len(player_positions)):
            if on_ground[i]:
                player_jump_counts[i] = jumpCount
            elif player_jump_counts[i] == jumpCount:
                player_jump_counts[i] = jumpCount - 1 
                

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player1alive:
            player1_pos.x -= PLAYER_MOVEMENT_SPEED * dt
        if keys[pygame.K_d]:
            player1_pos.x += PLAYER_MOVEMENT_SPEED * dt

        if keys[pygame.K_f] and player2alive:
            player2_pos.x -= PLAYER_MOVEMENT_SPEED * dt
        if keys[pygame.K_h] and player2alive:
            player2_pos.x += PLAYER_MOVEMENT_SPEED * dt

        if keys[pygame.K_j] and player3alive:
            player3_pos.x -= PLAYER_MOVEMENT_SPEED * dt
        if keys[pygame.K_l] and player3alive:
            player3_pos.x += PLAYER_MOVEMENT_SPEED * dt

        if keys[pygame.K_LEFT] and player4alive:
            player4_pos.x -= PLAYER_MOVEMENT_SPEED * dt
        if keys[pygame.K_RIGHT] and player4alive:
            player4_pos.x += PLAYER_MOVEMENT_SPEED * dt

        if keys[pygame.K_SEMICOLON] and player5alive:
            player5_pos.x -= PLAYER_MOVEMENT_SPEED * dt
        if keys[pygame.K_RETURN] and player5alive:
            player5_pos.x += PLAYER_MOVEMENT_SPEED * dt

        for pos in player_positions:
            pos.x = max(0, min(pos.x, WIDTH - PLAYER_WIDTH))
            pos.y = max(0, min(pos.y, HEIGHT - PLAYER_HEIGHT))



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
