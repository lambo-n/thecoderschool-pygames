# Example file showing a circle moving on screen
import pygame
import random
from customPlatform import CustomPlatform

# pygame setup
pygame.init()
#screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
# 1280 x 720
# 640 x 360
clock = pygame.time.Clock()
running = True
dt = 0
gameState = "titleScreen"
playerCount = 2
jumpCount = 2
randomizedPlatforms = 0
gamemode = "normal"
# Normal, Bomb, Freeze, Infection
gamemodeList = ["Normal", "Bomb", "Freeze", "Infection"]
gamemodeIndex = 0
mapList = ["Map A", "Map B", "Map C", "Map D", "Map E"]
mapIndex = 0
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

# Player Variables
PLAYER_HEIGHT = SCREEN_HEIGHT / (720 / 20)
PLAYER_WIDTH = SCREEN_WIDTH / (1280 / 20)
PLAYER_MOVEMENT_SPEED = SCREEN_WIDTH / (1280 / 250)
PLAYER_JUMP_HEIGHT = SCREEN_HEIGHT / (720 / 425)
PLAYER_GRAVITY = SCREEN_HEIGHT / (720 / 720)
PLAYER_TAG_SPEED_MULT = 1.1
PLAYER_TAG_JUMP_MULT = 1
player_jump_mults = [1, 1, 1, 1, 1]
player_speed_mults = [1, 1, 1, 1, 1]

# Platform Variables
platformSpeedNormal = 2.5
movingPlatformSpeedSlow = 1.5
platform21SpeedNormal = platformSpeedNormal
platform23SpeedNormal = platformSpeedNormal


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

# Per-player mode state (Freeze / Infection)
player_frozen = [False, False, False, False, False]
player_infected = [False, False, False, False, False]

# Player colors, used for naming the winner on the results screen
player_colors = ["red", "yellow", "blue", "green", "purple"]
winner_text = ""

player_positions = [player1_pos,
                    player2_pos,
                    player3_pos,
                    player4_pos,
                    player5_pos]

# Remember the spawn points so each new round can reset positions
player_spawns = [pygame.Vector2(p) for p in player_positions]

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

# Platform Types Pink: Can go up and down, Red: Can only go down, Green: Can only go up, Yellow: Only tagger can go through, Orange: Makes you move faster, Blue: Makes you jump higher

# Map A platforms
mapAfloorBase1 = CustomPlatform(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 75))
mapAroof1 = CustomPlatform(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 770), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 50))
mapAplatform1 = CustomPlatform(SCREEN_WIDTH / (1280 / 400), SCREEN_HEIGHT / (720 / 500), SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (1280 / 36), "bounce") # Fall
mapAplatform2 = CustomPlatform(SCREEN_WIDTH / (1280 / 700), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 220), SCREEN_HEIGHT / (720 / 20), "speed") # Climb
mapAplatform3 = CustomPlatform(0, SCREEN_HEIGHT / (720 / 300), SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (720 / 20))
mapAplatform4 = CustomPlatform(SCREEN_WIDTH / (1280 / 100), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 220), SCREEN_HEIGHT / (720 / 20))
mapAplatform5 = CustomPlatform(SCREEN_WIDTH / (1280 / 700), SCREEN_HEIGHT / (720 / 420), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 80))
mapAplatform6 = CustomPlatform(0, SCREEN_HEIGHT / (720 / 500), SCREEN_WIDTH / (1280 / 100), SCREEN_HEIGHT / (720 / 20))
mapAplatform7 = CustomPlatform(SCREEN_WIDTH / (1280 / 120), SCREEN_HEIGHT / (720 / 200), SCREEN_WIDTH / (1280 / 180), SCREEN_HEIGHT / (720 / 20))
mapAplatform8 = CustomPlatform(SCREEN_WIDTH / (1280 / 850), SCREEN_HEIGHT / (720 / 500), SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (720 / 20), "fall") # Phase
mapAplatform9 = CustomPlatform(SCREEN_WIDTH / (1280 / 300), SCREEN_HEIGHT / (720 / 300), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 120))
mapAplatform10 = CustomPlatform(SCREEN_WIDTH / (1280 / 300), SCREEN_HEIGHT / (720 / 300), SCREEN_WIDTH / (1280 / 125), SCREEN_HEIGHT / (720 / 20))
mapAplatform11 = CustomPlatform(SCREEN_WIDTH / (1280 / 585), SCREEN_HEIGHT / (720 / 300), SCREEN_WIDTH / (1280 / 195), SCREEN_HEIGHT / (720 / 20)) # ,---' platform
mapAplatform12 = CustomPlatform(SCREEN_WIDTH / (1280 / 100), SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 120))
mapAplatform13 = CustomPlatform(SCREEN_WIDTH / (1280 / 210), 0, SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 100))
mapAplatform14 = CustomPlatform(SCREEN_WIDTH / (1280 / 210), SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH / (1280 / 100), SCREEN_HEIGHT / (720 / 20))
mapAplatform15 = CustomPlatform(SCREEN_WIDTH / (1280 / 775), SCREEN_HEIGHT / (720 / 245), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 75))
mapAplatform16 = CustomPlatform(SCREEN_WIDTH / (1280 / 775), SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 75))
mapAplatform17 = CustomPlatform(SCREEN_WIDTH / (1280 / 800), SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH / (1280 / 335), SCREEN_HEIGHT / (720 / 20))
mapAplatform18 = CustomPlatform(SCREEN_WIDTH / (1280 / 575), SCREEN_HEIGHT / (720 / 300), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 75))
mapAplatform19 = CustomPlatform(SCREEN_WIDTH / (1280 / 900), SCREEN_HEIGHT / (720 / 200), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 120)) # | middle right side
mapAplatform20 = CustomPlatform(SCREEN_WIDTH / (1280 / 900), SCREEN_HEIGHT / (720 / 200), SCREEN_WIDTH / (1280 / 125), SCREEN_HEIGHT / (720 / 20))
mapAplatform21 = CustomPlatform(SCREEN_WIDTH / (1280 / 1025), SCREEN_HEIGHT / (720 / 300), SCREEN_WIDTH / (1280 / 130), SCREEN_HEIGHT / (720 / 20), "bounce") # Bounce
mapAplatform22 = CustomPlatform(SCREEN_WIDTH / (1280 / 1135), SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 120))
mapAplatform23 = CustomPlatform(SCREEN_WIDTH / (1280 / 310), SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH / (1280 / 150), SCREEN_HEIGHT / (720 / 20), "phase")

