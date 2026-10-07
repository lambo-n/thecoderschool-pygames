# Example platformer.
#   platformTemplate.py     -- CustomPlatform, the solid boxes
#   physicsBodyTemplate.py  -- PhysicsBody, all of the collision maths
import pygame
from derrick.derrickPlatform import CustomPlatform
from derrick.derrickPhysicsBody import PhysicsBody
from derrick.derrickLevels import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0

gameState = "levelSelect"
currentLevel = 0

BACKGROUND_COLOR = pygame.Color("#202020")
PANEL_COLOR = pygame.Color("#666768B0")  # #666768B0 # last two digits are alpha: 80 hex = 128 = 50%
PLATFORM_COLOR = pygame.Color("#101010")
PLAYER_COLOR = pygame.Color("#FFB44B")
TEXT_COLOR = pygame.Color("#EFEFEF")

SCREEN_HEIGHT = screen.get_height()
SCREEN_WIDTH = screen.get_width()
SCREEN_AVERAGE_LENGTH = (SCREEN_HEIGHT + SCREEN_WIDTH) / 2

WALK_SPEED = 350 # 300
JUMP_SPEED = 450
WALL_JUMP_SPEED = 400
WALL_KICK = 250
KICK_TIME = 0.05

FONT = pygame.font.SysFont(None, int(SCREEN_AVERAGE_LENGTH / (1080 / 135)))

jumpCount = 2

startButton = pygame.Rect(440, 285, 400, 150)

# pygame.draw.rect ignores alpha, so draw the panel onto its own surface that
# supports transparency (SRCALPHA) and blit that onto the screen instead.
levelPanel = pygame.Rect(90, 200, 1100, 452)
levelPanelSurface = pygame.Surface(levelPanel.size, pygame.SRCALPHA)
levelPanelSurface.fill(PANEL_COLOR)

levelSelectTextPanel = pygame.Rect(340, 37, 600, 100)

levelSelectTextPanelSurface = pygame.Surface(levelSelectTextPanel.size, pygame.SRCALPHA)
levelSelectTextPanelSurface.fill(PANEL_COLOR)

level1Panel = pygame.Rect(110, 220, 196, 196)
level2Panel = pygame.Rect(326, 220, 196, 196)
level3Panel = pygame.Rect(542, 220, 196, 196)
level4Panel = pygame.Rect(758, 220, 196, 196)
level5Panel = pygame.Rect(974, 220, 196, 196)
level6Panel = pygame.Rect(110, 436, 196, 196)
level7Panel = pygame.Rect(326, 436, 196, 196)
level8Panel = pygame.Rect(542, 436, 196, 196)
level9Panel = pygame.Rect(758, 436, 196, 196)
level10Panel = pygame.Rect(974, 436, 196, 196)


# A tall platform is just a platform.  Side collisions work the same way: walk
# into it and you stop, jump beside it and you slide up it, land on it and you
# stand on it.
wall = CustomPlatform(950, 380, 40, 300, "#101010")

# Two platforms sharing an edge.  Walking across the seam is smooth -- nothing
# to snag on, because horizontal and vertical collisions are handled separately.
ledgeA = CustomPlatform(180, 620, 120, 20, "#101010")
ledgeB = CustomPlatform(300, 620, 120, 20, "#101010")

platformList = levels[currentLevel]()

# xpos, ypos, xwidth, yheight -- the top-left corner, same as a platform.
# Any size works; try 12 x 12 or 80 x 140.
player = PhysicsBody(100, 600, 20, 20, PLAYER_COLOR)
kick_timer = 0.0
jump_held = False
font = pygame.font.SysFont(None, 26)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if gameState == "startScreen":
                if startButton.collidepoint(event.pos):
                    gameState = "levelSelect"
            if gameState == "levelSelect":
                if level1Panel.collidepoint(event.pos):
                    gameState = "playing"

    if gameState == "startScreen":

        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, TEXT_COLOR, startButton)

    elif gameState == "levelSelect":

        screen.fill(BACKGROUND_COLOR)

        screen.blit(levelSelectTextPanelSurface, levelSelectTextPanel.topleft)

        text_surface = FONT.render("Level Select", True, pygame.Color("#EFEFEF"))
        screen.blit(text_surface, (SCREEN_WIDTH / 2 - text_surface.get_width()// 2, 50))

        screen.blit(levelPanelSurface, levelPanel.topleft)

        pygame.draw.rect(screen, PLATFORM_COLOR, level1Panel)
        pygame.draw.rect(screen, PLATFORM_COLOR, level2Panel)
        pygame.draw.rect(screen, PLATFORM_COLOR, level3Panel)
        pygame.draw.rect(screen, PLATFORM_COLOR, level4Panel)
        pygame.draw.rect(screen, PLATFORM_COLOR, level5Panel)
        pygame.draw.rect(screen, PLATFORM_COLOR, level6Panel)
        pygame.draw.rect(screen, PLATFORM_COLOR, level7Panel)
        pygame.draw.rect(screen, PLATFORM_COLOR, level8Panel)
        pygame.draw.rect(screen, PLATFORM_COLOR, level9Panel)
        pygame.draw.rect(screen, PLATFORM_COLOR, level10Panel)


    elif gameState == "playing":
        keys = pygame.key.get_pressed()
        jump_down = keys[pygame.K_UP] or keys[pygame.K_w]
        jump_now = jump_down and not jump_held
        jump_held = jump_down
        # Set a velocity; the engine does the moving.  Never move the player
        # directly, or you will move it inside a platform.
        if kick_timer > 0:
            kick_timer -= dt
        else:
            player.vel_x = 0
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player.vel_x = -WALK_SPEED
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player.vel_x = WALK_SPEED
        if player.on_ground:
            jumpCount = 1
        if jump_down and player.on_ground:
            player.jump(JUMP_SPEED)
            jumpCount = 1
        elif jump_now:
            if player.on_ground:
                player.jump(JUMP_SPEED)
            if player.hit_wall_left:
                player.vel_x = WALL_KICK
                player.jump(WALL_JUMP_SPEED)
                kick_timer = KICK_TIME
                jumpCount = 1
            if player.hit_wall_right:
                kick_timer = KICK_TIME
                player.vel_x = -WALL_KICK
                player.jump(WALL_JUMP_SPEED)
                jumpCount = 1
            if jumpCount == 1 and not player.on_ground and not player.hit_wall_right and not player.hit_wall_left:
                player.jump(JUMP_SPEED)
                jumpCount -= 1



        # Gravity, movement, substepping and every collision, in one call.  The
        # screen rect is passed as bounds, so its edges are solid too.
        player.move_and_collide(platformList, dt, bounds=screen.get_rect())

        screen.fill(BACKGROUND_COLOR)

        for platform in platformList:
            platform.update(screen)

        player.draw(screen)

    # Live read-out of what the engine decided this frame.
    # state = "on_ground %s   hit_head %s   walls %s%s   squeezed %s   vel_y %6.1f" % (
    #     player.on_ground,
    #     player.hit_head,
    #     "<" if player.hit_wall_left else "-",
    #     ">" if player.hit_wall_right else "-",
    #     player.squeezed,
    #     player.vel_y,
    # )
    # screen.blit(font.render(state, True, "gray"), (10, 10))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
