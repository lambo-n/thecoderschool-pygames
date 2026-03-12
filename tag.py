# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

PLAYER_HEIGHT = 40
PLAYER_WIDTH = 40

player1_pos = pygame.Vector2(200, screen.get_height() / 2)
player2_pos = pygame.Vector2(400, screen.get_height() / 2)
player3_pos = pygame.Vector2(600, screen.get_height() / 2)
player4_pos = pygame.Vector2(800, screen.get_height() / 2)
player5_pos = pygame.Vector2(1000, screen.get_height() / 2)

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

floorBase = pygame.Rect(0, screen.get_height() - 100, screen.get_width(), 100)
platform1 = pygame.Rect(300, 500, 200, 10)
platform2 = pygame.Rect(700, 400, 200, 10)

platforms = [floorBase, platform1, platform2]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.rect(screen, "red", (player1_pos.x, player1_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(screen, "blue", (player2_pos.x, player2_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(screen, "green", (player3_pos.x, player3_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(screen, "yellow", (player4_pos.x, player4_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.draw.rect(screen, "orange", (player5_pos.x, player5_pos.y, PLAYER_WIDTH, PLAYER_HEIGHT))
    
    
    for platform in platforms:
        pygame.draw.rect(screen, "black", platform)
    
    for i in range(len(player_velocities)):
        player_velocities[i] += 475 * dt

    for i in range(len(player_positions)):
        prev_bottom = player_positions[i].y + PLAYER_HEIGHT
        player_positions[i].y += player_velocities[i] * dt

        player_rect = pygame.Rect(player_positions[i].x, player_positions[i].y, PLAYER_WIDTH, PLAYER_HEIGHT)
        for platform in platforms:
            if player_rect.colliderect(platform) and player_velocities[i] >= 0 and prev_bottom <= platform.y + 1:
                player_positions[i].y = platform.y - PLAYER_HEIGHT
                player_velocities[i] = 0
                player_rect.y = player_positions[i].y
        
        

    # Player-to-player collisions
    for i in range(len(player_positions)):
        player_rect = pygame.Rect(player_positions[i].x, player_positions[i].y, PLAYER_WIDTH, PLAYER_HEIGHT)
        for j in range(i + 1, len(player_positions)):
            other_rect = pygame.Rect(player_positions[j].x, player_positions[j].y, PLAYER_WIDTH, PLAYER_HEIGHT)
            if player_rect.colliderect(other_rect):
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

    # Check which players are on a platform
    on_ground = []
    for i in range(len(player_positions)):
        check_rect = pygame.Rect(player_positions[i].x, player_positions[i].y + 1, PLAYER_WIDTH, PLAYER_HEIGHT)
        on_ground.append(any(check_rect.colliderect(platform) for platform in platforms))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and on_ground[0]:
        player_velocities[0] = -300
    if keys[pygame.K_a]:
        player1_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player1_pos.x += 300 * dt

    if keys[pygame.K_t] and on_ground[1]:
        player_velocities[1] = -300
    if keys[pygame.K_f]:
        player2_pos.x -= 300 * dt
    if keys[pygame.K_h]:
        player2_pos.x += 300 * dt

    if keys[pygame.K_i] and on_ground[2]:
        player_velocities[2] = -300
    if keys[pygame.K_j]:
        player3_pos.x -= 300 * dt
    if keys[pygame.K_l]:
        player3_pos.x += 300 * dt

    if keys[pygame.K_UP] and on_ground[3]:
        player_velocities[3] = -300
    if keys[pygame.K_LEFT]:
        player4_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player4_pos.x += 300 * dt

    if keys[pygame.K_LEFTBRACKET] and on_ground[4]:
        player_velocities[4] = -300
    if keys[pygame.K_SEMICOLON]:
        player5_pos.x -= 300 * dt
    if keys[pygame.K_RETURN]:
        player5_pos.x += 300 * dt
        

        
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()