# Map B platforms
mapBfloorBase1 = CustomPlatform(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 75))
mapBroof1 = CustomPlatform(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 770), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 50))
mapBplatform1 = CustomPlatform(SCREEN_WIDTH / (1280 / 1100), SCREEN_HEIGHT / (720 / 550), SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (720 / 20))
mapBplatform2 = CustomPlatform(SCREEN_WIDTH / (1280 / 1100), SCREEN_HEIGHT / (720 / 275), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 145))
mapBplatform3 = CustomPlatform(SCREEN_WIDTH / (1280 / 1075), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 40), SCREEN_HEIGHT / (720 / 20))
mapBplatform4 = CustomPlatform(SCREEN_WIDTH / (1280 / 1190), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 100), SCREEN_HEIGHT / (720 / 20))
mapBplatform5 = CustomPlatform(SCREEN_WIDTH / (1280 / 1100), SCREEN_HEIGHT / (720 / 475), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 75))
mapBplatform6 = CustomPlatform(SCREEN_WIDTH / (1280 / 1190), SCREEN_HEIGHT / (720 / 475), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 20))
mapBplatform7 = CustomPlatform(SCREEN_WIDTH / (1280 / 1120), SCREEN_HEIGHT / (720 / 325), SCREEN_WIDTH / (1280 / 25), SCREEN_HEIGHT / (720 / 20))
mapBplatform8 = CustomPlatform(SCREEN_WIDTH / (1280 / 1100), SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 145))
mapBplatform9 = CustomPlatform(SCREEN_WIDTH / (1280 / 465), SCREEN_HEIGHT / (720 / 75), SCREEN_WIDTH / (1280 / 25), SCREEN_HEIGHT / (720 / 20))
mapBplatform10 = CustomPlatform(SCREEN_WIDTH / (1280 / 570), SCREEN_HEIGHT / (720 / 75), SCREEN_WIDTH / (1280 / 25), SCREEN_HEIGHT / (720 / 20))
mapBplatform11 = CustomPlatform(SCREEN_WIDTH / (1280 / 450), SCREEN_HEIGHT / (720 / 75), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 150))
mapBplatform12 = CustomPlatform(SCREEN_WIDTH / (1280 / 585), SCREEN_HEIGHT / (720 / 75), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 150))
mapBplatform13 = CustomPlatform(SCREEN_WIDTH / (1280 / 465), SCREEN_HEIGHT / (720 / 205), SCREEN_WIDTH / (1280 / 25), SCREEN_HEIGHT / (720 / 20))
mapBplatform14 = CustomPlatform(SCREEN_WIDTH / (1280 / 570), SCREEN_HEIGHT / (720 / 205), SCREEN_WIDTH / (1280 / 25), SCREEN_HEIGHT / (720 / 20))

# Map C platforms
mapCfloorBase1 = CustomPlatform(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 75))

# Map D platforms
mapDfloorBase1 = CustomPlatform(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 75))

# Map E platforms
mapEfloorBase1 = CustomPlatform(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 75))

mapA = [mapAfloorBase1, mapAroof1, mapAplatform1, mapAplatform2, mapAplatform3, mapAplatform4, mapAplatform5,
        mapAplatform6, mapAplatform7, mapAplatform8, mapAplatform9, mapAplatform10, mapAplatform11, mapAplatform12,
        mapAplatform13, mapAplatform14, mapAplatform15, mapAplatform16, mapAplatform17, mapAplatform18, mapAplatform19,
        mapAplatform20, mapAplatform21, mapAplatform22, mapAplatform23]
