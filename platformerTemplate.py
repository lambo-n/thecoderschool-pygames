# Example platformer.
#   platformTemplate.py     -- CustomPlatform, the solid boxes
#   physicsBodyTemplate.py  -- PhysicsBody, all of the collision maths
import pygame
from platformTemplate import CustomPlatform
from physicsBodyTemplate import PhysicsBody

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

WALK_SPEED = 300
JUMP_SPEED = 600

# xpos, ypos, xwidth, yheight
platformGround = CustomPlatform(0, 600, 1280, 20, "white")
platform1 = CustomPlatform(100, 300, 150, 20, "white")
platform2 = CustomPlatform(400, 450, 150, 20, "white")
platform3 = CustomPlatform(700, 150, 150, 20, "white")

# A tall platform is just a platform.  Side collisions work the same way: walk
# into it and you stop, jump beside it and you slide up it, land on it and you
# stand on it.
wall = CustomPlatform(950, 300, 40, 300, "white")

# Two platforms sharing an edge.  Walking across the seam is smooth -- nothing
# to snag on, because horizontal and vertical collisions are handled separately.
ledgeA = CustomPlatform(180, 540, 120, 20, "white")
ledgeB = CustomPlatform(300, 540, 120, 20, "white")

platformList = [platformGround, platform1, platform2, platform3, wall, ledgeA, ledgeB]

# xpos, ypos, xwidth, yheight -- the top-left corner, same as a platform.
# Any size works; try 12 x 12 or 80 x 140.
player = PhysicsBody(620, 320, 40, 40, "gold")

font = pygame.font.SysFont(None, 26)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Set a velocity; the engine does the moving.  Never move the player
    # directly, or you will move it inside a platform.
    player.vel_x = 0
    if keys[pygame.K_LEFT]:
        player.vel_x = -WALK_SPEED
    if keys[pygame.K_RIGHT]:
        player.vel_x = WALK_SPEED
    if keys[pygame.K_UP] and player.on_ground:
        player.jump(JUMP_SPEED)

    # Gravity, movement, substepping and every collision, in one call.  The
    # screen rect is passed as bounds, so its edges are solid too.
    player.move_and_collide(platformList, dt, bounds=screen.get_rect())

    screen.fill("black")

    for platform in platformList:
        platform.update(screen)

    player.draw(screen)

    # Live read-out of what the engine decided this frame.
    state = "on_ground %s   hit_head %s   walls %s%s   squeezed %s   vel_y %6.1f" % (
        player.on_ground,
        player.hit_head,
        "<" if player.hit_wall_left else "-",
        ">" if player.hit_wall_right else "-",
        player.squeezed,
        player.vel_y,
    )
    screen.blit(font.render(state, True, "gray"), (10, 10))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
