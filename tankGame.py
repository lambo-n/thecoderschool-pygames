# Example file showing a circle moving on screen
import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

TANK_SPEED = 300
ROTATION_SPEED = 200

tank1_pos = pygame.Vector2(WIDTH / 4, HEIGHT / 4)
tank1_angle = 0

tank2_pos = pygame.Vector2(WIDTH - WIDTH / 4, HEIGHT - HEIGHT / 4)
tank2_angle = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Draw tank 1 (red) - body circle + barrel line
    pygame.draw.circle(screen, "red", tank1_pos, 40)
    barrel1_end = tank1_pos + pygame.Vector2(60, 0).rotate(-tank1_angle)
    pygame.draw.line(screen, "black", tank1_pos, barrel1_end, 10)

    # Draw tank 2 (blue) - body circle + barrel line
    pygame.draw.circle(screen, "blue", tank2_pos, 40)
    barrel2_end = tank2_pos + pygame.Vector2(60, 0).rotate(-tank2_angle)
    pygame.draw.line(screen, "black", tank2_pos, barrel2_end, 10)
    


    keys = pygame.key.get_pressed()
    # Tank 1: A/D rotate, W/S move forward/backward in barrel direction
    if keys[pygame.K_a]:
        tank1_angle += ROTATION_SPEED * dt
    if keys[pygame.K_d]:
        tank1_angle -= ROTATION_SPEED * dt
    if keys[pygame.K_w]:
        direction = pygame.Vector2(1, 0).rotate(-tank1_angle)
        tank1_pos += direction * TANK_SPEED * dt
    if keys[pygame.K_s]:
        direction = pygame.Vector2(1, 0).rotate(-tank1_angle)
        tank1_pos -= direction * TANK_SPEED * dt


    if keys[pygame.K_e]:
        pass

    # Tank 2: Left/Right rotate, Up/Down move forward/backward in barrel direction
    if keys[pygame.K_LEFT]:
        tank2_angle += ROTATION_SPEED * dt
    if keys[pygame.K_RIGHT]:
        tank2_angle -= ROTATION_SPEED * dt
    if keys[pygame.K_UP]:
        direction = pygame.Vector2(1, 0).rotate(-tank2_angle)
        tank2_pos += direction * TANK_SPEED * dt
    if keys[pygame.K_DOWN]:
        direction = pygame.Vector2(1, 0).rotate(-tank2_angle)
        tank2_pos -= direction * TANK_SPEED * dt
    if keys[pygame.K_RCTRL]:
        pass
        
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()