mapB = [mapBfloorBase1, mapBroof1, mapBplatform1, mapBplatform2, mapBplatform3, mapBplatform4, mapBplatform5,
        mapBplatform6, mapBplatform7, mapBplatform8, mapBplatform9, mapBplatform10, mapBplatform11, mapBplatform12,
        mapBplatform13, mapBplatform14]
mapC = [mapCfloorBase1]
mapD = [mapDfloorBase1]
mapE = [mapEfloorBase1]
mapBfloorBase1 = CustomPlatform(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 75))
mapBroof1 = CustomPlatform(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 770), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 50))
mapBplatform1 = CustomPlatform(SCREEN_WIDTH / (1280 / 1100), SCREEN_HEIGHT / (720 / 550), SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (720 / 20))
mapBplatform2 = CustomPlatform(SCREEN_WIDTH / (1280 / 1100), SCREEN_HEIGHT / (720 / 275), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 145))
mapBplatform3 = CustomPlatform(SCREEN_WIDTH / (1280 / 1075), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 40), SCREEN_HEIGHT / (720 / 20))
mapBplatform4 = CustomPlatform(SCREEN_WIDTH / (1280 / 1190), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 100), SCREEN_HEIGHT / (720 / 20))
mapBplatform5 = CustomPlatform(SCREEN_WIDTH / (1280 / 1100), SCREEN_HEIGHT / (720 / 475), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 75))
mapBplatform6 = CustomPlatform(SCREEN_WIDTH / (1280 / 1190), SCREEN_HEIGHT / (720 / 475), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 20))
mapBplatform7 = CustomPlatform(SCREEN_WIDTH / (1280 / 1120), SCREEN_HEIGHT / (720 / 325), SCREEN_WIDTH / (1280 / 25), SCREEN_HEIGHT / (720 / 20))
mapBplatform8 = CustomPlatform(SCREEN_WIDTH / (1280 / 1100), SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 145))
mapBplatform9 = CustomPlatform(SCREEN_WIDTH / (1280 / 465), SCREEN_HEIGHT / (720 / 75), SCREEN_WIDTH / (1280 / 25), SCREEN_HEIGHT / (720 / 20))
mapBplatform10 = CustomPlatform(SCREEN_WIDTH / (1280 / 570), SCREEN_HEIGHT / (720 / 75), SCREEN_WIDTH / (1280 / 25), SCREEN_HEIGHT / (720 / 20))
mapBplatform11 = CustomPlatform(SCREEN_WIDTH / (1280 / 450), SCREEN_HEIGHT / (720 / 75), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 150))
mapBplatform12 = CustomPlatform(SCREEN_WIDTH / (1280 / 585), SCREEN_HEIGHT / (720 / 75), SCREEN_WIDTH / (1280 / 20), SCREEN_HEIGHT / (720 / 150))
mapBplatform13 = CustomPlatform(SCREEN_WIDTH / (1280 / 465), SCREEN_HEIGHT / (720 / 205), SCREEN_WIDTH / (1280 / 25), SCREEN_HEIGHT / (720 / 20))
mapBplatform14 = CustomPlatform(SCREEN_WIDTH / (1280 / 570), SCREEN_HEIGHT / (720 / 205), SCREEN_WIDTH / (1280 / 25), SCREEN_HEIGHT / (720 / 20))

# Map C platforms
mapCfloorBase1 = CustomPlatform(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 75))

# Map D platforms
mapDfloorBase1 = CustomPlatform(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 75))

# Map E platforms
mapEfloorBase1 = CustomPlatform(0, SCREEN_HEIGHT - SCREEN_HEIGHT / (720 / 100), SCREEN_WIDTH, SCREEN_HEIGHT / (720 / 75))

mapA = [mapAfloorBase1, mapAroof1, mapAplatform1, mapAplatform2, mapAplatform3, mapAplatform4, mapAplatform5,
        mapAplatform6, mapAplatform7, mapAplatform8, mapAplatform9, mapAplatform10, mapAplatform11, mapAplatform12,
        mapAplatform13, mapAplatform14, mapAplatform15, mapAplatform16, mapAplatform17, mapAplatform18, mapAplatform19,
        mapAplatform20, mapAplatform21, mapAplatform22, mapAplatform23]
mapB = [mapBfloorBase1, mapBroof1, mapBplatform1, mapBplatform2, mapBplatform3, mapBplatform4, mapBplatform5,
        mapBplatform6, mapBplatform7, mapBplatform8, mapBplatform9, mapBplatform10, mapBplatform11, mapBplatform12,
        mapBplatform13, mapBplatform14]
mapC = [mapCfloorBase1]
mapD = [mapDfloorBase1]
mapE = [mapEfloorBase1]

map = [mapA, mapB, mapC, mapD, mapE]

# Extra hand-placed custom platforms, shared across every map
#custPlatform1 = CustomPlatform(200, 200, 100, 20, "phase")
#customPlatforms = [custPlatform1]


downArrowImage = pygame.image.load("arrow1.png").convert_alpha()
downArrowImage = pygame.transform.scale(downArrowImage, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Menu UI Elements
gamemodeIncrement = pygame.Rect(SCREEN_WIDTH / 2 + 280, 230, 75, 75)
gameModeDecrement = pygame.Rect(SCREEN_WIDTH / 2 - 353, 230, 75, 75)

playerCountIncrement = pygame.Rect(SCREEN_WIDTH / 2 + 280, 325, 75, 75)
playerCountDecrement = pygame.Rect(SCREEN_WIDTH / 2 - 353, 325, 75, 75)

jumpCountIncrement = pygame.Rect(SCREEN_WIDTH / 2 + 280, 420, 75, 75)
jumpCountDecrement = pygame.Rect(SCREEN_WIDTH / 2 - 353, 420, 75, 75)

mapIncrement = pygame.Rect(SCREEN_WIDTH / 2 + 280, 515, 75, 75)
mapDecrement = pygame.Rect(SCREEN_WIDTH / 2 - 353, 515, 75, 75)


menuStart = pygame.Rect((SCREEN_WIDTH / (1280 / 440), SCREEN_HEIGHT / (720 / 400), SCREEN_WIDTH / (1280 / 400), SCREEN_HEIGHT / (720 / 150)))

startGame = pygame.Rect((SCREEN_WIDTH / 2 - 250, 610, 500, 75))
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and gameState == "playing":
            aliveList = [player1_alive, player2_alive, player3_alive, player4_alive, player5_alive]
            jump_bindings = [pygame.K_w, pygame.K_t, pygame.K_i, pygame.K_LEFTBRACKET, pygame.K_UP]
            for idx, key in enumerate(jump_bindings):
                if event.key == key and player_jump_counts[idx] > 0 and aliveList[idx] and not player_frozen[idx]:
                    player_velocities[idx] = -PLAYER_JUMP_HEIGHT
                    player_jump_counts[idx] -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if gameState == "titleScreen":
                if menuStart.collidepoint(event.pos):
                    gameState = "menu"

            if gameState == "results":
                # Click anywhere to head back to the menu for another round
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
                elif mapIncrement.collidepoint(event.pos):
                    if mapIndex == 4:
                        mapIndex = 0
                    else:
                        mapIndex += 1
                elif mapDecrement.collidepoint(event.pos):
                    if mapIndex == 0:
                        mapIndex = 4
                    else:
                        mapIndex -= 1

                elif startGame.collidepoint(event.pos):
                    gameState = "playing"
                    gamemode = gamemodeList[gamemodeIndex]

                    player1_alive = playerCount >= 1
                    player2_alive = playerCount >= 2
                    player3_alive = playerCount >= 3
                    player4_alive = playerCount >= 4
                    player5_alive = playerCount >= 5

                    # Reset round state
                    player_frozen = [False, False, False, False, False]
                    player_infected = [False, False, False, False, False]
                    tag_cooldowns = [0.0, 0.0, 0.0, 0.0, 0.0]
                    player_velocities = [0, 0, 0, 0, 0]
                    player_jump_counts = [jumpCount, jumpCount, jumpCount, jumpCount, jumpCount]
                    winner_text = ""

                    # Move players back to their spawn points
                    for i in range(len(player_positions)):
                        player_positions[i].update(player_spawns[i])

                    # Pick a random starting "it" among the players in this round
                    taggedPlayer = random.randint(0, playerCount - 1)
                    if gamemode == "Infection":
                        player_infected[taggedPlayer] = True

                    # Start the countdown fresh
                    countdown_seconds = 100
                    pygame.time.set_timer(TIMER_EVENT, 1000)



        if event.type == TIMER_EVENT:
            if gameState == "playing" and countdown_seconds > 0:
                countdown_seconds -= 1
    if gameState == "titleScreen": # Checks if the gamestate is titleScreen

        screen.fill("#419af2") # Background
        pygame.draw.rect(screen, "white", (SCREEN_WIDTH / (1280 / 200), SCREEN_HEIGHT / (720 / 50), SCREEN_WIDTH / (1280 / 840), SCREEN_HEIGHT / (720 / 200))) # Tag text
        pygame.draw.rect(screen, "white", menuStart) # Tag text

    elif gameState == "menu": # Checks if the gamestate is menu

        screen.fill("#419af2") # Background
        

        
        pygame.draw.rect(screen, "white", (SCREEN_WIDTH / 2 - 420, 25, 840, 175)) # Tag text
        pygame.draw.rect(screen, "white", (SCREEN_WIDTH / 2 - 250, 230, 500, 70)) # Type of gamemode
        pygame.draw.rect(screen, "white", (SCREEN_WIDTH / 2 - 250, 325, 500, 70)) # Amount of players box
        pygame.draw.rect(screen, "white", (SCREEN_WIDTH / 2 - 250, 420, 500, 70)) # Amount of Double Jumps
        pygame.draw.rect(screen, "white", (SCREEN_WIDTH / 2 - 250, 515, 500, 70)) # Map

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

        # Map cycle increment and decrement
        pygame.draw.polygon(screen, "white", right_tri(mapIncrement))
        pygame.draw.polygon(screen, "white", left_tri(mapDecrement))


        text_surface = FONT.render(str(gamemodeList[gamemodeIndex]), True, (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH / 2 - text_surface.get_width()// 2, 240))

        text_surface = FONT.render(str(playerCount) + " Players", True, (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH / 2 - text_surface.get_width()// 2, 335))

        jumpText = " Jumps" if jumpCount > 1 else " Jump"
        text_surface = FONT.render(str(jumpCount)+ jumpText, True, (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH / 2 - text_surface.get_width()// 2, 430))

        text_surface = FONT.render(str(mapList[mapIndex]), True, (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH / 2 - text_surface.get_width()// 2, 525))

    elif gameState == "playing": # Checks if the gamestate is playing
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("gray")

        # All platforms the players can stand on this frame: the current map's
        # platforms plus any hand-placed custom platforms
        active_platforms = map[mapIndex]# + customPlatforms

        playerAliveList = [player1_alive, player2_alive, player3_alive, player4_alive, player5_alive]

        while not playerAliveList[taggedPlayer]:
            taggedPlayer = random.randint(0, 4)

        # pygame.draw.circle(screen, "red", player1_pos, 40)
        # pygame.draw.circle(screen, "blue", player2_pos, 40)
        # pygame.draw.circle(screen, "green", player3_pos, 40)
        # pygame.draw.circle(screen, "yellow", player4_pos, 40)
        # pygame.draw.circle(screen, "orange", player5_pos, 40)

        for i in range(len(player_positions)):
            if not playerAliveList[i]:
                continue
            pygame.draw.rect(screen, player_colors[i], (player_positions[i].x, player_positions[i].y, PLAYER_WIDTH, PLAYER_HEIGHT))
            # Frozen players get an icy outline so you can tell who's stuck
            if player_frozen[i]:
                pygame.draw.rect(screen, "cyan", (player_positions[i].x, player_positions[i].y, PLAYER_WIDTH, PLAYER_HEIGHT), 4)

        # Arrow over whoever is "it" (over every infected player in Infection mode)
        if gamemode == "Infection":
            for i in range(len(player_positions)):
                if playerAliveList[i] and player_infected[i]:
                    pos = player_positions[i]
                    screen.blit(downArrowImage, (pos.x, pos.y - PLAYER_HEIGHT - 2))
        else:
            tagged_pos = player_positions[taggedPlayer]
            screen.blit(downArrowImage, (tagged_pos.x, tagged_pos.y - PLAYER_HEIGHT - 2))

        text_surface = FONT.render(str(countdown_seconds), True, (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH / 2 - fontWidth / 2, (SCREEN_HEIGHT / (1280 / 25))))
        
        # Moving Platforms
        if (mapAplatform21.bottom >= SCREEN_HEIGHT / (720 / 400) or mapAplatform21.top <= SCREEN_HEIGHT / (720 / 200)):
            platform21SpeedNormal *= -1

        mapAplatform21.move_ip(0, platform21SpeedNormal)

        for platform in active_platforms:
            pygame.draw.rect(screen, platform.color, platform)

        for i in range(len(player_velocities)):
            player_velocities[i] += PLAYER_GRAVITY * dt

        # dDown Key Brinders
        down_bindings = [pygame.K_s, pygame.K_g, pygame.K_k, pygame.K_QUOTE, pygame.K_DOWN]
        held_keys = pygame.key.get_pressed()
        player_dropping = [held_keys[down_bindings[i]] for i in range(len(player_positions))]

        for i in range(len(player_positions)):
            prev_bottom = player_positions[i].y + PLAYER_HEIGHT
            player_positions[i].y += player_velocities[i] * dt
            
            player_rect = pygame.Rect(player_positions[i].x, player_positions[i].y, PLAYER_WIDTH, PLAYER_HEIGHT)
            for platform in active_platforms:
                prect = platform
                if player_rect.colliderect(prect):
                    
                    player_speed_mults[i] = 1
                    #player_jump_mults[i] = 1
                    # Resets Multipliers upon collision

                    if getattr(platform, "type", "normal") == "phase":
                        if (player_velocities[i] >= 0
                            and prev_bottom <= prect.top + 1
                            and not player_dropping[i]):
                            player_positions[i].y = prect.y - PLAYER_HEIGHT
                            player_velocities[i] = 0
                            player_rect.y = player_positions[i].y
                        continue
                        # Purple Platforms
                    if getattr(platform, "type", "normal") == "climb":
                        if (prev_bottom <= prect.top + 1):
                            player_positions[i].y = prect.y - PLAYER_HEIGHT
                            player_velocities[i] = 0
                            player_rect.y = player_positions[i].y
                        elif (player_velocities[i] >= 0 and player_rect.bottom - prect.top <= 20):
                            player_positions[i].y = prect.y - PLAYER_HEIGHT
                            player_velocities[i] = 0
                            player_rect.y = player_positions[i].y
                        # Green Platforms

                        continue
                    if getattr(platform, "type", "normal") == "fall":
                        #if (prect.top >= player_rect.bottom and 
                            # prect.bottom <= player_rect.top):
                                # continue
                        if (player_velocities[i] >= 0 and 
                            prev_bottom <= prect.top + 1 and 
                            not player_dropping[i]):
                            player_positions[i].y = prect.y - PLAYER_HEIGHT
                            player_velocities[i] = 0
                            player_rect.y = player_positions[i].y
                        
                        elif (player_velocities[i] < 0 and 
                            prect.bottom - player_rect.top <= 20):
                            player_rect.top = prect.bottom # If the bottom player is on the top of the platform
                            player_positions[i].y = player_rect.y
                            player_velocities[i] = -player_velocities[i] * 0.3

                        if (not player_rect.right >= platform.left or 
                              not player_rect.left <= platform.right):
                            if (player_rect.right <= prect.left):
                                    player_rect.right = prect.left
                            else: player_rect.left = prect.right
                                # Going into the side of the platform
                        player_positions[i].x = player_rect.x
                        continue
                        # Pink Platforms
                    if getattr(platform, "type", "normal") == "bounce":
                        if (prev_bottom <= prect.top + 1):
                            player_jump_mults[i] = 2
                        if player_velocities[i] >= 0 and player_rect.bottom - prect.top <= 20:
                            player_jump_mults[i] = 2
                            player_positions[i].y = prect.y - PLAYER_HEIGHT
                            player_velocities[i] = 0
                            player_rect.y = player_positions[i].y
                            # Going Down into the Platform
                        elif player_velocities[i] < 0 and prect.bottom - player_rect.top <= 20:
                            player_rect.top = prect.bottom # If the bottom player is at the top of the platform
                            player_positions[i].y = player_rect.y
                            player_velocities[i] = -player_velocities[i] * 0.3
                            # Going Up into the Platform
                        else:
                            if player_rect.centerx < prect.centerx:
                                player_rect.right = prect.left
                            else: 
                                player_rect.left = prect.right
                            # Going into the side of the platform
                            #print(player_jump_mults[i])
                        continue
                    if getattr(platform, "type", "normal") == "speed":
                        if player_velocities[i] >= 0 and player_rect.bottom - prect.top <= 20:
                            player_positions[i].y = prect.y - PLAYER_HEIGHT
                            player_velocities[i] = 0
                            player_rect.y = player_positions[i].y
                            player_speed_mults[i] = 1.5
                            # Going Down into the Platform
                        elif player_velocities[i] < 0 and prect.bottom - player_rect.top <= 20:
                            player_rect.top = prect.bottom # If the bottom player is at the top of the platform
                            player_positions[i].y = player_rect.y
                            player_velocities[i] = -player_velocities[i] * 0.3
                            # Going Up into the Platform
                        else:
                            if player_rect.centerx < prect.centerx:
                                player_rect.right = prect.left
                            else: player_rect.left = prect.right
                            # Going into the side of the platform
                        player_positions[i].x = player_rect.x
                        continue
                    if getattr(platform, "type", "normal") == "danger":
                        if player_velocities[i] >= 0 and player_rect.bottom - prect.top <= 20:
                            player_positions[i].y = prect.y - PLAYER_HEIGHT
                            player_velocities[i] = 0
                            player_rect.y = player_positions[i].y
                            # Going Down into the Platform
                            taggedPlayer = i
                        elif player_velocities[i] < 0 and prect.bottom - player_rect.top <= 20:
                            player_rect.top = prect.bottom # If the bottom player is at the top of the platform
                            player_positions[i].y = player_rect.y
                            player_velocities[i] = -player_velocities[i] * 0.3
                            # Going Up into the Platform
                            taggedPlayer = i
                        else:
                            if player_rect.centerx < prect.centerx:
                                player_rect.right = prect.left
                            else: player_rect.left = prect.right
                            # Going into the side of the platform
                            taggedPlayer = i
                        continue
                    player_positions[i].x = player_rect.x
                    if getattr(platform, "type", "normal") == "crash":
                        if (player_velocities[i] >= 0
                            and prev_bottom <= prect.top + 1):
                            player_velocities[i] = 0/0
                        continue


                    if player_velocities[i] >= 0 and player_rect.bottom - prect.top <= 20:
                        player_positions[i].y = prect.y - PLAYER_HEIGHT
                        player_velocities[i] = 0
                        player_rect.y = player_positions[i].y
                        # Going Down into the Platform
                    elif player_velocities[i] < 0 and prect.bottom - player_rect.top <= 20:
                        player_rect.top = prect.bottom # If the bottom player is at the top of the platform
                        player_positions[i].y = player_rect.y
                        player_velocities[i] = -player_velocities[i] * 0.3
                        # Going Up into the Platform
                    else:
                        if player_rect.centerx < prect.centerx:
                            player_rect.right = prect.left
                        else: player_rect.left = prect.right
                        # Going into the side of the platform
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
                    # --- Mode-specific interaction when two players touch ---
                    if gamemode in ("Normal", "Bomb"):
                        # The tag (or bomb) passes from "it" to whoever they touch
                        if taggedPlayer == i and tag_cooldowns[i] <= 0:
                            taggedPlayer = j
                            tag_cooldowns[i] = TAG_COOLDOWN
                            tag_cooldowns[j] = TAG_COOLDOWN
                        elif taggedPlayer == j and tag_cooldowns[j] <= 0:
                            taggedPlayer = i
                            tag_cooldowns[i] = TAG_COOLDOWN
                            tag_cooldowns[j] = TAG_COOLDOWN
                    elif gamemode == "Freeze":
                        # "it" freezes a free runner; free runners thaw frozen ones
                        if taggedPlayer == i and j != taggedPlayer and not player_frozen[j]:
                            player_frozen[j] = True
                        elif taggedPlayer == j and i != taggedPlayer and not player_frozen[i]:
                            player_frozen[i] = True
                        elif i != taggedPlayer and j != taggedPlayer:
                            if player_frozen[i] and not player_frozen[j]:
                                player_frozen[i] = False
                            elif player_frozen[j] and not player_frozen[i]:
                                player_frozen[j] = False
                    elif gamemode == "Infection":
                        # Infection spreads to whoever an infected player touches
                        if player_infected[i] and not player_infected[j]:
                            player_infected[j] = True
                        elif player_infected[j] and not player_infected[i]:
                            player_infected[i] = True
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
                            for platform in active_platforms:
                                if p_rect.colliderect(platform):
                                    player_positions[pi].y = platform.y - PLAYER_HEIGHT
                                    player_velocities[pi] = 0
                                    p_rect.y = player_positions[pi].y

            
        on_ground = []
        for i in range(len(player_positions)):
            check_rect = pygame.Rect(player_positions[i].x, player_positions[i].y + 1, PLAYER_WIDTH, PLAYER_HEIGHT)
            on_platform = any(check_rect.colliderect(platform) for platform in active_platforms)
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
                player_jump_mults[i] = 1
                player_jump_counts[i] = jumpCount - 1

        keys = pygame.key.get_pressed()
        if player1_alive and not player_frozen[0]:
            if keys[pygame.K_w] and on_ground[0]:
                # player_jump_mults[0] = 1
                player_velocities[0] = -PLAYER_JUMP_HEIGHT * PLAYER_TAG_JUMP_MULT * player_jump_mults[0]
                #print(player_velocities[0])
            if keys[pygame.K_a]:
                player1_pos.x -= PLAYER_MOVEMENT_SPEED * PLAYER_TAG_SPEED_MULT * player_speed_mults[0] * dt
            if keys[pygame.K_d]:
                player1_pos.x += PLAYER_MOVEMENT_SPEED * PLAYER_TAG_SPEED_MULT * player_speed_mults[0] * dt

        if player2_alive and not player_frozen[1]:
            if keys[pygame.K_t] and on_ground[1]:
                # player_jump_mults[1] = 1
                player_velocities[1] = -PLAYER_JUMP_HEIGHT * PLAYER_TAG_JUMP_MULT * player_jump_mults[1]
            if keys[pygame.K_f]:
                player2_pos.x -= PLAYER_MOVEMENT_SPEED * PLAYER_TAG_SPEED_MULT * player_speed_mults[1] * dt
            if keys[pygame.K_h]:
                player2_pos.x += PLAYER_MOVEMENT_SPEED * PLAYER_TAG_SPEED_MULT * player_speed_mults[1] * dt
        
        if player3_alive and not player_frozen[2]:
            if keys[pygame.K_i] and on_ground[2]:
                # player_jump_mults[2] = 1
                player_velocities[2] = -PLAYER_JUMP_HEIGHT * PLAYER_TAG_JUMP_MULT * player_jump_mults[2]
            if keys[pygame.K_j]:
                player3_pos.x -= PLAYER_MOVEMENT_SPEED * PLAYER_TAG_SPEED_MULT * player_speed_mults[2] * dt
            if keys[pygame.K_l]:
                player3_pos.x += PLAYER_MOVEMENT_SPEED * PLAYER_TAG_SPEED_MULT * player_speed_mults[2] * dt
        
        if player4_alive and not player_frozen[3]:
            if keys[pygame.K_LEFTBRACKET] and on_ground[3]:
                # player_jump_mults[3] = 1
                player_velocities[3] = -PLAYER_JUMP_HEIGHT * PLAYER_TAG_JUMP_MULT * player_jump_mults[3]
                if keys[pygame.K_SEMICOLON]:
                    player4_pos.x -= PLAYER_MOVEMENT_SPEED * PLAYER_TAG_SPEED_MULT * player_speed_mults[3] * dt
                if keys[pygame.K_RETURN]:
                    player4_pos.x += PLAYER_MOVEMENT_SPEED * PLAYER_TAG_SPEED_MULT * player_speed_mults[3] * dt

        if player5_alive and not player_frozen[4]:
            if keys[pygame.K_UP] and on_ground[4]:
                # player_jump_mults[4] = 1
                player_velocities[4] = -PLAYER_JUMP_HEIGHT * PLAYER_TAG_JUMP_MULT * player_jump_mults[4]
                if keys[pygame.K_LEFT]:
                    player5_pos.x -= PLAYER_MOVEMENT_SPEED * PLAYER_TAG_SPEED_MULT * player_speed_mults[4] * dt
                if keys[pygame.K_RIGHT]:
                    player5_pos.x += PLAYER_MOVEMENT_SPEED * PLAYER_TAG_SPEED_MULT * player_speed_mults[4] * dt
            
        for pos in player_positions:
            pos.x = max(0, min(pos.x, SCREEN_WIDTH - PLAYER_WIDTH))
            pos.y = max(0, min(pos.y, SCREEN_HEIGHT - PLAYER_HEIGHT))

        # --- Win / round-end conditions per gamemode ---
        playerAliveList = [player1_alive, player2_alive, player3_alive, player4_alive, player5_alive]
        alive_indices = [i for i in range(len(playerAliveList)) if playerAliveList[i]]

        if gamemode == "Normal":
            if countdown_seconds <= 0:
                winner_text = "Time's up! " + player_colors[taggedPlayer].capitalize() + " was IT and loses!"
                gameState = "results"
                pygame.time.set_timer(TIMER_EVENT, 0)

        elif gamemode == "Bomb":
            if countdown_seconds <= 0:
                # The bomb goes off on whoever is "it"
                if taggedPlayer == 0: player1_alive = False
                elif taggedPlayer == 1: player2_alive = False
                elif taggedPlayer == 2: player3_alive = False
                elif taggedPlayer == 3: player4_alive = False
                elif taggedPlayer == 4: player5_alive = False
                playerAliveList = [player1_alive, player2_alive, player3_alive, player4_alive, player5_alive]
                alive_indices = [i for i in range(len(playerAliveList)) if playerAliveList[i]]
                if len(alive_indices) <= 1:
                    winner_text = (player_colors[alive_indices[0]].capitalize() + " wins!") if alive_indices else "Nobody wins!"
                    gameState = "results"
                    pygame.time.set_timer(TIMER_EVENT, 0)
                else:
                    # Hand the bomb to a random survivor and reset the timer
                    taggedPlayer = random.choice(alive_indices)
                    tag_cooldowns = [0.0, 0.0, 0.0, 0.0, 0.0]
                    countdown_seconds = 100
                    pygame.time.set_timer(TIMER_EVENT, 1000)

        elif gamemode == "Freeze":
            runners = [i for i in alive_indices if i != taggedPlayer]
            if runners and all(player_frozen[i] for i in runners):
                winner_text = player_colors[taggedPlayer].capitalize() + " (IT) froze everyone and wins!"
                gameState = "results"
                pygame.time.set_timer(TIMER_EVENT, 0)
            elif countdown_seconds <= 0:
                winner_text = "Time's up! The runners escaped and win!"
                gameState = "results"
                pygame.time.set_timer(TIMER_EVENT, 0)

        elif gamemode == "Infection":
            uninfected = [i for i in alive_indices if not player_infected[i]]
            if len(uninfected) <= 1 or countdown_seconds <= 0:
                if len(uninfected) == 1:
                    winner_text = player_colors[uninfected[0]].capitalize() + " survived and wins!"
                elif len(uninfected) == 0:
                    winner_text = "Everyone got infected!"
                else:
                    winner_text = "Time's up! Survivors win: " + ", ".join(player_colors[i].capitalize() for i in uninfected)
                gameState = "results"
                pygame.time.set_timer(TIMER_EVENT, 0)

    elif gameState == "results": # Checks if the gamestate is results

        screen.fill("#419af2")
        text_surface = FONT.render(winner_text, True, (255, 255, 255))
        screen.blit(text_surface, (SCREEN_WIDTH / 2 - text_surface.get_width() // 2, SCREEN_HEIGHT / 2 - 60))
        info_surface = FONT.render("Click to return to menu", True, (255, 255, 255))
        screen.blit(info_surface, (SCREEN_WIDTH / 2 - info_surface.get_width() // 2, SCREEN_HEIGHT / 2 + 20))


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
